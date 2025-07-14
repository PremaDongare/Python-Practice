# <!-- Write a Python program that allows a user to enter the names and marks of 5 students, then:
# Store the data in a dictionary where the key is the student's name and the value is their marks.
# Display:
# The average marks.
# The name(s) of the highest-scoring student(s).
# All students who scored more than the average. -->

studentmarks={}

for i in range(5):
   name= input(f"Enter the name of the student {i+1}:")
   while True:
      try:
         marks = float(input(f"Enter the marks{name}:"))
         break
      except ValueError:
         print("please enter correct marks")
   studentmarks[name]=marks

   #marks
   total_marks= sum(studentmarks.values())
   average_marks= total_marks/len(studentmarks)

   higestmarks= max(studentmarks.values())

   #topper
   topper=[]
   aboveaverage=[]
   for name, marks in studentmarks.items():
      if marks == higestmarks:
         topper.append(name)
      if marks>average_marks:
         aboveaverage.append(name)

print("---------Result-------")
print(f"average marks:{average_marks:.2f}")
print(f"Topper:{topper}")
print(f"above average:{aboveaverage}")



