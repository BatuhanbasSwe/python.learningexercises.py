
#print('hello world')
#print("there is a my brother's restaruant")
#pasta_name = 'spaghetti'
#pasta_amount = 5.9
#unit= 'kg'
#print(pasta_name)
#print(f"pasta amount is : {pasta_amount} {unit}" )
#print(type(pasta_name))
#print(type(pasta_amount))
# Type your code below

"""
a=5.2
b=2.6
c= a/b
# Don't change the line below
print(f" a = {a}, b = {b}, c = {c}");
"""
from sqlalchemy import result_tuple

#from importlib.metadata import pass_none

"""
# Type your code below
count = 0
count += 4
count *= 2
count -= 1
# Don't change the line below
print(f"count = {count}")
"""

"""
# Type your code below
n1 = 8
n2 =9
n3= n1 > n2


# Don't change the line below
print(f"n1 = {n1}, n2 = {n2}, n3 = {n3}")
"""


"""
#excellent example

# Type your code below
b1 = 2
b2 = 3
b3 = b1<2 or b2>2

# Don't change the line below
print(f"b3 = {b3}")
"""

"""
# Type your code below
b1 = -7
b2 = 5
b3 = not (b1 + b2) < (b1 * b2)

# Don't change the line below
print(f"b3 = {b3}")
"""
"""
# Type your code below
a=6
b=4

# Don't change the line below
c = b * a
print(f'c = {c}')
"""

"""
b1 = 10
b2 = 4
b3 = 6

# Don't change the line below
b4 = b1>b2  and b2<5 and (not b3>10)
print(f"b4 = {b4}")
"""


"""
#if,else statement--------------------------------------------------

#factorial  function
def recursive_factorial(n):
    if n==1 :
        return n
    else:
        return n * recursive_factorial(n-1)
number=int(input("Enter a positive integer:"))
if number <0:
    print(" please enter a positive integer")
elif number ==0:
    print("factorial of 0 is 1")
else:
    print("factorial of number" , number , "=",recursive_factorial(number))
    
"""

"""
a= 15
b= 13
# Don't change below this line
c = 0
if a >= b and not b < 10:
    c = 2

c += 1
print(f"c = {c}")
"""


"""
wind = int(input("Please enter a  wind violence: "))  # Don't change this line
status = "unset"
# Type your code below
if wind < 8:
    status = "Calm"
elif wind >= 8 and wind <= 31:
    status = "Breeze"
elif wind >= 32 and wind <= 63:
    status = "Gale"
else:
    status= "storm"

# Don't change the line below
print(f"status = {status}")
"""

"""
n1 = int(input("Enter first number")) # Don't change this line
n2 = int(input("Enter second number")) # Don't change this line
op = input("action you want to take (sub,div,multip,collection " ) # Don't change this line
result = 0

if op == '+':
    result = n1 + n2
elif op == '-':
    result = n1 - n2
elif op == '/':
    result =n1 / n2
else:
    result = n1 * n2

# Don't change the line below
print(f"result = {result}")
"""

#their_name=input()
#print(their_name)

#their_name=input("what is your name")
#print(f"Hello,{their_name},welcome to Python" )

"""
var1 = input("please enter first variable")
var2 = input("please enter second variable")
var1 = int(var1)
var2 = float(var2)
print(var1*var2)
"""

#age=input("how old are you")
#age=int(age)
#print(f" {120-age} years till 120")

"""
number=int(input("please enter a number"))
if number==1:
    print("T")
else:
    print("F")
"""

###FOR LOOPS------------------------------------------------------
"""
for i in range (3,28):
    print(f"hello coddy:{i}" )
i += 1
"""


"""
number=float(input("enter a number"))
while number >= 3.5:
    number=number/2
print(number)

"""
"""
for i in range(1, 11):
    if i==6:
        break
    print (i)
"""

"""
i=2
while i<=20:
    print(i)
    i=i+2
"""

"""
number=int(input("how many numbers do you want enter"))
result = 0
for i in range(number):
    a = int(input("enter a number"))
    result += a
print("result= " , result)
"""


"""
def sum_numbers():
    res=0
    for i in range (1,10001):
        res += i
    print(res)

n=int(input("enter a number"))
for i in range(n):
    sum_numbers()
"""


"""
#nice example
def calculate_product(a,b):
    product=a * b
    print(f"girilen {a} ve {b} sayılarının çarpımı: {product}")

print("Enter a values of product")
num1=float(input("Enter first number"))
num2=float(input("Enter second number"))

calculate_product(num1,num2)
"""
###################Listlere dair hersey----------------------------------
"""
fruit=["banana","apple","watermelon","melon","orange","pineapple"]
#print(fruit[2:5])  # baştaki 2 dahil , 5 dahil değil
#print(fruit[-3:-1]) # baştaki -3 yine dahil, -1 dahil değil
#if "banana" in fruit:
#    print("yes banana in the fruit ")
#if "cherry" in fruit:
#    print("yes cherry in the fruit ")
#else:
#    print("no cherry in the fruit ")

print(fruit)
fruit[4]="cherry"
print(fruit)
fruit[1:3]=["cherry","banana"] #karıştırma 1 ve 3. index değil 1dahil ve 3 arasındaki yani 1 v 2
print(fruit)
print(len(fruit))
fruit[1:4]=["cherrry"] # o aralık yerine sadece cherry koydu fazla da koyabilirdi
print(fruit)
print(len(fruit))

"""

###listelere veri ekleme ve kopyalama
"""
fruit=["banana","apple","watermelon","melon","orange","pineapple"]
fruit2=["cherry","apple"]

new_fruit=fruit+fruit2
print(new_fruit)
print(len(new_fruit))

new_fruit.append("peach")#append ekliyor
print(new_fruit)
print(len(new_fruit))

new_fruit.insert(1,"cherry")#insert ile yerine koyuyo ve kalanları kaydırıyo
print(new_fruit)
print(len(new_fruit))

new_fruit.extend(fruit)# extend ile genişletiyo
print(new_fruit)
print(len(new_fruit))
"""

"""
import copy

list1=[[1,2],[3,4]]
new_list=copy.deepcopy(list1)

new_list[0][0]=70
new_list[0][1]=19
new_list[1][1]=34

print(list1)
print(new_list)
"""

"""
fruit=["banana","apple","melon","orange","melon","watermelon","pineapple"]

fruit.remove("watermelon") #remove kaldırır ,birden fazla aynı değer varsa ilk gördüğünü kaldırır
last_item=fruit.pop(3) # öğeyi kaldırır ve kaldırdığı öğeyi yazdırır
print(last_item)
print(fruit)
#fruit.clear() #listenin içini siler
result=fruit.index("apple")
print(result)
result2=fruit.count("melon")
print(result2)
"""
"""
fruit=["banana","apple","melon","orange","melon","watermelon","pineapple"]
myNumbers=[10,70,29,34,19,7,45]

fruit.sort(key=str.lower) #alfabetik sıraya göre sıralar
myNumbers.sort(reverse=True)  #reverse=False küçükten büyüğe doğru sıralar
print(myNumbers)
print(fruit)
"""

####------------WHILE DONGUSU------------------------------

"""
i=1
while(i<=7):
    #print(i,"- python")  ##alt alta yazmak istersek böyle
    print(i,end="-python ") #yanyana yazmak istersek end yazarız
    i+=1
print("\n done")
"""


"""
i=1
while(i<=7):
    print(i,end="- ")
    if(i==4):
        break #break döngüyü kırıp döngüden çıkar
    i+=1
print("\n done")
"""


"""
i=0
while(i<=7):
    i+=1
    if(i==4):
        continue  #ben çalıştıktan sonra benden sonraki döngü komutlarını es geç başa dön direkt
    print(i, end="- ")
print("\n done") #çıktıda 4 yok
"""


"""
i=1
while(i<=7):
    print(i,end="- ")
    i += 1
else:
    print("\ni variable is no longer less than 7")
print("\n While loop is over")
"""


"""
#While Loop
myNumbers=[70,19,34,23,7]
i = 0
while(i<len (myNumbers)):
    print(myNumbers[i],end=" ")
    i+=1
"""

"""
i=70
while(i>0):
    print(i,end=" ")
    i-=5
"""

##---while döngusu uygulamaları--------
#sıralama algoritması
"""
myNumbers=[]
i=0
while(i<7):
    input_number=int(input("Enter an integer:"))
    myNumbers.append(input_number)
    i+=1
myNumbers.sort(reverse=False)
x=0
while(x<7):
    print(myNumbers[x],end=" ")
    x+=1
"""

"""
#tek çift sayıları yazdırma
start_number=int(input("Enter the start number:"))
end_number=int(input("Enter the ending number:"))

while(start_number<end_number):
    if(start_number%2 ==0):
        print(start_number,end=" ")
    start_number+=1
"""

"""
###isim girene kadar isim istiyor
while(True):
    name=input("Enter your name:"))
    if(name==""):
        continue
    else:
        break
print(f"your name is {name}")

"""

"""
result=1
i=1
number=int(input("Enter an integer:"))
while(i<=number):
    result*=i
    i+=1
print(f"{number}! ={result}")
"""

#######FOR DONGUSU ---------------------------------------
"""
fruits=["apple","banana","orange","melon","pineapple","cherry","grape"]
i=0
for fruit in fruits:
    print(i,".index=",fruit)
    i+=1
"""

"""
fruits=["apple","banana","orange","melon","pineapple","cherry","grape"]
for fruit in fruits:
    if(fruit=="orange"):
        #break #orange olduktan sonra durur
        continue #orange ı es geçer sonra yazmaya devam eder
    print(fruit)
"""
##for döngüsünde continue sayesinde tek çift yazdırma
"""
number=int(input("Enter an integer:"))
for item in range(number):
    if(item%2==1):
        continue
    print(item, end=" ")
else:
    print("For loop finished")

"""

