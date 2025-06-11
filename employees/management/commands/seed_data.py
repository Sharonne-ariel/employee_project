from django.core.management.base import BaseCommand
from employees.models import Employee, Department, Attendance, Performance
from faker import Faker
import random

class Command(BaseCommand):
    help = "Seed the database with dummy data"

    def handle(self, *args, **options):
        fake = Faker()

        # 🧹 Clear old data to avoid duplicates
        Performance.objects.all().delete()
        Attendance.objects.all().delete()
        Employee.objects.all().delete()
        Department.objects.all().delete()

        # 🏢 Create Departments
        departments = ['HR', 'Engineering', 'Marketing', 'Sales', 'Finance']
        for dep_name in departments:
            Department.objects.create(name=dep_name)

        # 👨‍💼 Create Employees with Attendance + Performance
        for _ in range(50):
            dept = Department.objects.order_by('?').first()
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number(),
                address=fake.address(),
                date_of_joining=fake.date_between(start_date='-2y', end_date='today'),
                department=dept,
            )

            # 🌟 Create Performance Reviews
            Performance.objects.create(
                employee=emp,
                rating=random.randint(1, 5),
                review_date=fake.date_this_year()
            )

            # 🕒 Create Attendance Entries (P = Present, A = Absent, L = Late)
            for _ in range(5):
                Attendance.objects.create(
                    employee=emp,
                    date=fake.date_this_year(),
                    status=random.choice(['P', 'A', 'L'])  # 'P' = Present, 'A' = Absent, 'L' = Late
                )

        fake.unique.clear()  # Reset unique constraint
        self.stdout.write(self.style.SUCCESS('✅ Database seeded successfully!'))
