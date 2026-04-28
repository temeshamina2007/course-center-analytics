import os
import matplotlib.pyplot as plt


class Visualizer:
    def __init__(self, charts_folder="charts"):
        self.charts_folder = charts_folder
        os.makedirs(self.charts_folder, exist_ok=True)

    def revenue_by_course_chart(self, data):
        courses = list(data.keys())
        revenues = list(data.values())

        plt.figure(figsize=(10, 6))
        plt.bar(courses, revenues)
        plt.title("Revenue by Course")
        plt.xlabel("Course")
        plt.ylabel("Revenue")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.savefig(f"{self.charts_folder}/revenue_by_course.png")
        plt.close()

    def students_by_course_chart(self, data):
        courses = list(data.keys())
        students = list(data.values())

        plt.figure(figsize=(10, 6))
        plt.bar(courses, students)
        plt.title("Students by Course")
        plt.xlabel("Course")
        plt.ylabel("Number of Students")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.savefig(f"{self.charts_folder}/students_by_course.png")
        plt.close()

    def monthly_revenue_chart(self, data):
        months = list(data.keys())
        revenues = list(data.values())

        plt.figure(figsize=(10, 6))
        plt.plot(months, revenues, marker="o")
        plt.title("Monthly Revenue")
        plt.xlabel("Month")
        plt.ylabel("Revenue")
        plt.tight_layout()
        plt.savefig(f"{self.charts_folder}/monthly_revenue.png")
        plt.close()

    def payment_status_chart(self, data):
        statuses = list(data.keys())
        counts = list(data.values())

        plt.figure(figsize=(8, 8))
        plt.pie(counts, labels=statuses, autopct="%1.1f%%")
        plt.title("Payment Status")
        plt.tight_layout()
        plt.savefig(f"{self.charts_folder}/payment_status.png")
        plt.close()