"""
adjectives=["red","big","tasty"]
fruits=["grape","strawberry","cherry"]

for outer in adjectives:
    for inner in fruits:
        print(outer,inner)
"""


"""
myNumbers=[
    [70,"batuhan"],
    [34,"sudem"],
    [23,"ufo"]
    ]
for item1,item2 in myNumbers:
    print(f"{item1},numaralı öğrenci {item2}")
"""

##----------SAYI TAHMIN OYUNU-----------------------
"""
import random
random_number=random.randint(1,100) # 1 ile 100 arasında rasgele bir tam sayı üret
remaining_attempts=7 # 5 deneme hakkı atandı
score=100 # başlangıç puanı
attempt_count=0 # deneme sayısı
print("Guess a number between 1 and 100")
print(f"Your starting score: {score}")
while (remaining_attempts>0):
    guess=int(input("Your guess:"))
    if(guess<1 or guess>100):
        print("Please! Enter a number between 1 and 100")
        continue
        attempt_count += 1
    if(guess==random_number):
        print(f"Congratulations! You guessed the number correctly on your {attempt_count}.attempt")
        print(f"Your total score: {score}")
        break
    elif(guess<random_number):
        print("Try a larger number")
    else:
        print("Try a smaller number")
    remaining_attempts-=1
    score-=15
    if (remaining_attempts > 0):
        print(f"Remaining attempts: {remaining_attempts}")
        print(f"Current score: {score}")
    else:
        print("Unfortunately! You ran out of attempts!")
        print(f"Your total score: {score}")
print(f"Number was {random_number}")
"""
#####GİRİLEN SAYININ ASAL SAYI OLUP OLMADIĞINI BULMA
"""
input_number=int(input("Enter a number:"))
isPrime=True
if(input_number<0):
    print("Enter a positive number")
elif(input_number>0 and input_number<2):
    print(" the smallest prime number is 2 ")
else:
     for i in range(2,int(input_number**0.5)+1):
         if(input_number % i == 0):
             isPrime=False
             break
     if(isPrime):
        print(f"{input_number} is prime number")
     else:
        print(f"{input_number} is not a prime number")
"""


"""
####Girilen sayıya kadar olan tüm asal sayıları bulma
input_number=int(input("Enter a number:"))
prime_numbers=[]
if(input_number<0):
    print("Enter a positive number")
elif(input_number>0 and input_number<2):
    print(" the smallest prime number is 2 ")
else:
    prime_numbers.append(2)
    for i in range(3,input_number+1,2): ##tek sayılara baktırcaz sadece
        for j in range(3,int(i**0.5)+1):
            if(i %j==0):
                break
        else:
            prime_numbers.append(i)
    print(f"{prime_numbers}")
"""


"""
names=['ali','yağmur','hakan','deniz']
years=[1998,2000,1998,1987]

result = 'ali' in names
result=names.index('ali')


names.reverse()
#print(names)


names.sort()
#print(names)

names.sort(reverse=True)
#print(names)

years.sort()
#print(years)

str="chevrolet,dacia"

min=min(years)
max=max(years)
#print(min,max)

result=years.count(1998)
#print(result)
"""


#square = lambda num: num**2
#numbers=[1,3,5,9]
#result=list(map(square,numbers))
#print(result)

"""
numbers = [1,3,5,9,10,4]
def check_even(num):  return num%2==0
result=list(filter(check_even,numbers))
print(result)

#aynılar altaki ile üstteki

"""

"""
numbers = [1,3,5,9,10,4]
result=list(filter(lambda num: num%2==0 ,numbers))
print(result)

"""



"""
###BANK APPLICATION
accountA = {
    'name':'batuhan baş',
    'idno':'325236',
    'balance':3000,
    'creditmoney':2000
}

accountB = {
    'name':'ali turan',
    'idno':'9574987',
    'balance':2000,
    'creditmoney':1000
}

def withdrawmoney(account,amount):
    print(f"Hello {account['name']}")

    if account['balance']>=amount:
        print("you can withdraw money")
    else:
        total=account['balance'] + account['creditmoney']

        if(total>=amount):
            creditmoney=input("do you want to withdraw credit money? y/n")
            if creditmoney=="y":
                account['balance'] -= amount
                account['balance']=0
                account['creditmoney']-=amount
                print("you can withdraw money")
            else:
                print(f"you can not withdraw money from {account['idno']} no account your balance is {account['balance']}")

        else:
            print("sorry insufficient money ")

withdrawmoney(accountA,5000)
withdrawmoney(accountA,5000)

"""


"""
class Person:
    address='no information'

    #constructor(yapıcı method)
    def __init__(self,name,year):

        #object attributes
        self.name=name
        self.year=year

    #instance methods
    def intro(self):
        print(f"Hello there I am {self.name}")

    def calculateAge(self):
        return 2025-self.year

p1=Person(name='ali',year=1990)
p2=Person(name='sudem',year=1995)

p1.intro()
p2.intro()

print(f"My name is {p1.name} and I am {p1.calculateAge()} years old")
print(f"My name is {p2.name} and I am {p2.calculateAge()} years old")

"""


"""
class Circle:
    #class object attribute
    pi=3.14

    def __init__(self,radius=1):
        self.r=radius

    #methods
    def circumference(self):
        return 2*self.pi*self.r

    def area (self):
        return self.pi*(self.r**2)

c1=Circle() # r =1
c2=Circle(5)

print(f"c1: area ={c1.area()} circumference = {c1.circumference()}")
print(f"c2: area ={c2.area()} circumference = {c2.circumference()}")
"""


"""
#--------------------------INHERITANCE----------------------------------
class Person():
    def __init__(self,fname,lname):
        self.firstName=fname
        self.lastName=lname
        print("Person created thanks")

    def who_am_i(self):
        print(" i am a person")

    def eat(self):
        print(" i am eating")



class Student(Person):
    def __init__(self,fname,lname,number):
        #Person.__init__(self,fname,lname) #person init metodunu çalıştırır
        super().__init__(fname,lname) #super metodu kullanmak daha işlevli

        self.studentNumber=number
        print("Student created thanks")

    #override
    def who_am_i(self):
        print(" i am a student")

    def say_hello(self):
        print(" hello")

class Teacher(Person):
    def __init__(self,fname,lname,branch):
        #Person.__init__(self,fname,lname)
        super().__init__(fname,lname)

        print("Teacher created thanks")

        self.branch=branch

    def who_am_i(self):
        print(f" i am a {self.branch} teacher")




p1 = Person("ali","yılmaz")
s1 = Student("batuhan","baş",2309111036)
t1 = Teacher("serkan ","yılmaz","math")

t1.who_am_i()

print(f"firstName is {p1.firstName} and lastname is {p1.lastName}")
print(f"firstName is {s1.firstName} and lastname is {s1.lastName} my student number is {s1.studentNumber}  ")

s1.say_hello()
"""


"""
####------------demo-quiz-------------
class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer

    def checkAnswer(self,answer):
        return self.answer == answer

#QUIZ
class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question=self.getQuestion()
        print(f"Question  {self.questionIndex + 1} : {question.text} ")

        for q in question.choices:
            print('-' + q )

        answer = input("Answer:")

        is_correct =self.quess(answer)
        if is_correct:
            print("Correct")
        else:
            print(f"Incorrect the correct answer is {question.answer}")
        self.loadQuestion()

    def quess(self,answer):
        question=self.getQuestion()

        is_correct = question.checkAnswer(answer)

        if is_correct:
            self.score +=1

        self.questionIndex +=1
        return is_correct

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print(f"Your score is {self.score}")

    def displayProgress(self):
        totalQuestion=len(self.questions)
        questionNumber=self.questionIndex +1

        if questionNumber > totalQuestion:
            print("quiz  is over")
        else:
            print(f"question {questionNumber} of {totalQuestion}")

q1 = Question('what is the best program language ?' ,['C#' ,'python', 'javascript','java'],'python')
q2 = Question('most popular programing language ?' , ['C#' ,'python', 'javascript','java'],'python')
q3 = Question('most profitable programing language ?' ,['C#' ,'python', 'javascript','java'],'python')
questions = [q1, q2, q3]

quiz = Quiz(questions)

quiz.loadQuestion()
"""

####-----------------------programlamada moduller -------------

"""
###-------------math modulu-----------------------
from math import *       #import math yerine from math import * kullandığımız için aşağıda value = math.factorial gibi kullanmamıza gerek yok
                           #from math import factorial,sqrt,ceil gibi kullanabiliriz ama kullancağımız her şeyi belirtmemiz gerekir
#value=sqrt(49)   ## karekök alır
#value=factorial(5) ##factorial alır
#value=floor(5.9) ### sayıyı aşağı yuvarlar int yapar
#value=ceil(5.9)  ## sayıyı yukarı yuvarlar int yapar

print(value)
"""




##----------------random modulu------------------------

"""
#from random import *   #bunu kullanırsan başlarına random. getirmemize gerek kalmaz
import random

#result = random.random() # (0.0 ,1.0) arasında değer üretir
#result = random.uniform(10,100)  #verdiğimiz değer arasında değer üretir
#result = random.randint(10,100)  #verdiğimiz değer arasında integer değer üretir


names=['ali','yagmur','deniz','cenk']
result=names[random.randint(0,len(names)-1)]  #listenin içinden rastgele bir değer getirir
result=random.choice(names)
list=list(range(10))
random.shuffle(list)
result=list


list=range(100)
result=random.sample(list,3)
result=random.sample(names,2)
print(result)

"""


#------------------kendi ana modulumuzu oluşturup ordan bilgi çekme -------------------------
"""
import myfirstmoduleattempt

result=myfirstmoduleattempt.numbers
result=myfirstmoduleattempt.number
result=myfirstmoduleattempt.person["name"]
result=myfirstmoduleattempt.person["age"]
result=myfirstmoduleattempt.person["city"]
result=myfirstmoduleattempt.func(10)
p=myfirstmoduleattempt.Person()
p.speak()

print(result)
"""

