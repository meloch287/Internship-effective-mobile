from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('waiting', 'В ожидании'),
        ('ready', 'Готово'),
        ('paid', 'Оплачено'),
    ]
    
    table_number = models.PositiveIntegerField()
    # Сохраняем список блюд в формате JSON (каждый элемент: словарь с 'name' и 'price')
    items = models.JSONField(default=list)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='waiting')
    
    def save(self, *args, **kwargs):
        # Рассчитываем общую стоимость заказа
        self.total_price = sum(item.get('price', 0) for item in self.items)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"Order #{self.id} for Table {self.table_number}"


class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('snack', 'Закуски'),
        ('drink', 'Напитки'),
        # и т.д.
    ]
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.price}₽)"

