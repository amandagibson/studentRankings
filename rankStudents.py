# Read the names and grades of at least 3 students.
# Rank the top 3 students with highest marks.
# Give cash rewards. $500 for first, $300 for second and $100 for third rank. These amounts cannot be modified.
# Appreciate students who scored 950 and above.
import operator


def readStudentDetails():
  print("Enter the number of students: ")
  numberOfStudents = int(input())
  studentRecord = {}
  for student in range(0, numberOfStudents):
    print("Enter the name of the student: ")
    name = input()
    print("Enter the grade of the student: ")
    grades = int(input())
    studentRecord[name] = grades
  return studentRecord


def rankStudents(studentRecord):
  sortedStudentRecord = sorted(
      studentRecord.items(), key=operator.itemgetter(1), reverse=True)
  print(sortedStudentRecord)
  print("{} has secured the highest grade with a score of {}!".format(
      sortedStudentRecord[0][0], sortedStudentRecord[0][1]))
  print("{} has secured the second highest grade with a score of {}!".format(
      sortedStudentRecord[1][0], sortedStudentRecord[1][1]))
  print("{} has secured the third highest grade with a score of {}!".format(
      sortedStudentRecord[2][0], sortedStudentRecord[2][1]))
  return sortedStudentRecord


def rewardStudents(sortedStudentRecord, reward):
  print("{} has received a cash reward of ${}".format(sortedStudentRecord[0][0], reward[0]))
  print("{} has received a cash reward of ${}".format(sortedStudentRecord[1][0], reward[1]))
  print("{} has received a cash reward of ${}".format(sortedStudentRecord[2][1], reward[2]))

def appreciateStudents():
  pass

studentRecord = readStudentDetails()
sortedStudentRecord = rankStudents(studentRecord)
reward = (500, 300, 100)
rewardStudents(sortedStudentRecord, reward)