###---------------------ERROR HANDLING HATA YONETIMI----------------------
"""
while True:
    try:
        x=int(input("x="))
        y=int(input("y="))
        print(x/y)
    except Exception as e:
        print("you entered invalid value",e)
    else:
        print("you entered valid value")
        break
    finally:
        print("Try exception block  terminated (sonlandı) ")

print("PROGRAM TERMINATED")
"""

#---------------------------RAISE EXCEPTION-------------------------------------

##yeni şifre oluşturma aracı

#def check_password(psw):
#    import re
#    if len(psw)<8:
#        raise Exception("Password must have at least 8 characters")
#    elif not re.search("[a-z]",psw):
#        raise Exception("Password must have at least one lowercase letter")
#    elif not re.search("[A-Z]",psw):
#        raise Exception("Password must have at least one uppercase letter")
#    elif not re.search("[0-9]",psw):
#        raise Exception("Password must have at least one number")
#    elif not re.search("[.,!,@,*]",psw):
#        raise Exception("Password must have at least one special character(.,!,#,@)")
#  elif re.search(r"\s",psw):
#        raise Exception("Password must does not contain spaces")

#while True:
#    password=input("enter new password")

#    try:
#        check_password(password)
#    except Exception as e:
#        print(e)

#   else:
#        print(" strong password approved !")
#        break

"""
list = ["1","2", "5a", "10b", "abc", "10","50"]
# 1: Liste elemanları içindeki sayısal değerleri bulunuz.
for x in list:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue
"""

"""
#kullanıcı 'q' değerini girmedikce aldığınız her inputun sayı olduğundan emın ol aksı halde hata mesajı yayınla
while True:
    number = input('number:')
    if number.lower() == 'q':
        break

    try:
        result=float(number)
        print(f"entered value is {result}")
    except ValueError:
        print("entered invalid value")
        continue
"""

"""
def checkPassword(password):
####   Girilen parola içerisinde türkçe karakter hatası veriniz
    turkish_characters='şçğöüıİ'

    for i in password:
        if i in turkish_characters:
            raise TypeError("password can't contain turkish characters")
        else:
            pass

    print(' valid password ')
password=input("password:")
try:
    checkPassword(password)
except TypeError as err:
    print(err)
"""

"""
def factorial(x):
    x=int(x)

    if x<0:
        raise ValueError("factorial can not be negative")
    result=1
    for i in range(1,x+1):
        result *= i
    return result

for x in [5,10,20,-3,'10a']:
    try:
        y=factorial(x)
    except ValueError as err:
        print(err)
        continue

    print(y)
"""

###-------------iç içe fonksiyonlar-------------------------------------------------
"""
def outer (num1):
    print("outer")
    def inner_increment(num1):
        print ("inner")
        return num1+1
    num2 = inner_increment(num1)
    print(num1,num2)
outer(10)
"""

"""
def factorial (number):
    if not isinstance(number,int):
        raise TypeError("factorial must be an integer")

    if not number >=0 :
        raise ValueError("factorial must be equal or greater than 0")


    def inner_factorial(number):
        if number <=1:
            return 1
        else:
            return number * inner_factorial(number-1)
    return inner_factorial(number)

try:
    input_str=input("please enter the number whose factorial you want to calculate: ")
    factorial_number=int(input_str)
    result = factorial(factorial_number)
    print(f"\nThe factorial of {factorial_number} is: {result}")
except ValueError as err:
    print(f"\n Error : Invalid input {err} please enter whole number ")
except (TypeError, Exception) as err:
    print(f"\nError in calculation: {err}")
"""

"""
def usalma(number):

    def inner(power):
        return number ** power
    return inner

two = usalma(2)
print(two(3))
"""


"""
def my_decorator(func):
    def wrapper(name):
        print("process before function")
        func(name)
        print("process after function")
    return wrapper


 
@my_decorator
def sayHello(name):
    print("hello",name)
sayHello("ali")
"""


"""

import math
import time

def calculate_time(func):
    def inner(*args, **kwargs):
        start=time.time()
        time.sleep(1)

        func(*args, **kwargs)
        finish=time.time()
        #print( func.__name__ ,"function took :",str(finish -start) + " seconds")
    return inner

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))

@calculate_time
def factorial (number):
    print(math.factorial(number))

@calculate_time
def multiplication (a,b):
    print(a*b)


usalma(2,3)
factorial(34)
multiplication(48,22)
"""


##--------------------------ITERATORS--------------------------------------------
list = [1,2,3,4,5]

iterator = iter(list)
#print(next(iterator))
#print(next(iterator))

"""
iterator = iter(list)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
"""

"""
class myNumbers:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop


    def __iter__(self):
        return self

    def __next__(self):
        if self.start<=self.stop:
            x=self.start
            self.start += 1
            return x
        else:
            raise StopIteration

list = myNumbers(20,50)
myiter = iter(list)

while True:
    try:
        print(next(myiter))
    except StopIteration:
        break

#for i in list
#   print (i)
"""

#--------------------------------GENERATORS------------------------------------------

"""
generator =(i**3 for i in range (5))
print(generator)

for i in generator:
    print(i)
"""



"""
def cube_generator_up_to(limit):
    current_number = 1
    while current_number <= limit:
        yield current_number ** 3
        current_number += 1

limit_str = input("Lütfen üst limit sayısını girin: ")

try:
    limit = int(limit_str)
except ValueError:
    print("Hatalı giriş. Lütfen tam sayı girin.")
    exit()

print(f"\n{limit}'e kadar olan sayıların küpleri:")

# Generator'ı kullan ve çıktıları yazdır
for result in cube_generator_up_to(limit):
    print(result)

"""


####----------------------------------DATETIME MODULU---------------------------------



"""
from datetime import datetime

now = datetime.now()

result=now.month
result=now.day
result=now.year


###----genel olarak HARFLERİ KÜÇÜK YAZARSAN KISALTMASINI YAZIYOR BÜYÜK Yazarsan tamamnı yazıyor
result=datetime.ctime(now) ## mon dec 15 18:16:34 2025 şeklinde yazar
result=datetime.strftime(now,"%y")   # 25 yazıyor 2025 in 25 i
result=datetime.strftime(now,"%Y")   #2025 yazıyor
result=datetime.strftime(now,"%X")  # saati yazıyor
result=datetime.strftime(now,"%A")  # günü yazıyor örn: monday
result=datetime.strftime(now,"%B")  # AY YAZIYOR örn: december
result=datetime.strftime(now,"%Y %B %A")



t = '14  October 2004 hour 12:12:30'
result =datetime.strptime(t,'%d %B %Y hour %H:%M:%S')
print(result)

"""


####-----------------------------OS MODULU-------------------------------------------

#import os
#import datetime


#------------------------------klasör oluşturma----------------------------------------
# os.mkdir("new directory deneme w os")  # yeni  klasör oluşturma
# os.makedirs("newdirectory/yeniklasor")
# os.rename("newdirectory","yeniklasör") # newdirectory dosyasının ismini yeni klasör olarak değiştirmek
# os.rmdir("newdirectory") #klasörü siler
# os.removedirs("yeniklasör/yeniklasör") #Belirttiğin yoldaki tüm boş üst klasörleri de temizleyerek geriye doğru gider.

#with open("data.txt", "w", encoding="utf-8") as file:
#   file.write("This is a new file created with Python.")

#
#-------------------------------dizin değiştirme---------------------------------------------------------
#os.chdir('..')  dosya konumu bir üst dizine geçer
#os.chdir('../..') dosya konumu iki üst dizine geçer


#-------------------------------listeleme---------------------------------------------

#result=os.listdir()
#result=os.listdir('C:\\')
#print(result)

#for file in os.listdir():
#    if file.endswith(".py"):  #.py ile biten dosyaları getir bu klasörde
#        print(file)


#--------------------------------etkin dizin öğrenme--------------------------------------
#result = os.getcwd() #olduğu dosya
#result = os.stat("deneme2.py")  # burdkai bilgileri anlamadığımız için datetime modulunu kullanıp aşağıda çözümlüyoruz
#result = result.st_size/1024  #kaç mb
#result = datetime.datetime.fromtimestamp(result.st_ctime) #oluşturulma tarihi
#result = datetime.datetime.fromtimestamp(result.st_atime) #son erişilme tarihi
#result = datetime.datetime.fromtimestamp(result.st_mtime)  #değiştirime tarihi

#os.system("notepad.exe")  #notepad uygulamasını açar

#------path
#result=os.path.abspath("deneme2.py")  #dosya yolunu verir
#result=os.path.dirname(r"C:\Users\Batuhan\PycharmProjects\denemee2\.venv\deneme2.py" )
#result=os.path.dirname(os.path.abspath("deneme2.py"))
#result = os.path.exists("deneme2.py")  #böyle bir dosya var mı test eder
#result = os.path.isfile(r"C:\Users\Batuhan\PycharmProjects\denemee2\.venv\deneme2.py")  ## bir dosya mı diye kontorl eder
#result = os.path.isdir(r"C:\Users\Batuhan\PycharmProjects") # klasör mü diye kontrol eder
#result = os.path.join("C:\\","denemee2.py","deneme1.py")  ##bu uzantıları birbirine birleştirir
#result = os.path.split(r"C:\\denemee2.py")   #bu uzantı birbirinden ayırır

#result = os.path.splitext("deneme2.py")  ## ismi ile uzantısını ayırır
#result= result[0]
#result=result[1]    #burda baktık gerçekten ikiye ayırmış mı

#print(result)










#---------------------------REGULAR ESPRESSION METHOD------------------------------------


import re

#result = dir(re)  #dir methodunu istediğimiz modulde kullanıp hangi metodlara sahip bakabiliyoruz aynı bu örnekteki gibidd
#print(result)

#str="python course : python program guide | 40 hours (saat)"

