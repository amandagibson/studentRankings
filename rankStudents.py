import operator

def readStudentDetails():
  print()
  print("Enter the number of students: ")
  numberOfStudents = int(input())
  studentRecord = {}
  for student in range(0, numberOfStudents):
    print("Enter the name of the student: ")
    name = input()
    print("Enter the grade of the student: ")
    grades = int(input())
    studentRecord[name] = grades
    print()
  return studentRecord


def rankStudents(studentRecord):
  print()
  sortedStudentRecord = sorted(
      studentRecord.items(), key=operator.itemgetter(1), reverse=True)
  print(sortedStudentRecord)
  print("{} has secured the highest grade with a score of {}!".format(
      sortedStudentRecord[0][0], sortedStudentRecord[0][1]))
  print("{} has secured the second highest grade with a score of {}!".format(
      sortedStudentRecord[1][0], sortedStudentRecord[1][1]))
  print("{} has secured the third highest grade with a score of {}!".format(
      sortedStudentRecord[2][0], sortedStudentRecord[2][1]))
  print()
  return sortedStudentRecord


def rewardStudents(sortedStudentRecord, reward):
  print()
  print("{} has received a cash reward of ${}".format(sortedStudentRecord[0][0], reward[0]))
  print("{} has received a cash reward of ${}".format(sortedStudentRecord[1][0], reward[1]))
  print("{} has received a cash reward of ${}".format(sortedStudentRecord[2][0], reward[2]))
  print()

def appreciateStudents(sortedStudentRecord):
  print()
  for record in sortedStudentRecord:
    if record[1] >= 950:
      print("Congratulations on scoring {} marks, {}!".format(record[1], record[0]))
    else:
      break
  print()

studentRecord = readStudentDetails()
sortedStudentRecord = rankStudents(studentRecord)
reward = (500, 300, 100)
rewardStudents(sortedStudentRecord, reward)
appreciateStudents(sortedStudentRecord)