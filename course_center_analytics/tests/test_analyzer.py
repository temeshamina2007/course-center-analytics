from analytics.models import Enrollment
from analytics.analyzer import Analyzer


def test_total_revenue():
    enrollments = [
        Enrollment("A", "Python", "Programming", 100000, 100000, "Paid", "2026-01-01", "Amina", "a@gmail.com"),
        Enrollment("B", "IELTS", "Languages", 90000, 30000, "Partial", "2026-01-02", "Amina", "b@gmail.com")
    ]

    analyzer = Analyzer(enrollments)

    assert analyzer.total_revenue() == 130000


def test_total_debt():
    enrollments = [
        Enrollment("A", "Python", "Programming", 100000, 100000, "Paid", "2026-01-01", "Amina", "a@gmail.com"),
        Enrollment("B", "IELTS", "Languages", 90000, 30000, "Partial", "2026-01-02", "Amina", "b@gmail.com")
    ]

    analyzer = Analyzer(enrollments)

    assert analyzer.total_debt() == 60000