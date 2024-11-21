# cli_interface.py
from core import StudentAnalyzer

def display_menu():
    print("\n=== Student Lifestyle Analysis ===")
    print("1. Show Basic Statistics")
    print("2. Show Study Hours Impact")
    print("3. Show Stress Level Impact")
    print("4. Show Top Performers' Habits")
    print("5. Exit")
    return input("\nChoose an option (1-5): ")

def show_basic_stats(analyzer):
    stats = analyzer.get_basic_stats()
    print("\n=== Basic Statistics ===")
    print(f"Total Students: {stats['total_students']}")
    print(f"Average CGPA: {stats['average_cgpa']}")
    print(f"Average Study Hours: {stats['average_study_hours']}")
    print(f"Average Sleep Hours: {stats['average_sleep_hours']}")
    print(f"Average Physical Activity Hours: {stats['average_physical_hours']}")

def show_study_impact(analyzer):
    impact = analyzer.get_study_impact()
    print("\n=== Impact of Study Hours on CGPA ===")
    print("Study Hours | Average CGPA")
    print("-" * 25)
    for hours, cgpa in impact.items():
        print(f"{hours:9} | {cgpa}")

def show_stress_impact(analyzer):
    impact = analyzer.get_stress_impact()
    print("\n=== Impact of Stress Level on CGPA ===")
    print("Stress Level | Average CGPA")
    print("-" * 25)
    for level, cgpa in impact.items():
        print(f"{level:11} | {cgpa}")

def show_top_performers(analyzer):
    habits = analyzer.find_top_performers()
    print("\n=== Top Performers' Average Habits ===")
    print(f"Study Hours: {habits['study_hours']}")
    print(f"Sleep Hours: {habits['sleep_hours']}")
    print(f"Physical Activity Hours: {habits['physical_hours']}")
    print(f"Average CGPA: {habits['average_cgpa']}")

def main():
    try:
        analyzer = StudentAnalyzer('student_lifestyle_dataset.csv')
        
        while True:
            choice = display_menu()
            
            if choice == '1':
                show_basic_stats(analyzer)
            elif choice == '2':
                show_study_impact(analyzer)
            elif choice == '3':
                show_stress_impact(analyzer)
            elif choice == '4':
                show_top_performers(analyzer)
            elif choice == '5':
                print("\nGoodbye!")
                break
            else:
                print("\nInvalid choice. Please try again.")
            
            input("\nPress Enter to continue...")

    except FileNotFoundError:
        print("\nError: Data file not found!")
    except Exception as e:
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    main()