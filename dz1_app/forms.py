import datetime

from django import forms

from dz1_app.models import Product


# Задание №6
# 📌 Доработаем задачу про клиентов, заказы и товары из
# прошлого семинара.
# 📌 Создайте форму для редактирования товаров в базе
# данных.

class ProductEditForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'image']