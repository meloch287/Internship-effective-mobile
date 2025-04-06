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
