from django import forms
from .widgets import LayoutCreateWidget
from django.db import models
from django.core.exceptions import ValidationError

class LayoutCreateField(forms.MultiValueField):
    widget = LayoutCreateWidget
    def __init__(self,  *args, **kwargs):

        fields= (
            forms.CharField(max_length=20, label='Add Location', required=True),
            forms.CharField(max_length=20,label='Provide customary location', required=True))
        super(LayoutCreateField,self).__init__(fields,require_all_fields=True,*args,**kwargs)


    def compress(self, data_list):
        if data_list[0]=='Customary':
            if data_list[1]=='':
                raise ValidationError('You need to provide customary location')
            return data_list[1]
        return data_list[0]

class LayoutField(models.CharField):
    def formfield(self, **kwargs):
        return super(LayoutField,self).formfield(form_class=LayoutCreateField)