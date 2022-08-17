from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
from django.forms import inlineformset_factory
from django import forms
from django_aux.forms import BaseModelForm
from main.models import *

class PersonForm(BaseModelForm):
    class Meta:
        model = Person
        exclude = []
        widgets = {
            'adjectives': forms.CheckboxSelectMultiple
        }


class PersonHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.form_tag = False
        self.layout = Layout(
            Row(
               Div('org',css_class='ml-2 col-flex'),
               Div('first_name',css_class='ml-2 col-flex'),
               Div('middle_name',css_class='ml-2 col-flex'),
               Div('last_name',css_class='ml-2 col-flex'),
               Div('salary',css_class='ml-2 col-flex'),
               Div('adjectives',css_class='ml-2 col-flex'),
            )       
        )    

class PersonAwardHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.form_tag = False
        self.layout = Layout(
            Row(
               Div('type',css_class='ml-2 col-flex'),
               Div('DELETE',css_class='ml-2 col-flex'),
            )       
        )    


award_factory = inlineformset_factory(
    parent_model=Person,
    model=PersonAward,
    exclude = [],
    extra = 1,
)