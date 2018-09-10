#This program is designed to check the arithmetic skills of a mathematics teacher applying a teaching position in a Ibrahim Adeyemo primary school
import random
name = input("Welcome to smart checker, please enter your name: ")
print("\t Hey",name + "!\n",
      "\t I heard you're the smartest in town,\n",
      "\t let's test your arithmetic skills")
print('The answer to your division should only be to the nearest whole number')
for i in range (1):
    a = random.randint(1,12)
    b = random.randint(1,12)
    d = random.randint(1,12)
    e = random.randint(1,12)
    f = random.randint(1,12)
    score = 0
#The program asks for multiplication
    print("\t", a, "x", b, "=")
    c = eval(input("\t answer: "))
    if  c == a * b:
        print("\t CORRECT!!!\n",
              "\t Here's another one for you\n",
              "\t Loading...\n",
              "\t")
        score = score + 1
    else:
        print("\t WRONG!!!\n",
              "\t The right answer is", a * b,"\n",
              "\t Here's another one, STAY FOCUSED\n",
              "\t Loading...\n",
              "\t")
#The program asks for addition
    print('\t', a,'+', b, '=')
    d = eval(input('\t answer: '))
    if d == a + b:
       print('\t CORRECT!!!\n',
             '\t Here is another one for you\n',
             '\t Loading...\n',
             '\t')
       score = score + 1
    else:
        print('\t WRONG!!!\n',
              '\t The right answer is', a + b,'\n',
              '\t Here is another one, STAY FOCUSED\n',
              '\t Loading...\n',
              '\t')
#The program asks for a subtraction
    print('\t', a,'-', b, '=')
    e = eval(input('\t answer: '))
    if e == a - b:
        print('\t CORRECT!!!\n',
              '\t Here is another one for you\n',
              '\t Loading...\n',
              '\t')
        score = score + 1
    else:
         print('\t WRONG!!!\n',
               '\t The right answer is', a - b,'\n',
               '\t Here is another one, STAY FOCUSED\n',
               '\t Loading...\n',
               '\t')
#The program asks for a division
    print('\t', a,'//', b, '=')
    f = eval(input('\t answer: '))
    if f == a // b:
        print('\t CORRECT!!!\n',
              '\t Here is another one for you\n',
              '\t Loading...\n',
              '\t')
        score = score + 1
    else:
         print('\t WRONG!!!\n',
               '\t The right answer is', a // b,'\n',
               '\t Here is another one, STAY FOCUSED\n',
               '\t Loading...\n',)
    a = random.randint(1,15)
    b = random.randint(1,15)
    d = random.randint(1,15)
    e = random.randint(1,15)
    f = random.randint(1,15)
    print("\t", a, "x", b, "=")
    c = eval(input("\t answer: "))
    if  c == a * b:
        print("\t CORRECT!!!\n",
              "\t Here's another one for you\n",
              "\t Loading...\n",
              "\t")
        score = score + 1
    else:
        print("\t WRONG!!!\n",
              "\t The right answer is", a * b,"\n",
              "\t Here's another one, STAY FOCUSED\n",
              "\t Loading...\n",
              "\t")
#The program asks for addition
    print('\t', a,'+', b, '=')
    d = eval(input('\t answer: '))
    if d == a + b:
       print('\t CORRECT!!!\n',
             '\t Here is another one for you\n',
             '\t Loading...\n',
             '\t')
       score = score + 1
    else:
        print('\t WRONG!!!\n',
              '\t The right answer is', a + b,'\n',
              '\t Here is another one, STAY FOCUSED\n',
              '\t Loading...\n',
              '\t')
#The program asks for a subtraction
    print('\t', a,'-', b, '=')
    e = eval(input('\t answer: '))
    if e == a - b:
        print('\t CORRECT!!!\n',
              '\t Here is another one for you\n',
              '\t Loading...\n',
              '\t')
        score = score + 1
    else:
         print('\t WRONG!!!\n',
               '\t The right answer is', a - b,'\n',
               '\t Here is another one, STAY FOCUSED\n',
               '\t Loading...\n',
               '\t')
#The program asks for a division
    print('\t', a,'//', b, '=')
    f = eval(input('\t answer: '))
    if f == a // b:
        print('\t CORRECT!!!\n',
              '\t Here is another one for you\n',
              '\t Loading...\n',
              '\t')
        score = score + 1
    else:
         print('\t WRONG!!!\n',
               '\t The right answer is', a // b,'\n',
               '\t Here is another one, STAY FOCUSED\n',
               '\t Loading...\n',)
    a = random.randint(1,18)
    b = random.randint(1,18)
    d = random.randint(1,18)
    e = random.randint(1,18)
    f = random.randint(1,18)
    print("\t", a, "x", b, "=")
    c = eval(input("\t answer: "))
    if  c == a * b:
        print("\t CORRECT!!!\n",
              "\t Here's another one for you\n",
              "\t Loading...\n",
              "\t")
        score = score + 1
    else:
        print("\t WRONG!!!\n",
              "\t The right answer is", a * b,"\n",
              "\t Here's another one, STAY FOCUSED\n",
              "\t Loading...\n",
              "\t")
#The program asks for addition
    print('\t', a,'+', b, '=')
    d = eval(input('\t answer: '))
    if d == a + b:
       print('\t CORRECT!!!\n',
             '\t Here is another one for you\n',
             '\t Loading...\n',
             '\t')
       score = score + 1
    else:
        print('\t WRONG!!!\n',
              '\t The right answer is', a + b,'\n',
              '\t Here is another one, STAY FOCUSED\n',
              '\t Loading...\n',
              '\t')
#The program asks for a subtraction
    print('\t', a,'-', b, '=')
    e = eval(input('\t answer: '))
    if e == a - b:
        print('\t CORRECT!!!\n',
              '\t Here is another one for you\n',
              '\t Loading...\n',
              '\t')
        score = score + 1
    else:
         print('\t WRONG!!!\n',
               '\t The right answer is', a - b,'\n',
               '\t Here is another one, STAY FOCUSED\n',
               '\t Loading...\n',
               '\t')
#The program asks for a division
    print('\t', a,'//', b, '=')
    f = eval(input('\t answer: '))
    if f == a // b:
        print('\t CORRECT!!!\n',
              '\t Here is another one for you\n',
              '\t Loading...\n',
              '\t')
        score = score + 1
    else:
         print('\t WRONG!!!\n',
               '\t The right answer is', a // b,'\n',
               '\t Here is another one, STAY FOCUSED\n',
               '\t Loading...\n',)
    a = random.randint(1,20)
    b = random.randint(1,20)
    d = random.randint(1,20)
    e = random.randint(1,20)
    f = random.randint(1,20)
    print("\t", a, "x", b, "=")
    c = eval(input("\t answer: "))
    if  c == a * b:
        print("\t CORRECT!!!\n",
              "\t Here's another one for you\n",
              "\t Loading...\n",
              "\t")
        score = score + 1
    else:
        print("\t WRONG!!!\n",
              "\t The right answer is", a * b,"\n",
              "\t Here's another one, STAY FOCUSED\n",
              "\t Loading...\n",
              "\t")
#The program asks for addition
    print('\t', a,'+', b, '=')
    d = eval(input('\t answer: '))
    if d == a + b:
       print('\t CORRECT!!!\n',
             '\t Here is another one for you\n',
             '\t Loading...\n',
             '\t')
       score = score + 1
    else:
        print('\t WRONG!!!\n',
              '\t The right answer is', a + b,'\n',
              '\t Here is another one, STAY FOCUSED\n',
              '\t Loading...\n',
              '\t')
#The program asks for a subtraction
    print('\t', a,'-', b, '=')
    e = eval(input('\t answer: '))
    if e == a - b:
        print('\t CORRECT!!!\n',
              '\t Here is another one for you\n',
              '\t Loading...\n',
              '\t')
        score = score + 1
    else:
         print('\t WRONG!!!\n',
               '\t The right answer is', a - b,'\n',
               '\t Here is another one, STAY FOCUSED\n',
               '\t Loading...\n',
               '\t')
