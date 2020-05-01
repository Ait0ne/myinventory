import django_filters
from .models import Item, Layout
from django.contrib.auth.models import User
from django import forms
from django.db import models


def layout_qs(request):
    user=request.user
    return Layout.objects.filter(user=user)


class ItemFilter(django_filters.FilterSet):
    date_posted = django_filters.DateTimeFilter(label='Created',field_name='date_posted',lookup_expr='exact', widget=forms.DateInput(attrs={
        'type': 'date'
    }
    ))

    def filter_position_item(self, queryset, name, value):
        return queryset.filter()

    title = django_filters.CharFilter(label="Name contains", field_name='title', lookup_expr='icontains')
    type =django_filters.ChoiceFilter(label='Category', empty_label='All Categories', field_name='type', lookup_expr='exact', choices = Item.type_choices)
    position_item = django_filters.ModelChoiceFilter(label="Item's Location", empty_label='All locations', field_name='position_item', lookup_expr='exact', queryset= layout_qs)
    #position_item = django_filters.ChoiceFilter(label="Item's Location", field_name='position_item', lookup_expr='isnull', null_label = 'No location', choices = [x.position_item.position_layout for x in Item.objects.all()])

    class Meta:
        model = Item
        exclude =['image', 'author','size','info']













