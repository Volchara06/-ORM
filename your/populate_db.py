import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your.settings')  # Замените 'your.settings'
django.setup()

from company.models import Branch, Department, Employee
from datetime import date

def populate():
    # Создаем несколько филиалов
    branch1 = Branch.objects.create(address="Москва, ул. Примерная, д. 1", short_name="Примерная 1")
    branch2 = Branch.objects.create(address="Санкт-Петербург, пр. Главный, д. 2", short_name="Главный 2")

    # Создаем отделы для филиалов
    dept1 = Department.objects.create(name="Отдел разработки", floor=3, branch=branch1)
    dept2 = Department.objects.create(name="Отдел продаж", floor=2, branch=branch1)
    dept3 = Department.objects.create(name="Отдел маркетинга", floor=4, branch=branch2)

    # Создаем сотрудников для отделов
    Employee.objects.create(full_name="Иван Иванов", position="Менеджер", date_of_birth=date(1990, 5, 15), department=dept1)
    Employee.objects.create(full_name="Петр Петров", position="Разработчик", date_of_birth=date(1985, 10, 20), department=dept1)
    Employee.objects.create(full_name="Анна Сидорова", position="Маркетолог", date_of_birth=date(1992, 3, 10), department=dept3)

if __name__ == '__main__':
    print("Populating the database...")
    populate()
    print("Done!")