#The program asks for a division
    print('\t', a,'//', b, '=')
    f = eval(input('\t answer: '))
    if f == a // b:
        print('\t CORRECT!!!\n',
              '\t Here is another one for you\n',
              '\t Loading...\n',
              '\t')
        score = score + 1
    else:
         print('\t WRONG!!!\n',
               '\t The right answer is', a // b,'\n',
               '\t Here is another one, STAY FOCUSED\n',
               '\t Loading...\n',)
    a = random.randint(1,22)
    b = random.randint(1,22)
    d = random.randint(1,22)
    e = random.randint(1,22)
    f = random.randint(1,22)
    print("\t", a, "x", b, "=")
    c = eval(input("\t answer: "))
    if  c == a * b:
        print("\t CORRECT!!!\n",
              "\t Here's another one for you\n",
              "\t Loading...\n",
              "\t")
        score = score + 1
    else:
        print("\t WRONG!!!\n",
              "\t The right answer is", a * b,"\n",
              "\t Here's another one, STAY FOCUSED\n",
              "\t Loading...\n",
              "\t")
#The program asks for addition
    print('\t', a,'+', b, '=')
    d = eval(input('\t answer: '))
    if d == a + b:
       print('\t CORRECT!!!\n',
             '\t Here is another one for you\n',
             '\t Loading...\n',
             '\t')
       score = score + 1
    else:
        print('\t WRONG!!!\n',
              '\t The right answer is', a + b,'\n',
              '\t Here is another one, STAY FOCUSED\n',
              '\t Loading...\n',
              '\t')
#The program asks for a subtraction
    print('\t', a,'-', b, '=')
    e = eval(input('\t answer: '))
    if e == a - b:
        print('\t CORRECT!!!\n',
              '\t Here is another one for you\n',
              '\t Loading...\n',
              '\t')
        score = score + 1
    else:
         print('\t WRONG!!!\n',
               '\t The right answer is', a - b,'\n',
               '\t Here is another one, STAY FOCUSED\n',
               '\t Loading...\n',
               '\t')
#The program asks for a division
    print('\t', a,'//', b, '=')
    f = eval(input('\t answer: '))
    if f == a // b:
        print('\t CORRECT!!!\n',
              '\t Here is another one for you\n',
              '\t Loading...\n',
              '\t')
        score = score + 1
    else:
         print('\t WRONG!!!\n',
               '\t The right answer is', a // b,'\n',
               '\t Here is another one, STAY FOCUSED\n',
               '\t Loading...\n',)
    a = random.randint(1,24)
    b = random.randint(1,24)
    d = random.randint(1,24)
    e = random.randint(1,24)
    f = random.randint(1,24)
    print("\t", a, "x", b, "=")
    c = eval(input("\t answer: "))
    if  c == a * b:
        print("\t CORRECT!!!\n",
              "\t Here's another one for you\n",
              "\t Loading...\n",
              "\t")
        score = score + 1
    else:
        print("\t WRONG!!!\n",
              "\t The right answer is", a * b,"\n",
              "\t Here's another one, STAY FOCUSED\n",
              "\t Loading...\n",
              "\t")
#The program asks for addition
    print('\t', a,'+', b, '=')
    d = eval(input('\t answer: '))
    if d == a + b:
       print('\t CORRECT!!!\n',
             '\t Here is another one for you\n',
             '\t Loading...\n',
             '\t')
       score = score + 1
    else:
        print('\t WRONG!!!\n',
              '\t The right answer is', a + b,'\n',
              '\t Here is another one, STAY FOCUSED\n',
              '\t Loading...\n',
              '\t')
#The program asks for a subtraction
    print('\t', a,'-', b, '=')
    e = eval(input('\t answer: '))
    if e == a - b:
        print('\t CORRECT!!!\n',
              '\t Here is another one for you\n',
              '\t Loading...\n',
              '\t')
        score = score + 1
    else:
         print('\t WRONG!!!\n',
               '\t The right answer is', a - b,'\n',
               '\t Here is another one, STAY FOCUSED\n',
               '\t Loading...\n',
               '\t')
