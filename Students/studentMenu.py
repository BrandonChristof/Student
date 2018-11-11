'''
    Brandon Christof
    Binary Search Tree for Students
    Date created: 2018-11-09
    Last modified: 2018-11-11
'''

import BuildTree
import copy

dataList = []
newData = []
localTree = None;

#Student objects require a name, and number
class Student():
    def __init__(self, name, number):
        self.name = name
        self.number = number

#Reads in the file students.txt into dataList
def readData():
    global dataList

    dataFile = open("students.txt")
    with open('students.txt') as f:
        dataList = f.readlines()
    dataList = [x.strip() for x in dataList]
    f.close()


#Writes all new data into students.txt
def writeData():
    global localTree
    global newData
    
    localTree.orderList();
    newData = BuildTree.ordered;
    
    dataFile = open("students.txt", "w")
    for i in range(1, len(newData)):
        dataFile.write("\n" + newData[i].number + " " + newData[i].name)
    dataFile.close()   


#Builds a binary search tree using students in students.txt
def buildTree():
    global dataList
    global localTree

    root = Student("-", "0")
    localTree = BuildTree.Tree(root, None, None)
    
    for i in range(1, len(dataList)):
        name, num = dataList[i].partition(' ')[2], dataList[i].partition(' ')[0]
        addStudent = Student(name, num)
        localTree.addElement(addStudent)


#Adds a new student to binary tree if the new student number isn't already in use
def addStudent():
    global localTree
    privateTree = copy.deepcopy(localTree)
    
    studName = input("\nEnter new Student Name:")
    studNumber = input("Enter new Student Number:")

    newStudent = Student(studName, studNumber)
    if privateTree.searchElement(newStudent.number) != None:
        print("\n    Sorry, that number is already in use.")
    else:
        localTree.addElement(newStudent)
        print("\n    Successfully Added.")
    menu("")


#Takes a student number, and deletes it from the tree
def deleteStudent():
    userInput = input("\nEnter Student Number you wish to Delete:")
    localTree.deleteElement(userInput)
    print("\n    Deleted")
    menu("")


#Takes a student number, searches tree and outputs the student number and name
def searchStudent():
    privateTree = copy.deepcopy(localTree)
    userInput = input("\nEnter Student Number you wish to Search:")
    verdict = privateTree.searchElement(userInput)
    if verdict != None:
        print("\n    " + verdict.number + " " + verdict.name)
    else:
        print("\n    No results found")
    menu("");


#Decides what to do based on user input
def userDecision(d):
    if d == "A" or d == "a": addStudent()
    elif d == "D" or d == "d": deleteStudent()
    elif d == "S" or d == "s": searchStudent()
    elif d == "Q" or d == "q": writeData();
    else: menu("\n    Invalid entry. Please try again.\n")


#Prompts the user for input
def menu(s):
    print(s)
    print("[A]dd new Student\n[D]elete Student\n[S]earch Student\n[Q]uit");
    userInput = input("\nEnter:");
    userDecision(userInput)

def main():
    menu("\n    Welcome! What would you like to do?\n")
    

readData()
buildTree()
main()
