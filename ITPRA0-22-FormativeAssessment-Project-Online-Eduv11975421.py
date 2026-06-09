#Anzel Schoon
#2026/05/31
#Learner Progress Tracking System to track learners, their marks and their performance

import tkinter as tk
from tkinter import messagebox

# Initialize a hidden Tkinter root window so messageboxes function properly without causing visual bugs
root = tk.Tk()
root.withdraw()

#global list where learners that are added are stored
learnersDatabase = []
def main():
     mainMenu()



#CLASSES
#Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Learner(Person):

    def __init__(self, name, age,learnerId, course):
        super().__init__(name, age)
        self.learnerId = learnerId
        self.course = course
        self.__marks = []
    #Methods
    def getMarks(self):
         return self.__marks
        
    def average(self):
         marksList = self.getMarks()
         #average of a student's marks
         try:
             return sum(marksList)/len(marksList)
         #you can't divide by 0
         except ZeroDivisionError: 
             if marksList == []:
                  messagebox.showinfo('Error', "Marks is empty" )
                  return 0.0
        
        #figure out a students performance based on there average
    def performance(self):
         avg = self.average()
         markList = self.getMarks()
         if markList == []:
              return 'No marks entered' 
         elif avg < 50:
             return "Fail"
         elif avg < 75:
              return 'Pass'
         else:
              return 'Pass with Distinction'
             
    def qualifiesForCertificate(self):
         if self.average() >= 50:
             return True
         return False
             

#Main Menu
#controls navigation 
def mainMenu():
     while True:    #conditioned controlled loop
         print(f" {'='*5}Learner Progress Tracking System {'='*5}")
         print("1. Add learner")
         print("2. Enter marks")
         print("3. View all learners")
         print("4. Search learner")
         print("5. Update learner")
         print("6. Remove learner")
         print("7. Show learner result")
         print("8. Exit")
        
        #get input
         choice = input("Enter your choice:").strip()
         #Validate user input and make sure it is a option
         optionList = ['1', '2', '3', '4', '5', '6', '7', '8']
         if choice not in optionList:
               messagebox.showerror('Error', 'Not valid input')
               continue
         if choice == '1':
            addLearner()
         elif choice == '2':
            enterMarks()
         elif choice == '3':
            viewAllLearner()
         elif choice == '4':
            searchLearner()
         elif choice == '5':
            updateLearner()
         elif choice == '6':
            removeLearner()
         elif choice == '7':
            displayResults()
         elif choice == '8':
             if exitProgram():
                 print("Exiting program, Goodbye :)")
                 break


#Main Menu Function
#1. add learner
def addLearner():
       #take input
    learnerId = input("Enter learner ID: ")
     #Check if learner ID already exist to prevent duplication
    student = searchId(learnerId)
    if student:
         messagebox.showinfo('Error', 'ID already exist')
         return
    else:  
         name = input("Enter learner name: ")
         try:
             age = int(input("Enter learner age: "))
             #validate age input  
             # Note: The  exact age was not specified in requirements
             if 0 < age < 100:
                  course = input("Enter course name: ")
                  newStudent = Learner(name, age, learnerId, course)
                  learnersDatabase.append(newStudent)
                  messagebox.showinfo('Success', 'Learner added successfully!')
             else:
                 messagebox.showinfo('Error', 'Age is not valid')
                 return

         except ValueError:
              messagebox.showerror('Error', 'Invalid age. Please enter a valid number.')
              return
    

#2. Enter marks
def enterMarks():
      #search for learner that gets the marks
      targetId = input('Enter learner ID: ')
      learner = searchId(targetId)
      if learner:
            try:
                  entries = int(input('How many marks to you want to enter: '))
            except ValueError:
                  messagebox.showinfo('Error', 'Invalid input')
                  return
                
            for i in range(entries):
                  try:
                     test = float(input(f'Enter mark {i+1}: '))
                     #validate marks
                     #Note: exact range of marks was not specified in requirements
                     if 0 <= test <= 100:
                         learner.getMarks().append(test)
                         continue
                     else:
                          messagebox.showinfo('Error', 'Invalid mark')
                          continue
                     #if user type somthing in that is not a number
                  except ValueError:
                       messagebox.showinfo('Error', 'Invalid mark entered')
                       continue
                       
            messagebox.showinfo('System Message', 'Marks captured successfully')
            
      else:
           messagebox.showinfo('Error', 'Learner not found')
           
                        
