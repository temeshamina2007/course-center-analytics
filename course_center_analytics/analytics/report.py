import json
import csv
import os


class BaseReport:
    def __init__(self, folder="reports"):
        self.folder = folder
        os.makedirs(self.folder, exist_ok=True)

    def save(self, data):
        raise NotImplementedError("Subclasses must implement save method")


class JsonReport(BaseReport):
    def save(self, data):
        file_path = f"{self.folder}/sales_report.json"

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print(f"JSON report saved to {file_path}")


class CsvReport(BaseReport):
    def save(self, enrollments):
        file_path = f"{self.folder}/cleaned_enrollments.csv"

        with open(file_path, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "student_name",
                "course_name",
                "category",
                "price",
                "paid_amount",
                "payment_status",
                "remaining_amount",
                "enrollment_date",
                "manager",
                "email"
            ])

            for enrollment in enrollments:
                writer.writerow([
                    enrollment.student_name,
                    enrollment.course_name,
                    enrollment.category,
                    enrollment.price,
                    enrollment.paid_amount,
                    enrollment.payment_status,
                    enrollment.remaining_amount(),
                    enrollment.enrollment_date,
                    enrollment.manager,
                    enrollment.email
                ])

        print(f"CSV report saved to {file_path}")