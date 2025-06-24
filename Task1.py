name=input("Enter the student's name:").strip()

def get_marks(name):
    if not name:
        print("Student not found")
    else:
        print(f"{name}'s marks:{name_score[name]}")


get_marks(name)
