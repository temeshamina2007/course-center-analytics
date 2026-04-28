import csv
import os

from analytics.models import Enrollment
from analytics.validators import validate_email, validate_payment_status, validate_positive_number


class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def check_file_exists(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File was not found: {self.file_path}")

    def read_enrollments_generator(self):
        self.check_file_exists()

        with open(self.file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if not validate_email(row["email"]):
                    print(f"Invalid email skipped: {row['email']}")
                    continue

                if not validate_payment_status(row["payment_status"]):
                    print(f"Invalid payment status skipped: {row['payment_status']}")
                    continue

                if not validate_positive_number(row["price"]):
                    print(f"Invalid price skipped: {row['price']}")
                    continue

                enrollment = Enrollment(
                    row["student_name"],
                    row["course_name"],
                    row["category"],
                    row["price"],
                    row["paid_amount"],
                    row["payment_status"],
                    row["enrollment_date"],
                    row["manager"],
                    row["email"]
                )

                yield enrollment

    def load_data(self):
        return list(self.read_enrollments_generator())