#The program asks for a division
    print('\t', a,'//', b, '=')
    f = eval(input('\t answer: '))
    if f == a // b:
        print('\t CORRECT!!!\n',
              '\t Here is another one for you\n',
              '\t Loading...\n',
              '\t')
        score = score + 1
    else:
         print('\t WRONG!!!\n',
               '\t Here is another one, STAY FOCUSED\n',
               '\t Loading...\n',)
    a = random.randint(4,26)
    b = random.randint(4,26)
    d = random.randint(4,26)
    e = random.randint(4,26)
    f = random.randint(4,26)
    print("\t", a, "x", b, "=")
    c = eval(input("\t answer: "))
    if  c == a * b:
        print("\t CORRECT!!!\n",
              "\t Here's another one for you\n",
              "\t Loading...\n",
              "\t")
        score = score + 1
    else:
        print("\t WRONG!!!\n",
              "\t The right answer is", a * b,"\n",
              "\t Here's another one, STAY FOCUSED\n",
              "\t Loading...\n",
              "\t")
#The program asks for addition
    print('\t', a,'+', b, '=')
    d = eval(input('\t answer: '))
    if d == a + b:
       print('\t CORRECT!!!\n',
             '\t Here is another one for you\n',
             '\t Loading...\n',
             '\t')
       score = score + 1
    else:
        print('\t WRONG!!!\n',
              '\t The right answer is', a + b,'\n',
              '\t Here is another one, STAY FOCUSED\n',
              '\t Loading...\n',
              '\t')
#The program asks for a subtraction
    print('\t', a,'-', b, '=')
    e = eval(input('\t answer: '))
    if e == a - b:
        print('\t CORRECT!!!\n',
              '\t Here is another one for you\n',
              '\t Loading...\n',
              '\t')
        score = score + 1
    else:
         print('\t WRONG!!!\n',
               '\t The right answer is', a - b,'\n',
               '\t Here is another one, STAY FOCUSED\n',
               '\t Loading...\n',
               '\t')
#The program asks for a division
    print('\t', a,'//', b, '=')
    f = eval(input('\t answer: '))
    if f == a // b:
        print('\t CORRECT!!!\n',
              '\t Here is another one for you\n',
              '\t Loading...\n',
              '\t')
        score = score + 1
    else:
         print('\t WRONG!!!\n',
               '\t The right answer is', a // b,'\n',
               '\t Here is another one, STAY FOCUSED\n',
               '\t Loading...\n',)
    a = random.randint(5,28)
    b = random.randint(5,28)
    d = random.randint(5,28)
    e = random.randint(5,28)
    f = random.randint(5,28)
    print("\t", a, "x", b, "=")
    c = eval(input("\t answer: "))
    if  c == a * b:
        print("\t CORRECT!!!\n",
              "\t Here's another one for you\n",
              "\t Loading...\n",
              "\t")
        score = score + 1
    else:
        print("\t WRONG!!!\n",
              "\t The right answer is", a * b,"\n",
              "\t Here's another one, STAY FOCUSED\n",
              "\t Loading...\n",
              "\t")
#The program asks for addition
    print('\t', a,'+', b, '=')
    d = eval(input('\t answer: '))
    if d == a + b:
       print('\t CORRECT!!!\n',
             '\t Here is another one for you\n',
             '\t Loading...\n',
             '\t')
       score = score + 1
    else:
        print('\t WRONG!!!\n',
              '\t The right answer is', a + b,'\n',
              '\t Here is another one, STAY FOCUSED\n',
              '\t Loading...\n',
              '\t')
#The program asks for a subtraction
    print('\t', a,'-', b, '=')
    e = eval(input('\t answer: '))
    if e == a - b:
        print('\t CORRECT!!!\n',
              '\t Here is another one for you\n',
              '\t Loading...\n',
              '\t')
        score = score + 1
    else:
         print('\t WRONG!!!\n',
               '\t The right answer is', a - b,'\n',
               '\t Here is another one, STAY FOCUSED\n',
               '\t Loading...\n',
               '\t')
