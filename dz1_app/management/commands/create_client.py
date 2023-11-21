# Импортируйте ваш файл с функциями CRUD
from django.core.management.base import BaseCommand
from dz1_app.models import Client

class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        new_client = Client(
            name='Иван Иванов',
            email='ivan@example.com',
            phone_number='123-456-7890',
            address='Улица Пушкина, дом Колотушкина')
        new_client.save()
        self.stdout.write(self.style.SUCCESS('User'))
