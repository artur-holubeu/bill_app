from django import forms

from .models import Bills


class BillForm(forms.ModelForm):
    class Meta:
        model = Bills
        fields = ('user_id', 'count')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form_field'
            if field == 'count':
                self.fields[field].widget.attrs['min'] = '1'
