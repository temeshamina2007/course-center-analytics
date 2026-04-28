class Enrollment:
    def __init__(
        self,
        student_name,
        course_name,
        category,
        price,
        paid_amount,
        payment_status,
        enrollment_date,
        manager,
        email
    ):
        self.student_name = student_name
        self.course_name = course_name
        self.category = category
        self.price = float(price)
        self.paid_amount = float(paid_amount)
        self.payment_status = payment_status
        self.enrollment_date = enrollment_date
        self.manager = manager
        self.email = email

    def remaining_amount(self):
        return self.price - self.paid_amount

    def is_fully_paid(self):
        return self.payment_status.lower() == "paid"

    def __str__(self):
        return f"{self.student_name} - {self.course_name} - {self.payment_status}"


class OnlineEnrollment(Enrollment):
    def __init__(
        self,
        student_name,
        course_name,
        category,
        price,
        paid_amount,
        payment_status,
        enrollment_date,
        manager,
        email,
        platform="Zoom"
    ):
        super().__init__(
            student_name,
            course_name,
            category,
            price,
            paid_amount,
            payment_status,
            enrollment_date,
            manager,
            email
        )
        self.platform = platform

    def __str__(self):
        return f"{self.student_name} studies {self.course_name} online via {self.platform}"