#re.findall()
#result =re.findall("python",str)  #python geçen yeri bulma
#result=len(result)

#re.split()
#result=re.split(" ",str) # boşluk boşluk böldük istersek : koyup mesela : dan sorasını bölerdik

#re.sub()
#result=re.sub(" ","-",str) #boşluk karakterlerini - ile değiştiriyoruz

#re.search()
#result=re.search("python",str) # python ifadesini bulduk 0-6 aralığında bulduğunu söylüyor

#result=result.span()
#result=result.start() #hangi karakterden başladığını söylüyor
#result=result.end() # hangi karakterde bittiğini söylüyor
#result=result.string #hangi string ifadenin içinde arıyor



#print(result)


#------regular expression----------------
#str="python course : python program guide | 40 hours (saat)"

"""
[] Köşeli parantezler arasına yazılan bütün karakterler aranır.
[abc] => a: 1 match
         ac : 2 match
        Python: No matches

[a-e] => [abcde]
[1-5] => [12345]
[0-39] => [01239]

[^abc] => abc dışındaki karakterler.
[^0,9] => rakam olmayan karakterler.

"""
#result=re.findall("[abc]",str)
#result=re.findall("[saat]",str)  ##bütün harfleri arar ve bulduklarını sırayla yazar örn: ['t', 's', 't', 'a', 's']
#result=re.findall("[a-e]",str) #a dan e ye kadar tüm karakterleri ara
#result=re.findall("[^abc]",str) #abc dışı tüm karakterleri bulduğu sırayla yazar


#---------------------------------------------------------------------------------------------------
"""
Her hangi bir tek karakteri belirtir.
    ..=>    a: No match
            ab : 1 match
            abc : 1 match
            abcd 2 matches
"""
#result=re.findall("...",str)
#result=re.findall("py..on",str)
#print(result)
#-----------------------------------------------------------------------
""""  
     ^- Belirtilen string karakterlerle başlıyor mu?
     ^a => a: 1 match
           abc : 1 match
           bac: no match
"""

#result=re.findall("^p",str)

#--------------------------------------------------------------------------------

"""
$ belirtilen karakterle bitiyor mu ?
a$ =>   a: 1 match
        lamba: 1 match
        python: no match
"""
#result=re.findall("s$",str)

#-------------------------------------------------------------------------------

"""
  *  Bir karakterin sıfır ya da daha fazla sayıda olmasını kontrol eder.
ma*n => mn: 1 match
        man : 1 match
        maaan : 1 match
        main:No match (a' nın arkasına n gelmiyor.)
"""
#result=re.findall("sa*t",str)

#--------------------------------------------------
"""
 +  Bir karakterin bir ya da daha fazla sayıda olmasını kontrol eder.
ma+n => mn: no match
        man : 1 match
        maaan : 1 match
        main:No match (a' nın arkasına n gelmiyor.)

"""
#result= re.findall("sa*t",str)
#--------------------------------------------------------------------

"""
 ?  Bir karakterin 0 yada 1 kez olmasını kontrol eder.
ma?n => mn: no match
        man : 1 match
        maaan : 1 match
        main:No match (a' nın arkasına n gelmiyor.)

"""
#result= re.findall("sa?t",str)

#------------------------------------------------------------------
"""
{} Karakter sayısını kontrol eder.
a1{2} => a karakterinin arkasına 1 karakteri 2 kez tekrarlamalı.
a1{2,3} => a karakterinin arkasına 1 karakteri en az 2 en fazla 3 kez
[0-9] {2,4} => en az 2 en çok 4 basamaklı sayılar.
"""
#result=re.findall("a{2,3}",str)
#result=re.findall("[0-9]{2}",str) #0-9 a kadar 2 basamaklı sayı
#------------------------------------------------------------------------------------------------

"""
    |  alternatif seçeneklerden birinin gerçekleşmesi gerekir.
    
        a|b => a or b
            cde => no match
            ade => 1 match
            acdbea => 3 match
"""
#result=re.findall("a|p",str)
#--------------------------------------------------------------------------------------
r"""
   \$ -Özel karakterleri aramamızı sağlar.
        \$a => $ karakterinin arkasına a karakterinin arar. 
            Yani $ regular exp. engine tarafından yorumlanmaz.
        
"""
#result=re.findall("$a",str)
#---------------------------------------------------------------------------------------------------
r"""
    \A -Belirtilen karakter string in başında mı ?
        \Athe => the string in başındamı
"""
#result=re.findall(r"\Apython",str)

#-------------------------------------------------------------------------------------------
r"""
    \Z -Belirtilen karakter string in sonunda mı ?
        the\Z => the string in sonunda mı
"""
#result=re.findall(r"saat \Z",str)

#-----------------------------------------------------------------------------------
r"""   
 #   \b -Belirtilen karakter kelimenin in başında ya da sonunda mı ?
    \bthe --> the kelimenin en başında mı
    the\b --> the kelimenin en sonunda mı
"""
#result=re.findall(r"thon\b",str)

 #---------------------------------------------------------
r"""
    \B - belirtiler karakter kelimenin en başında ya da sonunda değil mi ?
    \Bthe --> the kelimenin en başında değil mi ?
    the\B --> the kelimenin en sonunda değil mi ?
"""
#result=re.findall(r"\Bpyth","str")




#---------------------------------------------------------------------------

#
# \d{2} -> 2 digits (Day)
# -     -> literal hyphen
# \d{2} -> 2 digits (Month)
# -     -> literal hyphen
# \d{4} -> 4 digits (Year)

#result=re.findall(r"\d+",str)   #\d rakamları arar birden fazla bulmak için d+ kullandık

#result=re.findall(r"\D",str)    # rakam olmayanları arar ve yazar

#restored_string=" ".join(result)  ## liste yapısını bozduk
#resultnospace =restored_string.replace(" ","")  ##aradaki boşlukları kapattık
#print(resultnospace)

#------------------------------------------------------------------------------------------------------

# \s boşluk karakterlerini arar
# \S boşluk karakteri dışındakiler
# \w alfabetik karakterler,rakamlar ve alt çizgi karakteri
# \W   \w nin tam tersi


#print(result)




###----------------------------PYTHON JASON MODULE------------------------------------
import json


r"""
person_string = '{"name":"Ali" ,"languages": ["python","C#"] }'

person_dict = {"name": "Ali", "languages": ["Python","C#"] }

# JSON string to Dict--------
#result=json.loads(person_string)
#result["name"]
#result["languages"]


#with open ("person.json") as f:
#    data=json.load(f)
#    print(data["name"])
#    print(data["languages"])



# Dict to JSON string
#result = json.dumps(person_dict)
#print(result)
#print(type(result))

#json dosyasını yazdırma
#with open("person.json","w") as f:
#    json.dump(person_dict,f)


converted_dict = json.loads(person_string)
result=json.dumps(converted_dict, indent =4 , sort_keys=True)
print("dictionary",person_dict)
print("converted text",result)

"""



r"""
import os

class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email
class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        #load users from .json file
        self.loadUsers()
    def loadUsers(self):
        if os.path.exists("users.json"):
            with open ("users.json","r",encoding='utf-8') as f:
                users = json.load(f)
                for user in users:
                    user=json.loads(user)
                    newUser = User(username=user["username"],password=user["password"],email=user["email"])
                    print(user['username'])
                    self.users.append(newUser)
            print(self.users)


    def register(self,user:User):
        self.users.append(user)
        self.savetoFile()
        print(" Denied ! User account created")

    def login(self,username ,password):
        if self.isLoggedIn:
            print("you already logged in")
        else:
            for user in self.users:
                if user.username ==username and user.password ==password:
                    self.isLoggedIn = True
                    self.currentUser = user
                    print("logged in.")
                else:
                    print("wrong username or password.")
                    break


    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print(" Denied ! User account logged out")

    def identity(self):
        if self.isLoggedIn:
            print(f"{username}: logged in")
        else:
            print("not logged in")

    def savetoFile(self):
        list=[]
        for user in self.users:
            list.append(json.dumps(user.__dict__)) ##listeye çevirip öyle dumps ile beraber yolluyoruz
        with open ('users.json','w') as f:
            json.dump(list,f)

repository = UserRepository()

while True:
    print('MENU'.center(50,'*'))
    choice = input('1 -Register \n2- Login\n3- Logout\n4- Identity\n5-exit \nChoice...')
    if choice =='5':
        break
    else:
        if choice == '1':
            username=input('Username : ')
            password = input('Password : ')
            email =input('Email : ')

            user=User(username=username,password=password,email=email)
            repository.register(user)
            print(repository.users)

        elif choice == '2':
            if repository.isLoggedIn:
                print("you already logged in")
            else:
                username=input('Username : ')
                password = input('Password : ')
                repository.login(username,password)
        elif choice == '3':
            repository.logout()

        elif choice == '4':
            repository.identity()

        else:
            print('Invalid choice')
"""


#########------------------------------NUMPY--------------------------------------------------------

import numpy as np # np olarak kullanıcaz


r"""
py_list = [1,2,3,4,5,6,7,8,9,]

np_array = np.array([1,2,3,4,5,6,7,8,9,])

print(type(py_list))
print(type(np_array))

py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi =np_array.reshape(3,3)  #3-3 şeklinde tekrar çağır demek

print(py_multi)
print(np_multi)

print(np_array.ndim)   # 1 boyutlu
print(np_multi.ndim)  # 3 e 3 lük yani 2 boyutlu   .ndim boyutunu söylüyor

print(np_array.shape)
print(np_multi.shape)   #formunu söylüyor (3,3) gibi
"""


# --------NUMPY dizileri ile çalışma----------- numpy yerine np kullanıyoruz unutma


