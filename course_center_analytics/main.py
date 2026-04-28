from analytics.data_loader import DataLoader
from analytics.analyzer import Analyzer
from analytics.visualizer import Visualizer
from analytics.report import JsonReport, CsvReport


def print_menu():
    print("\nCOURSE CENTER SALES ANALYTICS")
    print("1. Show summary")
    print("2. Show revenue by course")
    print("3. Show students by course")
    print("4. Show payment status")
    print("5. Generate charts")
    print("6. Save reports")
    print("7. Show top courses by revenue")
    print("0. Exit")


def main():
    file_path = "data/enrollments.csv"

    try:
        loader = DataLoader(file_path)
        enrollments = loader.load_data()

        analyzer = Analyzer(enrollments)
        visualizer = Visualizer()

        while True:
            print_menu()
            choice = input("Choose option: ")

            if choice == "1":
                summary = analyzer.create_summary()

                print("\nSUMMARY")
                print(f"Total students: {summary['total_students']}")
                print(f"Unique courses: {summary['unique_courses']}")
                print(f"Total revenue: {summary['total_revenue']}")
                print(f"Expected revenue: {summary['expected_revenue']}")
                print(f"Total debt: {summary['total_debt']}")
                print(f"Average check: {summary['average_check']:.2f}")

            elif choice == "2":
                print("\nREVENUE BY COURSE")
                for course, revenue in analyzer.revenue_by_course().items():
                    print(f"{course}: {revenue}")

            elif choice == "3":
                print("\nSTUDENTS BY COURSE")
                for course, count in analyzer.students_by_course().items():
                    print(f"{course}: {count}")

            elif choice == "4":
                print("\nPAYMENT STATUS")
                for status, count in analyzer.payment_status_count().items():
                    print(f"{status}: {count}")

            elif choice == "5":
                visualizer.revenue_by_course_chart(analyzer.revenue_by_course())
                visualizer.students_by_course_chart(analyzer.students_by_course())
                visualizer.monthly_revenue_chart(analyzer.monthly_revenue())
                visualizer.payment_status_chart(analyzer.payment_status_count())

                print("Charts were generated in the charts folder.")

            elif choice == "6":
                summary = analyzer.create_summary()

                json_report = JsonReport()
                csv_report = CsvReport()

                json_report.save(summary)
                csv_report.save(enrollments)

                print("Reports were saved in the reports folder.")

            elif choice == "7":
                print("\nTOP COURSES BY REVENUE")
                for course, revenue in analyzer.top_courses_by_revenue():
                    print(f"{course}: {revenue}")

            elif choice == "0":
                print("Program finished.")
                break

            else:
                print("Invalid option. Try again.")

    except FileNotFoundError as error:
        print(error)

    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()