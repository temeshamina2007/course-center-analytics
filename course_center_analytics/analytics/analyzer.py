from analytics.decorators import measure_time


class Analyzer:
    def __init__(self, enrollments):
        self.enrollments = enrollments

    @measure_time
    def total_revenue(self):
        return sum(enrollment.paid_amount for enrollment in self.enrollments)

    def expected_revenue(self):
        return sum(enrollment.price for enrollment in self.enrollments)

    def total_debt(self):
        return sum(enrollment.remaining_amount() for enrollment in self.enrollments)

    def average_check(self):
        if len(self.enrollments) == 0:
            return 0
        return self.total_revenue() / len(self.enrollments)

    def unique_courses(self):
        return set(enrollment.course_name for enrollment in self.enrollments)

    def revenue_by_course(self):
        result = {}

        for enrollment in self.enrollments:
            course = enrollment.course_name

            if course not in result:
                result[course] = 0

            result[course] += enrollment.paid_amount

        return result

    def students_by_course(self):
        result = {}

        for enrollment in self.enrollments:
            course = enrollment.course_name

            if course not in result:
                result[course] = 0

            result[course] += 1

        return result

    def payment_status_count(self):
        result = {
            "Paid": 0,
            "Partial": 0,
            "Unpaid": 0
        }

        for enrollment in self.enrollments:
            result[enrollment.payment_status] += 1

        return result

    def monthly_revenue(self):
        result = {}

        for enrollment in self.enrollments:
            month = enrollment.enrollment_date[:7]

            if month not in result:
                result[month] = 0

            result[month] += enrollment.paid_amount

        return result

    def paid_students(self):
        return list(filter(lambda enrollment: enrollment.payment_status == "Paid", self.enrollments))

    def prices_with_discount(self, discount_percent):
        return list(map(lambda enrollment: enrollment.price * (1 - discount_percent / 100), self.enrollments))

    def top_courses_by_revenue(self):
        revenue = self.revenue_by_course()

        sorted_courses = sorted(
            revenue.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return sorted_courses

    def create_summary(self):
        return {
            "total_students": len(self.enrollments),
            "unique_courses": list(self.unique_courses()),
            "total_revenue": self.total_revenue(),
            "expected_revenue": self.expected_revenue(),
            "total_debt": self.total_debt(),
            "average_check": self.average_check(),
            "revenue_by_course": self.revenue_by_course(),
            "students_by_course": self.students_by_course(),
            "payment_status_count": self.payment_status_count(),
            "monthly_revenue": self.monthly_revenue(),
            "top_courses_by_revenue": self.top_courses_by_revenue()
        }