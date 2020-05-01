from django import forms
from .models import Layout, Item
from .fields import LayoutField, LayoutCreateField
from .widgets import LayoutCreateWidget



class LayoutForm(forms.ModelForm):

    position_layout = LayoutCreateField(label='Add Location', required=False)

    class Meta:
        model = Layout
        fields = ['position_layout']

    def __init__(self, *args, **kwargs):
        self.request=kwargs.pop('user')
        super(LayoutForm,self).__init__(*args,**kwargs)


    def clean_position_layout(self):
        value = self.cleaned_data['position_layout']
        if Layout.objects.filter(position_layout=value).filter(user=self.request.user).count()>0:
            raise forms.ValidationError("This location has already been added!")
        return value





class   ItemForm(forms.ModelForm):


    position_item = forms.ModelChoiceField(label="Item's Location",queryset=Layout.objects.all())

    class Meta:
        model = Item
        fields=['title','type','position_item','size','info','image']

        labels = {
            'image': 'Photo',
            'title': "Item's Name",
            'type': 'Category',
            'size': 'Size',
            'info': 'Item Details'
        }
        required = {
            'size': False,
            'info': False
        }


    def __init__(self, *args,**kwargs):
        user = kwargs.pop('user')
        super(ItemForm,self).__init__(*args,**kwargs)
        self.fields['position_item'].queryset = Layout.objects.filter(user=user)
