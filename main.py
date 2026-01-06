student_name = input("Enter full name")
score = int(input("Enter test score"))


#taking iputs
age= int(input("what is your age?"))
print (age + 2)


#conditional statement
#once 1 condition is found true it doesnt check the rest of the conditions so it depens on the order

if age > 10:
    print ("you pay 200 lek")
elif age >20 :
    print("500 lek")
else:
    print("enter free")

#FIRST EXERSISE
student_name = input("Enter full name")
score = int(input("Enter test score"))
if score < 0 or score > 100 :
   print("invalid score number, score between 0-100")
elif score >50:
   print("you have passed")
else:
   print("you have failed")

if score <= 0 or score >= 100 :
   print()
elif score >=90:
   print("your grade is A")
elif score >=80:
   print("your grade is B")
elif score >=70:
   print("your grade is C")
elif score >=60:
   print("your grade is D")
elif score >=50:
   print("your grade is E")
else: 
   print("your grade is F")

#SECOND EXERSISE
#I know it's like either it should be evenly divisible by 4 and not evenly divisible by 100 or evenly divisible by 400. 
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    print ( year , "is a leap year")
elif year < 0 :
    print ("invalid year")
else:
    print( year , "is not a leap year")

#THIRD EXERSISE
salary =float(input("enter salary"))
if 0<= salary <= 1000:
   tax_rate = 0.2
elif 1001 <= salary < 2500:
   tax_rate = 0.15
elif salary >= 2501:
   tax_rate = 0.1
else:
