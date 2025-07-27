class Student:
    def __init__(self,roll_no, name, marks):
         self.roll_no=roll_no
         self.name = name
         self.marks=marks
    def display(self):
         print(f"Roll No:{self.roll_no},Name:{self.name},Marks:{self.marks}")
students =[]

while True:
     print("\n -- Student Management system")
     print("1.Add student")
     print("2.Display all student")
     print("3.search student by roll no")
     print("4.Exit")

     choice = input("Enter the choice you want to enter")

     if choice == '1':
          roll=input("Enter Roll no")
          name=input("Enter Name")
          marks= input("enter marks")
          student=Student(roll,name,marks)
          students.append(student)
          print("added successfully")
     elif choice == '2':
          if not students:
               print("class is empty")
          else:
               print("\n all student records")

               for s in students:
                    s.display()
     elif choice == '3':
          search_roll=input("enter roll no to search")
          found = False
          for s in students:
               if s.roll_no == search_roll:
                    print("student found")
                    s.display()
                    found=True
                    break
          if not found:
               print("student not found")
     elif choice == '4':
          print("exit")
          break
     else:
          print("Invalid choice")

               

          


               
        