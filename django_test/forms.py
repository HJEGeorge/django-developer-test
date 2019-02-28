from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Field
from django import forms

from django_test.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('name'),
            ButtonHolder(
                Submit('submit', 'Submit')
            ),
        )
        super(PersonForm, self).__init__(*args, **kwargs)
