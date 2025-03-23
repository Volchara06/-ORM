import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your.settings')
django.setup()

from django.db.models import Q
from company.models import Employee, Department, Branch

# 1. Получи количество сотрудников с должностью “Менеджер”
query_1 = Employee.objects.filter(position='Менеджер').count()

# 2. Получи список сотрудников, работающих на четвертых этажах
query_2 = Employee.objects.filter(department__floor=4)

# 3. Получи список всех сотрудников, работающих в этих двух филиалах, с помощью Q
branch_ids = [1, 2]
query_3 = Employee.objects.filter(Q(department__branch_id=branch_ids[0]) | Q(department__branch_id=branch_ids[1]))

# 4. Получи список сотрудников, работающих в тех же двух филиалах из прошлого вопроса, только вместо Q используй лукап, проверяющий вхождение ID в список
query_4 = Employee.objects.filter(department__branch_id__in=branch_ids)

# 5. Получи список ФИО сотрудников, у которых не указан email
query_5 = Employee.objects.filter(email__isnull=True).values_list('full_name', flat=True)

# 6. Получи список сотрудников, чей год рождения 1990.
query_6 = Employee.objects.filter(date_of_birth__year=1990)

# Для проверки в консоли (уберите, если нужно просто определения запросов)
print(f"Query 1: {query_1}")
print(f"Query 2: {query_2}")
print(f"Query 3: {query_3}")
print(f"Query 4: {query_4}")
print(f"Query 5: {query_5}")
print(f"Query 6: {query_6}")