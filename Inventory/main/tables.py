from .models import Layout
from django_tables2 import tables
from django.utils.safestring import mark_safe
from django_tables2.utils import A


class MaterializeCssCheckboxColumn(tables.columns.CheckBoxColumn):
    def render(self, value, bound_column, record):
        default = {"type": "checkbox", "name": bound_column.name, "value": value}
        if self.is_checked(value, record):
            default.update({"checked": "checked"})

        general = self.attrs.get("input")
        specific = self.attrs.get("td__input")
        attrs = tables.AttributeDict(default, **(specific or general or {}))
        return mark_safe("<p><label><input %s/><span></span></label></p>" % attrs.as_html())




class LayoutTable(tables.Table):
    position_layout = tables.columns.Column(verbose_name='Locations',linkify=('layout-delete', {'pk': A('pk')}))
    # check = MaterializeCssCheckboxColumn(accessor='position_layout')
    #delete = tables.columns.Column(linkify=('layout-delete', {'pk': A('pk')}))

    class Meta:
        model = Layout
        fields=['position_layout']
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {'class':'table table-hover table-responsive text-dark'}
