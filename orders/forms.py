from django import forms
from .models import Order
import json

class OrderForm(forms.ModelForm):
    # Пользователь вводит список блюд в виде JSON-строки
    items = forms.CharField(
        widget=forms.Textarea,
        help_text='Введите список блюд в формате JSON, например: [{"name": "Блюдо1", "price": 10.50}, {"name": "Блюдо2", "price": 5.75}]'
    )
    
    class Meta:
        model = Order
        fields = ['table_number', 'items']
    
    def clean_items(self):
        data = self.cleaned_data['items']
        try:
            items = json.loads(data)
            if not isinstance(items, list):
                raise forms.ValidationError("Должен быть передан список блюд")
            for item in items:
                if 'name' not in item or 'price' not in item:
                    raise forms.ValidationError("Каждый элемент должен содержать 'name' и 'price'")
            return items
        except Exception:
            raise forms.ValidationError("Неверный формат JSON")
