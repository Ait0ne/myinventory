from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Item, Layout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from enhanced_cbv.views.list import ListFilteredMixin
from.filters import ItemFilter
from .forms import LayoutForm, ItemForm
from.tables import LayoutTable
from django_tables2 import SingleTableMixin
from django.contrib.messages.views import SuccessMessageMixin




class MainListView(ListFilteredMixin, ListView):
    model = Item
    template_name = 'main/home.html'
    context_object_name = 'items'
    ordering = ['-date_posted']
    paginate_by = 9
    filter_set=ItemFilter


    def get_base_queryset(self):
        if self.request.user.is_authenticated:
            return Item.objects.filter(author=self.request.user).order_by('-date_posted')
        return None

    def get_filter_set_kwargs(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return {
                'data': self.request.GET,
                'queryset': self.get_base_queryset(),
                'request':self.request,
            }
        return {**kwargs}



# class ItemDetailView(DetailView):
#     model = Item


class ItemCreateView(SuccessMessageMixin,LoginRequiredMixin, CreateView):
    model = Item

    form_class = ItemForm
    success_url = '/item/new/'
    success_message = 'Item has been successfully added!'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        form_kwargs = super(ItemCreateView,self).get_form_kwargs()
        form_kwargs.update({'user':self.request.user})
        return form_kwargs



class ItemUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'main/item_detail.html'
    success_message = 'Item has been successfully updated!'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.author:
            return True
        return False

    def get_form_kwargs(self):
        form_kwargs = super(ItemUpdateView,self).get_form_kwargs()
        form_kwargs.update({'user':self.request.user})
        return form_kwargs




class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Item
    success_url = '/'

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.author:
            return True
        return False



class LayoutCreateView(SingleTableMixin, LoginRequiredMixin, CreateView):
    model = Layout
    table_class = LayoutTable
    context_object_name = 'layouts'
    table_pagination = {
        "per_page": 10
    }

    form_class = LayoutForm

    def get_queryset(self):
        return Layout.objects.filter(user=self.request.user)


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        form_kwargs = super(LayoutCreateView,self).get_form_kwargs()
        form_kwargs.update({'user':self.request})
        return form_kwargs



class LayoutDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Layout
    success_url = '/layout/new'

    def test_func(self):
        layout = self.get_object()
        if self.request.user == layout.user:
            return True
        return False