#The program asks for a division
    print('\t', a,'//', b, '=')
    f = eval(input('\t answer: '))
    if f == a // b:
        print('\t CORRECT!!!\n',
              '\t Here is another one for you\n',
              '\t Loading...\n',
              '\t')
        score = score + 1
    else:
         print('\t WRONG!!!\n',
               '\t The right answer is', a // b,'\n',
               '\t Here is another one, STAY FOCUSED\n',
               '\t Loading...\n',)
    a = random.randint(6,30)
    b = random.randint(6,30)
    d = random.randint(6,30)
    e = random.randint(6,30)
    f = random.randint(6,30)
    print("\t", a, "x", b, "=")
    c = eval(input("\t answer: "))
    if  c == a * b:
        print("\t CORRECT!!!\n",
              "\t Here's another one for you\n",
              "\t Loading...\n",
              "\t")
        score = score + 1
    else:
        print("\t WRONG!!!\n",
              "\t The right answer is", a * b,"\n",
              "\t Here's another one, STAY FOCUSED\n",
              "\t Loading...\n",
              "\t")
#The program asks for addition
    print('\t', a,'+', b, '=')
    d = eval(input('\t answer: '))
    if d == a + b:
       print('\t CORRECT!!!\n',
             '\t Here is another one for you\n',
             '\t Loading...\n',
             '\t')
       score = score + 1
    else:
        print('\t WRONG!!!\n',
              '\t The right answer is', a + b,'\n',
              '\t Here is another one, STAY FOCUSED\n',
              '\t Loading...\n',
              '\t')
#The program asks for a subtraction
    print('\t', a,'-', b, '=')
    e = eval(input('\t answer: '))
    if e == a - b:
        print('\t CORRECT!!!\n',
              '\t Here is another one for you\n',
              '\t Loading...\n',
              '\t')
        score = score + 1
    else:
         print('\t WRONG!!!\n',
               '\t The right answer is', a - b,'\n',
               '\t Here is another one, STAY FOCUSED\n',
               '\t Loading...\n',
               '\t')
#The program asks for a division
    print('\t', a,'//', b, '=')
    f = eval(input('\t answer: '))
    if f == a // b:
        print('\t CORRECT!!!\n',
              '\t Here is another one for you\n',
              '\t Loading...\n',
              '\t')
        score = score + 1
    else:
         print('\t WRONG!!!\n',
               '\t The right answer is', a // b,'\n',
               '\t Here is another one, STAY FOCUSED\n',
               '\t Loading...\n',)
    a = random.randint(8,30)
    b = random.randint(8,30)
    d = random.randint(8,30)
    e = random.randint(8,30)
    f = random.randint(8,30)
    print("\t", a, "x", b, "=")
    c = eval(input("\t answer: "))
    if  c == a * b:
        print("\t CORRECT!!!\n",
              "\t Here's another one for you\n",
              "\t Loading...\n",
              "\t")
        score = score + 1
    else:
        print("\t WRONG!!!\n",
              "\t The right answer is", a * b,"\n",
              "\t Here's another one, STAY FOCUSED\n",
              "\t Loading...\n",
              "\t")
#The program asks for addition
    print('\t', a,'+', b, '=')
    d = eval(input('\t answer: '))
    if d == a + b:
       print('\t CORRECT!!!\n',
             '\t Here is another one for you\n',
             '\t Loading...\n',
             '\t')
       score = score + 1
    else:
        print('\t WRONG!!!\n',
              '\t The right answer is', a + b,'\n',
              '\t Here is another one, STAY FOCUSED\n',
              '\t Loading...\n',
              '\t')
#The program asks for a subtraction
    print('\t', a,'-', b, '=')
    e = eval(input('\t answer: '))
    if e == a - b:
        print('\t CORRECT!!!\n',
              '\t Here is another one for you\n',
              '\t Loading...\n',
              '\t')
        score = score + 1
    else:
         print('\t WRONG!!!\n',
               '\t The right answer is', a - b,'\n',
               '\t Here is another one, STAY FOCUSED\n',
               '\t Loading...\n',
               '\t')
#The program asks for a division
    print('\t', a,'//', b, '=')
    f = eval(input('\t answer: '))
    if f == a // b:
        print('\t CORRECT!!!\n',
              '\t The end, THANK YOU')
        score = score + 1
        print('Your score is', score, 'of 40')
    else:
         print('\t WRONG!!!\n',
               '\t The right answer is', a // b,'\n',
               '\t The end, THANK YOU')
