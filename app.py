import datetime

students = [
    {"name": "John Okello", "id_number": "101", "Year": "Freshman"},
    {"name": "Mary Kamasia", "id_number": "102", "Year": "Freshman"},
    {"name": "Aaron Kavu", "id_number": "103", "Year": "Sophmore"},
    {"name": "Ken Thita", "id_number": "104", "Year": "Freshman"},
    {"name": "Mercy Rino", "id_number": "105", "Year": "Freshman"},
    {"name": "Will Lawrence", "id_number": "106", "Year": "Freshman"},
    {"name": "Ryan Yamer", "id_number": "107", "Year": "Sophmore"},
    {"name": "Ellaine Nixon", "id_number": "108", "Year": "Freshman"},
    {"name": "Indigo Dilla", "id_number": "109", "Year": "Freshman"},
    {"name": "Bryan Rinin", "id_number": "110", "Year": "Freshman"}
]


def find_student_by_id(student_id):
    for student in students:
        if student['id_number'] == student_id:
            return student
    return None


def read_subject_scores(subjects):
    scores = {}
    for subject in subjects:
        score = float(input(f"Enter score for {subject}: "))
        scores[subject] = score
    return scores


def calculate_average(scores):
    return sum(scores.values()) / len(scores)


def calculate_grade(average_score):
    if average_score >= 90:
        return 'A'
    elif average_score >= 80:
        return 'B'
    elif average_score >= 70:
        return 'C'
    elif average_score >= 60:
        return 'D'
    else:
        return 'F'


def recommendation(average_score):
    if average_score >= 70:
        return 'Good'
    else:
        return 'Poor'


def display_report_card(student, scores, average_score, grade, recommendation):
    print('\n*************************************************************************')
    print("UNITED STATES INTERNATIONAL UNIVERSITY")
    print("P.O BOX 1223228, NAIROBI")
    print("KENYA")
    print("--------------------------------------------------------------------------")
    print("\nEND TERM REPORT FORM")
    print("Name:", student['name'])
    print("ID Number:", student['id_number'])
    print("Subjects and Scores:")
    for subject, score in scores.items():
        print(f"{subject}: {score}")
    print("Average Score:", average_score)
    print("Grade:", grade)
    print("Recommendation:", recommendation)
    print("Date:", datetime.date.today())


def main():
    subjects = ['MTH1000', 'ENG1000', 'SCI1000', 'PHL1000', 'ART1000']

    while True:
        student_id = input("Enter the ID of the student (or type 'exit' to quit): ")
        if student_id.lower() == 'exit':
            break
        student = find_student_by_id(student_id)
        if student:
            print(f"\nEnter scores for {student['name']}:")
            scores = read_subject_scores(subjects)
            average_score = calculate_average(scores)
            grade = calculate_grade(average_score)
            rec = recommendation(average_score)
            display_report_card(student, scores, average_score, grade, rec)
        else:
            print("Student not found. Please enter a valid ID.")


if __name__ == "__main__":
    main()