students = ["anu","abi","priya","madhu","sri"]
marks = [60,50,77,90,26]
dept = ["cse","it","ece","eee","mech"]

def student_result(marl):

      if mark >= 40:
        return "pass"
      else:
        return "fail"

for i in range(len(students)):
    print("Name:",students[i])
    print("Dept:",dept[i])
    print("Mark:",marks[i])
    print("---------------------")