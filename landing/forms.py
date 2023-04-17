from django import forms
from .models import Lead


class LeadForm(forms.ModelForm):
    class Meta: # Изменение поведения модели и связка формы LeadForm с моделью Lead
        model = Lead # перечисление необходимых полей, которые будут показываться на экране
        fields = ['name','last_name','phone_number']



