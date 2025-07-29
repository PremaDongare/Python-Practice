class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name= name
        self.courses =[]
    def enroll(self,course):
        try:
            if course not in self.courses:
                self.courses.append(course)
                print(f"{self.name} enrolled in {course}.")
            else:
                print(f"{self.name} is alredy enrolled in {course}")
        except Exception as e:
            print(f"Error while enrollingin course:{e}")

    def showcourse(self):
        try:
            if self.courses:
                print(f"{self.name} is enrolled in {','.join(self.courses)}")
            else:
                print(f"{self.nsme} is not enroll in any course")
        except Exception as e:
            print(f"Error in displaying course:{e}")
def main():
    try:
        students={}

        while True:
            print("\n1 Add Student\n2.Enroll in course\n3.Show Course\n4. Exit")
            choice = input("Enter your choice:")

            if choice == '1':
                try:
                    roll=input("Enter Roll no:").strip()
                    name = input("Enter Name:").strip()
                    if roll not in students:
                        students[roll]=Student(roll,name)
                        print("Student added successfully")
                    else:
                        print("Student alredy exist.")
                except Exception as e:
                    print(f"Error adding student:{e}")
            elif choice == '2':
                try:
                    roll=input("enter roll no").strip()
                    if roll in students:
                        course= input("Enter course name to enter").strip()
                        students[roll].enroll(course)
                    else:
                        print("student not found")
                except Exception as e:
                    print(f"Error enrolling course:{e}")

            elif choice == '3':
                try:
                    roll=input("Enter Roll Number:").strip()
                    if roll in students:
                        students[roll].showcourse()
                    else:
                        print("Student not found.")
                except Exception as e:
                    print(f"Error showing courses:{e}")
            elif choice == '4':
                print("Exiting....")
                break
            else:
                print("Invalid choice. Try again")
    except Exception as e:
        print(f"Unexpected error:{e}")

if __name__ == "__main__":
    main()