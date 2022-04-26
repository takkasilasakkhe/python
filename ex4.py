total_students=100
first_class=60
second_class=20
third_class=10
passed_students=first_class+second_class+third_class
failed_students=total_students-passed_students
average_passed_students=((first_class+second_class+third_class)/total_students)*100

#This code gives information regarding our classes information

print("total students",total_students,"in our class")
print("number of students",first_class,"passed in first class")
print("number of students",second_class,"passed in second class")
print("students passed",third_class,"in third class")
print("total students",passed_students,"passed in our class")
print("number of students",failed_students,"failed in our class")
print(average_passed_students ,"passed students")




