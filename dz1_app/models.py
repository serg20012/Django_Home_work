from django.db import models

# Задание №8
# 📌 Создайте три модели Django: клиент, товар и заказ. Клиент
# может иметь несколько заказов. Заказ может содержать
# несколько товаров. Товар может входить в несколько
# заказов.
# 📌 Поля модели "Клиент":
# ○ имя клиента
# ○ электронная почта клиента
# ○ номер телефона клиента
# ○ адрес клиента
# ○ дата регистрации клиента
#
# Поля модели "Товар":
# ○ название товара
# ○ описание товара
# ○ цена товара
# ○ количество товара
# ○ дата добавления товара
#
#  Поля модели "Заказ":
# ○ связь с моделью "Клиент", указывает на клиента, сделавшего заказ
# ○ связь с моделью "Товар", указывает на товары, входящие в заказ
# ○ общая сумма заказа
# ○ дата оформления заказа
#
# 📌 *Допишите несколько функций CRUD для работы с
# моделями по желанию. Что по вашему мнению актуально в
# такой базе данных.

from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    added_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='product_photos/', null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.client.name}"

# функций CRUD (дополнить позже)!!!!
#
# # Create
# def create_client(name, email, phone_number, address):
#     return Client.objects.create(name=name, email=email, phone_number=phone_number, address=address)
#
# def create_product(name, description, price, quantity):
#     return Product.objects.create(name=name, description=description, price=price, quantity=quantity)
#
# def create_order(client, products, total_amount):
#     return Order.objects.create(client=client, products=products, total_amount=total_amount)
#
# # Read
# def get_clients():
#     return Client.objects.all()
#
# def get_products():
#     return Product.objects.all()
#
# def get_orders():
#     return Order.objects.all()
#
# # Update
# def update_client(client_id, **kwargs):
#     client = Client.objects.get(id=client_id)
#     for key, value in kwargs.items():
#         setattr(client, key, value)
#     client.save()
#
# def update_product(product_id, **kwargs):
#     product = Product.objects.get(id=product_id)
#     for key, value in kwargs.items():
#         setattr(product, key, value)
#     product.save()
#
# def update_order(order_id, **kwargs):
#     order = Order.objects.get(id=order_id)
#     for key, value in kwargs.items():
#         setattr(order, key, value)
#     order.save()
#
# # Delete
# def delete_client(client_id):
#     Client.objects.get(id=client_id).delete()
#
# def delete_product(product_id):
#     Product.objects.get(id=product_id).delete()
#
# def delete_order(order_id):
#     Order.objects.get(id=order_id).delete()
#
#
# if __name__ == '__main__':
#     new_client = create_client(
#         name='Иван Иванов',
#         email='ivan@example.com',
#         phone_number='123-456-7890',
#         address='Улица Пушкина, дом Колотушкина')