#3. view learner
def viewAllLearner():
      if learnersDatabase == []:
            messagebox.showinfo('No Learners', 'No learners found in the database.')
            return
      
      total_students = recursiveTotalLearners(learnersDatabase)
      print(f"\nTotal Registered Students: {total_students}")
      
      #loopthrough learner database
      for student in learnersDatabase:
         summary(student)
               
#4.Search for a learner
def searchLearner():
      #ask for learner ID
      targetId = input("Enter learner ID to search: ")
      learner = searchId(targetId)
      if learner:  #learner found
        summary(learner)
      else:
           messagebox.showinfo('Not Found', 'Learner not found.')

#5. Update learner
def updateLearner():
       #ask for learner ID
      targetId = input("Enter learner ID to update: ")
      learner = searchId(targetId)
      if learner:
             newName = input('Enter new name: ').strip()
             try:
                 newAge = int(input('Enter new age: ').strip())
             except:
                   messagebox.showerror('Error', 'Invalid age')
                   return
             newCourse = input('Enter new course: ').strip()
        
             learner.age = newAge
             learner.name = newName
             learner.course = newCourse
             messagebox.showinfo('Success', 'Learner updated successfully')
      else:
         messagebox.showinfo('Not found', 'Learner not found')



#6. Remove learner
def removeLearner():
     #search learner
     targetID = input('Enter learner ID to remove: ')
     learner = searchId(targetID)
     if learner:
           learnersDatabase.remove(learner)
           messagebox.showinfo('Success', 'Learner removed successfully')
     else:
         messagebox.showinfo('Error', 'Learner not found')

#7. Show learner result
def displayResults():
      targetId = input('Enter learner ID: ')
      learner = searchId(targetId)
      if learner:
            print(f'Results for {learner.name}')
            print(f'Average: {learner.average()} ')
            print(f'Performance: {learner.performance()}')
            if learner.qualifiesForCertificate():
                 messagebox.showinfo('Result ', f'{learner.name} qualifies for a certificate.')
            else:
                 messagebox.showinfo('Result ', f'{learner.name} does not qualify for a certificate. ')
      else:
        messagebox.showinfo('Error', 'Learner not found')

#8. Exit
def exitProgram():
      confirm = messagebox.askyesno("Exit Confirmation", """Are you sure you want to exit the tracking system? 
                                    \n\n Note: All learner data will be lost because it is not saved in a database.""")
      return confirm

#STUDENT SUMMARY
def summary(learnerObject):
       
       print(f"{'-'*5} Learner Summary {'-'*5}")
       print(f"ID: {learnerObject.learnerId}")
       print(f"Name: {learnerObject.name}")
       print(f"Age: {learnerObject.age}")
       print(f"Course: {learnerObject.course}")
       print(f"Marks: {learnerObject.getMarks()}")
       print(f"Average: {learnerObject.average()}")
       print(f"Result: {learnerObject.performance()}")
       


#Search ID
def searchId(searchId):
      #loop through database to search for a match
      for learner in learnersDatabase:
           if learner.learnerId == searchId:
                return learner  # Returns the actual student object found
      return None  # Returns None if the ID doesn't exist
                
def recursiveTotalLearners(learners_list, index=0):
    # Base case: if the index matches the length of the list, stop
    if index >= len(learners_list):
        return 0
    # Recursive case: count 1 for the current student, then add the rest
    else:
        return 1 + recursiveTotalLearners(learners_list, index + 1)
         


if __name__ == "__main__":      
   main()

   