#result= np.arange(10,100,3) #10 ile 100 arasında 3 er 3 er yaz
#result=np.zeros(10) #10 tane 0
#result=np.ones(10)  #10 tane 1
#result=np.linspace(0,100,5)  #başlangıç ve bitiş dahil eşit aralıklara böler 0 25 ... 100
#result=np.random.randint(0,10) #0 ile 9 dahil rastgele bir sayı üretir
#result=np.random.randint(20) # 20 ye kadar rastgele sayı üretir
#result=np.random.randint(0,20,3)  #20 'ye kadar rastgele 3 sayı üretir

#print(result)


#np_array =np.arange(50)
#np_multi=np_array.reshape(5,10)  # 5 e 10 luk bir matris üretir
#print(np_multi.sum(axis=1))  #row sum
#print(np_multi.sum(axis=0))  #column sum


#rnd_numbers =np.random.randint(1,100,10)
#print(rnd_numbers)
#result=rnd_numbers.max() # max number
#result=rnd_numbers.min() #min number
#result=rnd_numbers.mean()  # average of generated numbers
#print(result)


#numbers = np.array([[0,5,10],[15,20,25],[50,75,85]])
#result=numbers[2]
#result=numbers[2,1]
#result=numbers[0,2]
#result=numbers[:,1] #tüm satırlardaki 2. eleman gelir
#result=numbers[:,0:2] #tüm satırlarda 2. index e kadar getirir
#result=numbers[:2,:2] #2.index satırına  kadar 2.sütun index e kadar getirir
#print(result)

#numbers1=np.random.randint(10,100,6)
#numbers2=np.random.randint(10,100,6)

#print(numbers1)
#print(numbers2)

#result=numbers1+numbers2
#result=numbers1 +10
#result=numbers1-numbers2
#result=numbers1*numbers2
#result=numbers1/numbers2

#result=np.sin(numbers1)
#result=np.sqrt(numbers1)
#result=np.log(numbers1) # ln üzerinden mesela ln74
#print(result)



### NUMPY UYGULAMA TEKRAR ETME EXERCISES-------------------------------------
r"""         

result = np.array([10,15,30,45,60])
result=np.arange(5,15)
result=np.arange(50,100,5)
result=np.zeros(10)
result=np.ones(10)
result=np.linspace(0,100,5)
result=np.random.randint(10,30,5)
result=np.random.randn(10) #rand metodu 0ile 1 arasında üretir -1 i de katmak istersek randn kullanırız
result=np.random.randint(10,50,15).reshape(3,5)  #3x5 boyutlarında 10-50 arasında rastgele matris


matris=np.random.randint(10,50,15).reshape(3,5)
rowTotal=matris.sum(axis=1)
columnTotal=matris.sum(axis=0)
print(matris)
#print(f"column total is  {columnTotal}")
#print(f"row total is  {rowTotal}")
result=matris.max() #matris max value
result=matris.min() #matris min value
result=matris.mean() # average of values
result=matris.argmax() #max value index
result=matris.argmin() #min value  aşağı doğru 5-6 diye devam ediyor
result=matris[0]  #ilk satırı yazdırma
result=matris[2:3] #2.satırı 3.sütunu yazdırma
result=matris[:,0] # tüm satırlarda ilk elemanı yazdırma
result=(matris**2) # tüm elemanlaırn karesini alma


matris2=np.random.randint(-50,50,15).reshape(3,5)
print(matris2)
result=(matris2 % 2 ==0) & (matris2 > 0 )  #-50 ile 50 arasında değerleri olan 3x5 lik matris üretip tek mi çift mi  ve pozitif mi diye baktık
print (result)




#arr =np.arange(10,20)
#print(arr)
#result= arr[0:3] #ilk 3 rakamı yazdırma
#result= arr[::-1] # tersten yazdırma
#print(result)

"""


#-----------------------------PANDAS------------------------------------------
#KAGGLE.COM
import pandas as pd

"""
numbers =[20,30,40,50]
letters =['a','b','c','d',20] #heterojen bilgi koyabiliyoruz sayı ve harf mesela
dict ={'a':10, 'b':20 ,'c':30 ,'d':40}
random_numbers=np.random.randint(10,100,6)

pandas_series = pd.Series(numbers)
#pandas_series = pd.Series(letters)
#pandas_series=pd.Series(5,[0,1,2,3])

pandas_series=pd.Series(numbers,['a','b','c','d'])
#pandas_series=pd.Series(dict)
#pandas_series =pd.Series(random_numbers)
#print((pandas_series))

result=pandas_series[:3]  # 3 e kaadar sayıları  getirir  pd.Series(numbers,['a','b','c','d'])bunla kullandığımız örnekte
result=pandas_series.ndim  #1 boyutlu
result=pandas_series.dtype
result=pandas_series.shape  #4 eleman
result=pandas_series.sum()  #sum
result=pandas_series.min() #min
result=pandas_series + 50  #elemanlara 50 eklenir
result=np.sqrt(pandas_series)  #karekök alır
result= pandas_series >= 40  # 40 ve 40dan büyük olanlar true
"""




#df =pd.DataFrame([1,2,3,4])
#df = pd.DataFrame([["Batuhan",50],["ali",60],["yağmur",70],["çınar",80]])
#print (df)

"""
list =[["Batuhan",50],["ali",60],["yağmur",70],["çınar",80]]
dict ={"Name": ["Batuhan","ali","yağmur","çınar"],"Grade":[50,60,70,80]}
df=pd.DataFrame(dict,index =["212","232","236","124"])
print(df)


dict_list=[
    {"Name":"Batuhan","Grade":50},
    {"Name":"Ali","Grade":60},
    {"Name":"yağmur","Grade":70},
    {"Name":"çınar","Grade":80}
]
df=pd.DataFrame(dict_list,index =["212","232","236","124"])
print(df)
"""


#s1 = pd.Series([3,2,0,1])
#s2 = pd.Series([0,3,7,2])
#data = dict(apples =s1, oranges =s2)
#df = pd.DataFrame(data)  ### df = dataframe unutma pd= pandas
#print(df)


#-----pandas ile  farklı dosya tiplerinden veri okuma

"""
import pandas as pd
from sqlalchemy import create_engine

user = "root"
password = "1967Batuhan44"
host = "localhost"
database = "node-app"

engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")

query = "SELECT * FROM USvideos"

try:
    df_sql = pd.read_sql_query(query, engine)
    print("MySQL'den veriler başarıyla çekildi:")
    print(df_sql.head())
except Exception as e:
    print(f"Hata: {e}")
"""


r"""
from numpy.random import randn
df=pd.DataFrame(randn(3,3),index=["A","B","C"],columns=["Column1","Column2","Column3"])
print (df)

result=df["Column1"]
result=type(df["Column1"])
result=df[["Column1","Column2"]]

#loc["row","column"] ==> loc["row"] ==>  loc[":","column"]
result=df.loc["A"]
result=type(df.loc["A"])
result=df.loc[:,"Column1"]
result=df.loc[:,["Column1","Column2"]]
result=df.loc[:,"Column1":"Column3"]   # köşeli parantez kullanmadım  ve araya , yerine : koydum aralığı aldı
result=df.loc[:,"" : "Column3"] # mesela ilk değeri boş bıraktık başlangıçdan 3. sütuna kadar gitti

result=df.loc["A":"B", "Column1":"Column2"]   # a ve b satırından column 2 ye kadar filtelerndi
result=df.loc[:"B", :"Column2"]# a yı kaldırdık b ye kadar dedik yine aynı çıktı geldi Column1 kaldırdık column2 ye kadar dedik
result=df.loc["C","Column2"]  #C satırından 2.sütun geldi
result=df.loc[["A","B"],["Column1","Column2"]]
#print(result)

df["Column4"] =pd.Series(randn(3),index=["A","B","C"])  #column 4 oluşturduk
df["Column5"] =df["Column1"] +df["Column2"]  # column1 ve column 2 topladık
#print(df)
print(df.drop("Column5",axis = 1)) # colum5 siler axis=1 diyerek soldan sağa lduğunu söylüyoruz
print(df)  #burda anlıyoruz ki orj dataframe (df) de bir değişiklik yapılmadı  aşağıda df den de silmek için göstericem

result =df.drop("Column5",axis = 1,inplace=True) #inplace=True sayesinde  sonuç orjinal df ye yazılır #inplace=false yaparsak kopyası çıkar yani 5.sütunlu olan

#axis=0 : Yukarıdan aşağıya hareket eder (Satırları/Index'i tarar).
# axis=1 : Soldan sağa hareket eder (Sütunları/Columns'u tarar).
"""


##-------------------------DATAFRAME FILTRELEME ---------------------------


import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data,index=["a","b","c","d","e","f","g","h","k","p","i","q","w","r","t"] ,columns = ["Column1","Column2","Column3","Column4","Column5"]) #index ve columnları hiç belirtmesek de olurdu
print(df)

#result=df.columns
result=df.head() #ilk 5 tane satır kayıt getirir
result=df.head(7)  #ilk 7 tane kayıt getirir
result=df.tail() #son 5 kayıt

result=df.tail(7)  #son 7 kayıt
result=df["Column1"].head()
result=df[["Column1","Column2"]].head() #seçili columnlarla getirme
result=df[5:15][["Column1","Column2"]].head(5)  # 5 v 10.kayıt arası

#print(result)


##----filtrelemeee--

result=df>50
result=df[df>50] #df içine alırsan değeri gösterir
result=df[df%2==0]
result=df[ (df["Column1"]>50) & (df["Column2"]<= 70) ] #filtreleme
result=df[ (df["Column1"]>50) | (df["Column2"]<= 70) ] #filtreleme
result=df.query("Column1>=50 & Column1 %2==0")
result=df.query("Column1>= 50 & Column1 %2 ==0")[["Column1","Column2"]]
result=df.query("Column1 >= 50 | Column1 %2 ==0")[["Column1","Column2"]]


#print(result)




