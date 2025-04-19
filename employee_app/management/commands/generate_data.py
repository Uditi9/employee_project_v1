from django.core.management.base import BaseCommand
from faker import Faker
import random
from datetime import datetime, timedelta
from employee_app.models import Department, Employee, Attendance, Performance

class Command(BaseCommand):
    help = 'Generate synthetic employee data'

    def handle(self, *args, **options):
        fake = Faker()
        departments = ['HR','Engineering','Sales','Marketing']
        for d in departments:
            Department.objects.get_or_create(name=d)
        for _ in range(5):
            dept = Department.objects.order_by('?').first()
            emp = Employee.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                department=dept,
                date_joined=fake.date_between(start_date='-2y', end_date='today')
            )
            # Attendance for past 7 days
            for i in range(7):
                date = datetime.today().date() - timedelta(days=i)
                Attendance.objects.create(employee=emp, date=date, status=random.choice(['P','A']))
            # Performance records
            for i in range(3):
                review_date = datetime.today().date() - timedelta(days=i*30)
                Performance.objects.create(employee=emp, score=random.randint(1,10), review_date=review_date, comments=fake.sentence())
        self.stdout.write(self.style.SUCCESS('Data generated'))
