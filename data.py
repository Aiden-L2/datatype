""" x = 5
y = float(5)
print(x,y) """

""" values = [1,2,4,6,8,10,15,20]
print(values)
for i in values:
    print(i)
    print(values[0])
    print(values[6])
    print(values[7]) """

""" #integer
x=7
#string
name = "Aiden"
#name.upper()
#boolean
isvalid=True
#float
bill = 56.87

students = ["kevin, aiden, william"]
students.append("kevin")
print(students[1])
for student in students:
    if student == "kevin":
        print(f'gamble {student}')

#string
y = input("money?")
z = y + 5 """

""" x = "I need money"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" x = input("hello star")
y = len(x.split())
print(y) """

""" day_of_week = input("what day is today")
if day_of_week == "Thursday":
    print("correct")
elif day_of_week == "thursday":
    print("correct")
else:
    print("Nope") """

""" x = "test"
print(f"hello {x}")
 """

""" temp = 68
if temp >68:
    print('HOT')
elif temp == 68:
    print('warm')
else:
    print('cold') """

""" number = int(input("give me a number"))
print(number)
if number % 2 == 1:
    print("odd")
elif number % 2 == 0:
    print("even") """

""" bill = float(input("How much is the bill?"))
tip = input("How was the servic?")
if tip == "bad":
    print(float(bill) * 1.05)
elif tip == "okay":
    print(float(bill) * 1.1)
elif tip == "good":
    print(float(bill) * 1.15)
elif tip == "Perfect":
    print(float(bill) * 1.2) """

""" def spaces(n,y,t):
    n = input("twoto")
n = 5
y = [".",".","c","c","."]
t = ["c","c",".","c","."]
O = 0
for i in range(n):
    if y[i] == t[i] and y[i] == "c":
        O = O + 1
print("there are", str(O), "spaces") """

""" def find_factor(num):
    factors = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    return factors

print(find_factor(36)) """

def find_factor(num):
    factors = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    return factors

print(find_factor(36))
print(find_factor(12))

def GCF():