r"""
#----------uygulamaa----IMDBMOVIES---
import pandas as pd
df=pd.read_csv("movie_data.csv")  #movide_data.csv dosyamızıı çektik

#1- Dosyada hakkındaki bilgiler.
result=df

#2-ilk 5 kaydı gösterin
result=df.head()

#3-ilk 10 kaydı gösterin
result=df.head(10)

#4-Son 5 kaydı gösterin
result=df.tail()

#5- Son 10 kaydı gösterin
result=df.tail(10)

#6- Sadece director_name kolonunu alın. ie_Ti
#result=df["director_name"]

#7- Sadece director_name kolonunu içeren ilk 5 kaydı alın.
#result=df["director_name"].head()

#8- Sadece director_name ve imdb_score kolonunu içeren ilk 5 kaydı alın.
result=df[["director_name","imdb_score"]].head()

#9- Sadece director_name ve imdb_score kolonunu içeren son 7 kaydı alın.
result=df[["director_name","imdb_score"]].tail(7)

#10- Sadece director_name ve imdb_score kolonunu içeren ikinci 5 kaydı alın.
result=df[5:10][["director_name","imdb_score"]].head()

#11- Sadece Movie_Title ve Rating kolonunu içeren ve imdb puanı 8.0
#ve üstünde olan kayıtlardan ilk 50 tanesini alınız
result=df[ df["imdb_score"] >=8.0 ]  [["director_name","imdb_score"]].head(50)

#12- Yayın tarihi 2014 ile 2015 arasında olan filmlerin isimlerini getiriniz.
result=df[ (df["title_year"]>= 2014) &  (df["title_year"]<=2015) ] [["director_name","title_year"]]

#13- duration (film süresi) 120  den büyük ya da imdb puanı 7.5 ile 8.5 arası
result= df[ (df["duration"] > 120)  | (df["imdb_score"]>=7.5) & (df["imdb_score"] <= 8.5)  ] [["director_name","imdb_score","duration"]]

print(result)

"""

#----DATAFRAME------GROUP BY--------------------
import numpy as np



employee = {
'employee': ['Ahmet Yılmaz', 'Can Ertürk', 'Hasan Korkmaz', 'Cenk Saymaz', 'Ali','Rıza erturk','Mustafa Can'],
'department': ['İnsan Kaynakları', 'Bilgi İşlem', 'Muhasebe', 'İnsan Kaynakları','Bilgi İşlem','Muhasebe','Bilgi İşlem'],
'age': [30,25, 45, 50, 23, 34,42],
'district': ['Kadıköy', 'Tuzla', 'Maltepe', 'Tuzla', 'Maltepe', 'Tuzla', 'Kadıköy'],
'salary': [5000, 3000, 4000, 3500, 2750,6500,4500]
}
df=pd.DataFrame(employee)
result=df
result=df["salary"].sum()

result=df.groupby("department").groups

result=df.groupby(["department","district"]).groups



#for name, group in df.groupby("district"):
#    print(name)
#    print(group)

#for name , group in df.groupby("department"):
#    print(name)
#    print(group)


result=df.groupby("district").get_group("Kadıköy") #kadıköyde oturanları görme
result=df.groupby("district").get_group("Maltepe")
result=df.groupby("department").get_group("Muhasebe") #muhasebe çalışanlarını görme
result=df.groupby("department").mean(numeric_only=True)  #departmanların maaş ve yaş ortalamaları
result=df.groupby("department")["salary"].mean(numeric_only=True)  # sadece maaş ortalaması
result=df.groupby("district")["age"].mean(numeric_only=True)  #kadıköyde yaşayanların yaş ortalaması
result=df.groupby("district")["employee"].count()  #semtlerde yaşayan insan sayıları
result=df.groupby("department")["age"].max() # en çok kaç yaşındalar
result=df.groupby("department")["salary"].min() # en az aldıkları maaş bölüme göre

result = df.groupby("department") [["age", "salary"]].agg("mean")
result = df.groupby("department") ["salary"].agg(["sum", "mean", "max", "min"])
result = df.groupby("department") ["salary"].agg(["sum", "mean", "max", "min"]).loc["Muhasebe"] #sadece muhasebe için filtreledik

#print(result)



##-------------PYTHON İLE KAYIP VE BOZUK VERİ ANALİZİ -----------------------------
#################
r"""

import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)
df =pd.DataFrame(data,index=['a','c','e','f','h'],columns=['column1','column2','column3'])

df= df.reindex(['a','b','c','d','e','f','g','h'])
df.loc['b','column1'] =50
newColumn=[np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["column4"]=newColumn
print(df)
#print(df)

#result=df.drop("column1",axis=1) #0 satır      1 sütun  #column1  sildik
#result=df.drop(["column1","column2"],axis=1) #column1 ve column2 yi sildik
#result=df.drop('a',axis=0) # a ssatırını sildik
#result=df.drop(['a','b','h'],axis=0) # a b h satırını sildik
#result = df.isnull() #değer içermeyenler NAN olanlar true değer içerenler false
#result=df.notnull() #tam tersi
#result=df.isnull().sum() #column toplamlarıre
result=df[ df["column1"].isnull() ]
result=df[ df["column1"].isnull()] ["column1" ]
#result=df[df["column1"].notnull()]["column1"]

result=df.dropna(axis=0)

result=df.dropna(axis=1)

result=df.dropna(how="any")

result=df.dropna(how="all") #içinde nan olan satırlar gelmez

result=df.dropna(subset =["column1","column2"],how="all") #ikisi birden boşsa sil biri bile doluysa getir
result=df.dropna(subset =["column1","column2"],how="any") #herhangi birisi ble boşsa getirme

result=df.dropna(thresh=2) # en az 2 tane değer benim için kabul

result=df.fillna(value='no value')  #NAN OLAN YERLERE OUTPUT YAZAR
result=df.sum() #sütun toplamı
result=df.sum().sum()  # tüm sütunların toplamı
result=df.size #32 değelrik yer var 8*4
result=df.isnull().sum() # NAN OLAN DEĞERLERİN SAYISI sütun sütun
result=df.isnull().sum().sum() # NAN OLAN DEĞERLERİN SAYISI TOPLAM
#print(result)



def average(df):
    sum =df.sum().sum()
    amount=df.size - df.isnull().sum().sum()
    return sum/amount


result=df.fillna(value=average(df))   ### NAN OLAN YERLERE ORTALAMA YAZDIRDIK
#print(result)

#print(f"average is {average(df)}")
"""


#-----------------------PANDAS AND STRING FUNCTIONS----------------------------------
r"""
import pandas as pd
data=pd.read_csv("movie_data.csv")
data=data.dropna() #NAN OLANLARI YAZMAZ

#data["director_name"] = data["director_name"].str.upper() #gelen datada director_name sütununu büyük yazdırdık
#data["director_name"] = data["director_name"].str.lower() # küçük harfe çevirir

#data["index"] =data["director_name"].str.find('a')  # a karakterini arar ve kaçıncı indexde bulduğunu söyler -1 olan index de geçmediğini görürüz
#data=data[data.director_name.str.contains('James')]  #director name james ile geçenleri bulur
#data=data.director_name.str.replace(' ','-') #boşluk yerine artık - işareti koyuyor
#data[['firstname','lastname']] =data['director_name'].loc[data['director_name'].str.split()]
data['director_name'].loc[data['director_name'].str.split().str.len()==2].str.split(expand=True)

print(data)

"""

# --------------------------PANDAS İLE JOIN AND MERGE------------------------------

"""
customers ={
    'CustomerId':[1,2,3,4],
    'FirstName' :["Ahmet","Ali","Hasan","Canan"],
    'LastName':["tan","kan","demir","öz"]
}
orders= {
    'OrderId': [10,11,12,13],
    'CustomerId':[1,2,5,7],
    'OrderDate':['2020-01-10','2020-01-11','2020-01-12','2020-01-13'  ]
}
df_customers=pd.DataFrame(customers,columns=['CustomerId','FirstName','LastName'])
df_orders=pd.DataFrame(orders,columns=['OrderId','CustomerId','OrderDate'])

print(df_customers)
print(df_orders)

result=pd.merge(df_customers,df_orders,how='inner')  #siparişi olan müşterileri getirdik
result=pd.merge(df_customers,df_orders,how='left')  #bütün müşteriler gelsin siparişi olmayanlar dahil
result=pd.merge(df_customers,df_orders,how='right')  #tüm siparişler geldi isimler yoksa NAN GELDİ VERİTABANINDA YOK MİSALİ

print(result)
"""


"""
CustomersA ={
    'CustomerId':[1,2,3,4],
    'FirstName' :["Ahmet","Ali","Hasan","Canan"],
    'LastName':["tan","kan","demir","öz"]
}

CustomersB ={
    'CustomerId':[5,6,7,8],
    'FirstName' :["yağmur","cınar","cengız","batu"],
    'LastName':["top","balta","kök","atın"]
}

df_customersA = pd.DataFrame(CustomersA,columns=['CustomerId','FirstName','LastName'])
df_customersB = pd.DataFrame(CustomersB,columns=['CustomerId','FirstName','LastName'])
result=pd.concat([df_customersA,df_customersB] ) #iki dataframe i birleştirdik
result=pd.concat([df_customersA,df_customersB], axis=1) #column bazlı birleştirdik
print(result)
"""

#----------------------------------PANDAS ILE DATAFRAME METHODS------------------------------------------


import pandas as pd
import numpy as np

data ={
    "Column1":[1,2,3,4,5],
    "Column2":[10,20,12,45,25],
    "Column3":["abc","acb","bca","cab","bac"]
}
df=pd.DataFrame(data)

def square(x):
    return x*x

result=df
result=df["Column2"].unique() #sadece column2 geldi yanyana index no suz
print(result)
result=df["Column2"].nunique()  #5 tane

result=df["Column2"].value_counts() #değerlerin kaç tane olduğunu söyler
result=df["Column2"] *2
result=df["Column2"].apply(square) #fonksiyonu çağırdık
df["Column4"] = df["Column3"].apply(len)
result = df.columns
result = len(df.columns)

