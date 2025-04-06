# forms.py
from django import forms
from .models import Order, MenuItem

class OrderForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(
        queryset=MenuItem.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        help_text='Выберите одно или несколько блюд'
    )

    class Meta:
        model = Order
        fields = ['table_number', 'items']

    def clean_items(self):
        # возвращаем список словарей с name и price
        menu_items = self.cleaned_data['items']
        return [{"name": item.name, "price": float(item.price)} for item in menu_items]