result = df.index
result = len(df.index)

result=df.info #bilgi verir satır ve sütun detaylarını
result=df.sort_values("Column2")  #değerleri sıralayarak atar
result=df.sort_values("Column2",ascending=True)
#print(result)

data ={
"Month": ["Mayıs", "Haziran", "Nisan", "Mayıs", "Haziran", "Nisan"],
"Category": ["Elektronik", "Elektronik", "Elektronik", "Kitap","Elektronik","Kitap"],
"Income": [20, 30, 15, 14, 35, 42]
}
df=pd.DataFrame(data)
print(df)
df=df.pivot_table(index='Month',columns='Category',values='Income')
print(df)



#---------------------------------EXERCISE NBA PLAYERS---------------------------
r"""

df=pd.read_csv("all_seasons.csv")


# 1- İlk 10 kaydı getiriniz.
result=df.head(10)

# 2- Toplam kaç kayıt vardır ?
result=len(df.index)

# 3- Tüm oyuncuların toplam yaş ortalaması nedir ?
result=df["age"].mean()

# 4- En yüksek yaş nedir ?
result=df["age"].max()

#5- En  yaşlı oyuncu kimdir ?
result=df[ df["age"]==df["age"].max() ] ["player_name"].iloc[0]

# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takım nedir
result=df[ (df["age"] >=20) & (df["age"] <=25)]   [["player_name","team_abbreviation"]] .head(50)

#7- "George Zidek" isimli oyuncunun oynadığı takım hangisidir ?
result= df[ (df["player_name"]== "George Zidek") ]   ["team_abbreviation"]

# 8- Takımlara göre oyuncuların ortalama yaş bilgisi nedir ?
result=df.groupby("team_abbreviation") ["age"].mean()


# 9- Kaç farklı takım mevcut ?
result=len(df.groupby("team_abbreviation"))

result=len(df["team_abbreviation"].unique())


# 10- Her takımda kaç oyuncu oynamaktadır ?
result= df["team_abbreviation"].value_counts()

# 11- İsmi içinde "and" geçen kayıtları bulunuz.
df=df.dropna()   #NAN ALANLARI ÇIKARTTIK
result=df[ df["player_name"].str.contains("and") ]

#def str_find(player_name):                       #İKİ YÖNTEMLE YAPTIK AŞAĞINDAKİNDE DAHA FAZLA GELDİ ÇÜNKÜ BÜYÜK KÜÇÜK FARKI YOK
#    if "and" in player_name.lower():
#        return True
#    return False
#result=df[ df["player_name"].apply(str_find) ]

#print(result)
"""



#-----------------------EXERCISE YOUTUBE STATISTIC DATAS ANALYZ--------------------------------------
"""

import pandas as pd
df=pd.read_csv("USvideos.csv")

#1- İlk 10 kaydı getiriniz.
result=df.head(10)

#2- İkinci 5 kaydı getiriniz.
result=df[5:10].head

#3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.
result=df.columns

result=len(df.columns)

#4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyin
result=df.drop(["video_id","title"],axis=1).head(10)
#print(result.to_string()) #.to_string() ile tüm columnları görebiliyoruz

#5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz
result=df["likes"].mean()
result=df["dislikes"].mean()

#6- ilk 50 videonun like ve dislike kolonlarını getiriniz.
result=df.head(50) [["title","likes","dislikes"]]

#7- En çok görüntülenen video hangisidir ?
result=df["views"].max()  # en çok kaç izlendiği
result=df[ df["views"].max()==df["views"] ]  [["title","likes","dislikes"]]

# 8- En çok dislike alan  video hangisidir?
result=df[ df["dislikes"].max()==df["dislikes"] ] [["title","likes","dislikes"]]

# 9- En fazla görüntülenen ilk 10 video hangisidir ?
result=df.sort_values(by="views",ascending=False).head(10) [["title","views"]]

# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.
result=df.groupby("category_id")["likes"].mean().sort_values(ascending=False)

#11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.
result=df.groupby("category_id")["comment_count"].sum().sort_values(ascending=False)

# 12- Her kategoride kaç video vardır ?
result=df["category_id"].value_counts()


# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
df["title_len"] =df["title"].apply(len)
result=df

# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.

#df["tag_count"] =df["tags"]    #böyle tag leri görebiliriz
#df=result

df["tag_count"] =df["tags"].apply(lambda x: len(x.split('|')))   #böyle de sayabiliriz
df=result

def tagCount(tag):
    return len(tag.split('|'))
df["tag_count"] = df["tags"].apply(tagCount)
df=result
#print(result)





#15- En popüler videoları listeleyiniz. (like/dislike oranına göre)


def likedratio(dataset):

    likeList = dataset["likes"].tolist()
    dislikeList = dataset["dislikes"].tolist()

    liste = [item for item in zip(likeList, dislikeList)]

    ratiolist =[]
    for like,dislike in liste:
        if (like+dislike)==0:
            ratiolist.append(0)
        else:
            ratiolist.append(like/(like+dislike))

    return ratiolist


df["like ratio"] = likedratio(df)

result1=df.sort_values("like ratio", ascending=False).head(50)[["title", "likes", "dislikes"]]
#print(result1)

"""

#--------------------------------MATPLOTLIB---------------------------------------,
import matplotlib.pyplot as plt
import numpy as np
#matplotlib.org işe yarar

"""
x = [1,2,3,4]
y = [1,4,9,16]

#plt.plot(x,y,color="red",linewidth="5")  # renk ve kalınlık ayarladık
plt.plot(x,y,"o--r")  # o marker  -- kesikli çizgi
plt.axis([0,6,0,20]) # x min değeri ,x max değeri, y min değeri , y max değeri

plt.title("Graphic title")  # grafik başlığı
plt.xlabel("x label")   # x ekseni adı
plt.ylabel("y label")   # y ekseni adı

plt.show()
"""

"""
x=np.linspace(0,2,100)
plt.plot(x,x,label="linear",color="blue")
plt.plot(x,x**2,label="quadratic",color="red")
plt.plot(x,x**3,label="cubic",color="green")

plt.xlabel("x label")
plt.ylabel("y label")

plt.legend() # çubuklar ne anlama  geliyo  sol üstte gözüksün
plt.show()
"""

"""
x=np.linspace(0,2,100)
fig,axs=plt.subplots(3)

axs[0].plot(x,x,color="blue")
axs[0].set_title("linear")

axs[1].plot(x,x**2,color="red")  ## 3 tane alt alta grafik yapma
axs[1].set_title("quadratic")

axs[2].plot(x,x**3,color="green")
axs[2].set_title("cubic")

plt.tight_layout() #başlıklar birbirine giriyodu
plt.show()
"""

"""
x=np.linspace(0,2,100)
fig,axs=plt.subplots(2,2)
fig.suptitle("Graphic title")

axs[0,0].plot(x,x,color="blue")
axs[0,1].plot(x,x**2,color="red")
axs[1,0].plot(x,x**3,color="green")
axs[1,1].plot(x,x**4,color="yellow")

plt.show()

"""


"""
import pandas as pd
df = pd.read_csv("all_seasons.csv")

df=df.drop(["player_name"], axis=1).groupby("college").mean(numeric_only=True)
df.plot(subplots=True  , figsize=(10,20))

plt.legend(loc='best')
plt.show()
"""



"""
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("all_seasons.csv")

features_to_analyze = ["pts","reb","ast","net_rating"]

df_grouped = df.groupby("college")[features_to_analyze].mean(numeric_only=True)

df_sorted = df_grouped.sort_values(by="pts" , ascending=False).head(50)

df_sorted.plot(kind="bar" ,subplots=True, figsize=(10,20))

plt.tight_layout()
plt.show()
"""



"""
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10,9,20)
y = x ** 3
z= x **2

figure = plt.figure()

axes_cube= figure.add_axes([0.1,0.1,0.9,0.9]) #soldan sağa doğru , alttan yukarı doğru ,genişlik(büyüklük) ,yükseklik

axes_cube.plot(x,y,'b')
axes_cube.set_xlabel("x label")
axes_cube.set_ylabel("y label")
axes_cube.set_title("Cube graphic")

axes_square = figure.add_axes([0.15,0.6,0.2,0.3])
axes_square.plot(x,z,'r')
axes_square.set_xlabel("x label")
axes_square.set_ylabel("y label")
axes_square.set_title("square graphic")

plt.show()
"""

"""
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-10,10,20)
y=x **3
z= x **2

figure =plt.figure()
axes =figure.add_axes([0,0,1,1])

axes.plot(x,z,label ="square")
axes.plot(x,y,label="cube")
axes.legend(loc=1) # 1-2-3-4 diyerek yerini değiştiriyoruz
plt.show()
"""

"""

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-10,10,20)
y=x **3
z= x **2
fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(4,4))
axes[0].plot(x,y)
axes[0].set_title("cube")
axes[1].plot(x,z)
axes[1].set_title("square")

plt.tight_layout()
fig.savefig("figure1.png") # grafiği png olarak kaydeder pdf olarak bile kaydedebiliriz

plt.show()
"""


"""
import matplotlib.pyplot as plt
year =[2011,2012,2013,2014,2015]

player1=[5,7,8,10,2]
player2=[7,12,5,15,21]
player3=[18,20,22,25,19]

plt.plot([],[],color="y",label="player1")
plt.plot([],[],color="b",label="player2")
plt.plot([],[],color="g",label="player3")

plt.stackplot(year,player1,player2,player3)   #stackplot artıra artıra devam eder
plt.title("scores by years")

plt.xlabel("year")
plt.ylabel("score")

plt.legend()
plt.show()
"""


"""
import matplotlib.pyplot as plt

goal_types =['penalty','freekick','corner']
goals=[45,12,36]

colors=['y','r','b']

plt.pie(goals,labels=goal_types,colors=colors,shadow=True,explode=(0.05,0.05,0.05),autopct="%1.1f%%")  #autopct pastanın sütünde yüzde kaç oldugunu yazdırır

plt.show()
"""


"""
## BAR GRAFİĞİ
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,60,70,80,20],label="BMW",width=0.3,color="blue")
plt.bar([0.75,1.75,2.75,2.25,2.55],[50,60,70,80,20],label="AUDI",width=0.3,color="red")

plt.legend()
plt.xlabel("day")
plt.ylabel("distance(km)")
plt.title("car label")
plt.show()
"""



"""
##----hıstogram grafik-------

ages= [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,29]
age_groups = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(ages,age_groups,histtype="bar",rwidth=0.8,color="blue")
plt.xlabel("age")
plt.ylabel("number of people")

plt.title("HISTOGRAM graphic")

plt.show()
"""


r"""
import matplotlib.pyplot as plt
import numpy as np

# 1. Veri Hazırlama (NumPy kullanarak)
x = np.linspace(0, 10, 20) # 0 ile 10 arası 20 nokta
y1 = x ** 2               # Kare fonksiyonu
y2 = x ** 2.2             # Kıyaslama için farklı bir eğri

# 2. Tuval ve Grafik Alanı Oluşturma
fig, ax = plt.subplots(figsize=(10, 6))

# 3. Grafik Çizimi ve Parametrelerin Kullanımı
# 'color': Renk (İsim, Hex kod veya RGB verilebilir)
# 'alpha': Şeffaflık (0 tamamen şeffaf, 1 tamamen opak)
# 'marker': Veri noktalarının şekli
# 'linestyle': Çizginin stili
ax.plot(x, y1,
        color='red',          # Renk tanımlama
        alpha=0.4,            # %40 şeffaflık (Alttaki çizgiler görünsün diye)
        marker='o',           # Yuvarlak noktalar
        markersize=8,         # Nokta büyüklüğü
        linestyle='--',       # Kesikli çizgi
        linewidth=2,          # Çizgi kalınlığı
        label='Transparent Red Line')

ax.plot(x, y2,
        color='#2ECC71',      # Hex kod ile yeşil renk
        alpha=0.9,            # %90 opak (Daha belirgin)
        marker='s',           # Kare (square) noktalar
        linestyle='-',        # Düz çizgi
        label='Solid Green Line')

# 4. Detaylı Ayarlar
ax.set_title("Color and Transparency (Alpha) Demo", fontsize=15)
ax.set_xlabel("X Axis (Time/Distance)")
ax.set_ylabel("Y Axis (Value)")

# Izgara (Grid) ekleme - Şeffaflık burada da kullanılabilir
ax.grid(True, linestyle=':', alpha=0.5)

# Gösterge (Legend) ekleme
ax.legend()

plt.show()
"""


#-------------------------------SELENIUM-------GITHUB---------------------------------------
"""

from selenium import webdriver
import time
#chromedriver.exe i dosyaya ekledik
driver = webdriver.Chrome()
url="https://www.imdb.com/?ref_=chttvtp_nv_home"
driver.get(url)
print(driver.title)

time.sleep(2)
driver.maximize_window() #açılan sayfayı tam ekran yapar
driver.save_screenshot("fromimdb.png") # ss alır

url="https://www.imdb.com/chart/toptv/?ref_=hm_nv_menu"
driver.get(url)
#if "Top 250 TV shows " in driver.title:
    #driver.save_screenshot("Top 250 TV shows ")
print(driver.title)

time.sleep(2)

#driver.forward #sonraki sayfaya gider
driver.back() # önceki sayfaya gider

driver.close()

"""


"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # nokta , space , enter gibi tuşları import ettik
from selenium.webdriver.common.by import By # Yeni eklememiz gereken kütüphane
import time

driver = webdriver.Chrome()

url="https://www.imdb.com/chart/toptv/?ref_=hm_nv_menu"
driver.get(url)

searchInput=driver.find_element(By.NAME,"q")
time.sleep(2)
searchInput.send_keys("breaking bad")
time.sleep(2)
searchInput.send_keys(Keys.ENTER) #yazdıktan sonra enter a basıp arıyor
time.sleep(5)
result=driver.find_elements(By.CSS_SELECTOR,".ipc-metadata-list-summary-item__t")
for element in result:
    print(element.text)

driver.quit()
"""



"""
#----------------------------GITHUB--------------------------------
from githubUserInfo import username, password
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)
        self.browser.find_element(By.XPATH, "//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element(By.XPATH, "//*[@id='password']").send_keys(self.password)
        time.sleep(1)
        self.browser.find_element(By.XPATH, "//input[@name='commit']").click()
        time.sleep(2)

    def getFollowers(self):
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        time.sleep(2)


        followers = self.browser.find_elements(By.CSS_SELECTOR, ".d-table-cell.col-9.v-align-top.pr-3 h3 a")

        print(f"\n--- Toplam {len(followers)} Takipçi Bulundu ---")

        for index, follower in enumerate(followers):
            print(f"{index + 1}. {follower.text}")


github = Github(username, password)
github.signIn()
github.getFollowers()
"""



###---------------------------SELENIUM INSTAGRAM BOT--------first 12-------------------------

r"""

from instagraminfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Instagram:
    def __init__(self, username, password):
        self.options = webdriver.ChromeOptions()

        self.options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})

        # Eğer chromedriver.exe projenin içindeyse bu en sade yoldur
        self.browser = webdriver.Chrome(options=self.options)

        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        self.browser.find_element(By.NAME, "username").send_keys(self.username)
        self.browser.find_element(By.NAME, "password").send_keys(self.password + Keys.ENTER)
        time.sleep(5)

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}/")
        time.sleep(5)

        try:
            # Takipçi linkini bul ve tıkla
            self.browser.find_element(By.XPATH, "//a[contains(@href, 'followers')]").click()
            time.sleep(5)
        except Exception as e:
            print("Takipçi linki bulunamadı.")
            return


        try:

            modal = self.browser.find_element(By.CSS_SELECTOR, "div[role='dialog'] ._aano")
            last_height = self.browser.execute_script("return arguments[0].scrollHeight", modal)

            while True:
                self.browser.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", modal)
                time.sleep(2)
                new_height = self.browser.execute_script("return arguments[0].scrollHeight", modal)
                if new_height == last_height:
                    break
                last_height = new_height
        except:
            pass

        # Takipçileri listele
        followers = self.browser.find_elements(By.CSS_SELECTOR, "div[role='dialog'] span a")
        print(f"\n--- Toplam {len(followers)} Takipçi ---")

        for user in followers:
            name = user.text
            if name:
                print(f"Kullanıcı: {name}")

    def followUser(self, target_username):
        self.browser.get("https://www.instagram.com/" + target_username + "/")
        time.sleep(5)
        try:
            followButton = self.browser.find_element(By.TAG_NAME, "button")
            followButton.click()
            print(f"{target_username} takibe alındı.")
        except:
            print("Buton bulunamadı.")

    def unfollowUser(self, target_username):
        self.browser.get("https://www.instagram.com/" + target_username + "/")
        time.sleep(3)
        followButton = self.browser.find_element(By.TAG_NAME, "button")
        if followButton.text =="Following":
            followButton.click()
            time.sleep(3)
            confirmButton = self.browser.find_element(By.XPATH,"//button[text()='Unfollow']")
            confirmButton.click()
        else:
            print("You already dont follow")


# --- Başlat ---
instagram = Instagram(username, password)
instagram.signIn()
#instagram.getFollowers()  # Takipçileri çekmek için
#instagram.followUser("lvbelc5") # Takip etmek için
instagram.unfollowUser("lvbelc5")

input("\nKapatmak için Enter'a bas...")
"""

####-----------------------------EXERCISE---------------------------------------------

r"""
import pandas as pd

data = {
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard'],
    'Price': [1200, 25, 300, 80],
    'Quantity': [15, 8, 12, 5]
}
df = pd.DataFrame(data)

# 1. Filter products where Quantity > 10
filtered_df = df[ df['Quantity'] >10 ].copy()
# 2. Create a new column 'Total_Revenue'
filtered_df['Total_Revenue'] = filtered_df['Price'] * filtered_df['Quantity']

print(filtered_df)


# Yukarıdaki filtered_df sonucunu kullanarak; X ekseninde ürün isimleri, Y ekseninde ise 'Total_Revenue'
# olacak şekilde bir Bar Chart (Sütun Grafiği) çizdiren kodu yaz. Grafiğin başlığı "Revenue Analysis" olmalı.

colors=["red","black"]
plt.bar(filtered_df["Product"], filtered_df["Total_Revenue"],color=colors,label="Revenue")
plt.title("Revenue Analysis")
plt.legend()
plt.show()

"""


"""
days = [1,2,3,4,5]
temps =[23,25,26,35,21]

plt.plot(days,temps,color="red",marker="o",linestyle="--",label="temperature of days")


plt.title("Temperature of days")
plt.xlabel("days")
plt.ylabel("temperature")

plt.legend()
plt.show()
"""



"""
df = pd.read_csv("movie_data.csv")
result=df
#result=df['director_name']
result["duration"] =result["duration"].fillna("0")  ##duration da ki NA ları 0 yaptık

print (result)

"""


#df["stock"]=df["stock"].fillna("-1") #-1 koyup doldurma
#df=df.dropna(subset=["price"])  #direkt kaldırma



#txt = f"The price is {95:.2f} dollars"
#print(txt)


# os modeline bak 1290 lı satırlar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
df=pd.read_csv("ev_charge_logs.csv")
df["Energy_Delivered;Kwh"]=pd.to_numeric( df["Energy_Delivered_Kwh"],errors="coerce" )

median_energy = df["Energy_Delivered;Kwh"].median()
df["Energy_Delivered;Kwh"]=df["Energy_Delivered;Kwh"].fillna(median_energy)
"""

#energy_by_vehicle = df.groupby("vehicle_type")



















