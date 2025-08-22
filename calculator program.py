def calculator():
      import cmath
      while True:
        option1 = int(input('''
please select the task you want the calculator to be able to do
1-Do basic arithmetic operation
2-Solve quadratic equations(with or without complex roots
3-Solve simultaneous equation(both 2 and 3 unknowns
4-matrix calculations
option: '''))
        
        if option1 == 1:
          print("This option will only focus on basic arithmetic operations")
          option2 = int(input("""
1-Division
2-Multiplication
3-Addition
4-Subtraction
option: """))
          number1 = int(input("Enter your first number: "))
          number2 = int(input("Enter your second number: "))
          if option2 == 1:
              selection=input("Do you want to take number2 / number1 (yes/y/yep) (no/n/nope): ")
              select = selection.lower()
              if select.strip() in ["yes","yep","y"]:
                if number1!=0:
                 division = number2/number1
                 print('{0} / {1} = {other}'.format(number2,number1,other = division))
                else:
                 print('the operation {0} / {1} will give a math error '.format(number2,number1))
              elif select.strip() in ["nope","no","n"]:
                division = number1/number2
                print('{0}/{1} = {other}'.format(number1,number2,other=division))
              else:
               print("please select one of the commands")
          elif option2 == 2:
              multiplication = number2 * number1
              print(f'{number1} *{number2} = {multiplication}')
          elif option2 == 3:
              selection =input("Do you want to take number2 + number1 (yes/y/yep) (no/n/nope): ")
              select = selection.lower()
              if select.strip() in ["yep","yes","y"]:
               addition = number2 + number1
               print(f'{number2} + {number1} = {addition}')
              elif select.strip() in ["nope","no","n"]:
                addition = number1 + number2
                print(f'{number1} + {number2} = {addition}')
              else:
               print("please input one of the commands")
          elif option2 == 4:
              selection = input("Do you want to do number2 - number1 (yes/y/yep) (no/n/nope): ")
              select = selection.lower()
              if select.strip() in ["yes","yep","y"]:
               subtraction = number2 - number1
               print(f'{number2} - {number1} = {subtraction}')
              elif select.strip() in ["nope","no","n"]:
               subtraction = number1 - number2
               print(f'{number1} - {number2} = {subtraction}')
              else:
               print("please input one of the commands")
        elif option1 == 2:
          print("This option will enable you to solve quadratic equations")
          a = int(input("please can you enter the value of a: "))
          b = int(input("please can you enter the value of b: "))
          c = int(input("please can you enter the value of c: "))
          discriminant = b**2 - (4*a*c)
          if discriminant == 0 :
           x = -b /(2*a)
           print('The value of x is {}'.format(x))
          elif discriminant >0:
           x1 = (-b +cmath.sqrt(discriminant))/(2*a)
           x2 = (-b -cmath.sqrt(discriminant))/(2*a)
           print('x1: {0} and x2: {1}'.format(x1,x2))
          elif discriminant<0:
           x1 = (-b +cmath.sqrt(discriminant))/(2*a)
           x2 = (-b -cmath.sqrt(discriminant))/(2*a)
           print('x1: {0} and x2: {1}'.format(x1,x2))
     
        elif option1 == 3:
          print("this option will help you to calculate a simultaneous equation having either 2 or 3 unknowns")
          select= input('''please choose what you want this option to do: 
                     1- two unknowns
                     2- three unknowns
                     option: ''') 
          if select == '1':
            print('''the equation will be in this form
ax+by=c
dx+ey=f''')
            a =float(input("please can you enter the value of a: "))
            b =float(input("Please can you enter the value of b: "))
            c =float(input("Please can you enter the value of c: "))
            d =float(input("Please can you enter the value of d: "))
            e =float(input("Please can you enter the value of e: "))
            f =float(input("Please can you enter the value of f: "))
            Try = (e*a - b*d)
            if Try == 0:
              print("This has given an error because the denominator {} == 0".format(Try))
            else:
             x =(e*c - b*f)/Try
             y =(d*c - a*f)/Try
             print(f"the values of x and y are respectively {x} amd {y}")
          elif select == '2':
           print('''the equation will be in this form
ax+by+cz= j
dx+ey+fz= k
gx+hy+iz= l''')
           a = float(input("Enter the value of A: "))
           b = float(input("Enter the value of B: "))
           c = float(input("Enter the value of C: "))
           j = float(input("Enter the value of J: "))
           d = float(input("Enter the value of D: "))
           e = float(input("Enter the value of E: "))
           f = float(input("Enter the value of F: "))
           k = float(input("Enter the value of K: "))
           g = float(input("Enter the value of G: "))
           h = float(input("Enter the value of H: "))
           i = float(input("Enter the value of I: "))
           l = float(input("Enter the value of L: "))
           Try =(a*((e*i)-(f*h))-b*((d*i)-(f*g))+c*((d*h)-(e*g)))
           if Try ==0:
            print("it will give a math error because the denominator {} is zero".format(Try))
           else:
            x = (j*((e*i)-(f*h))-k*((b*i)-(c*h))+l*((b*f)-(c*e)))/(a*((e*i)-(f*h))-b*((d*i)-(f*g))+c*((d*h)-(e*g)))
            y = (j*((f*g)-(d*i))-k*((c*g)-(a*i))+l*((c*d)-(a*f)))/(a*((e*i)-(f*h))-b*((d*i)-(f*g))+c*((d*h)-(e*g)))
            z = (j*((d*h)-(g*e))-k*((a*h)-(b*g))+l*((a*e)-(b*d)))/(a*((e*i)-(f*h))-b*((d*i)-(f*g))+c*((d*h)-(e*g)))
            print("the values of x,y and z are respectively {0},{1} and {other}".format(x,y,other = z))


        elif option1 == 4:
          print('''This choice will enable you to solve basic matrix operation''')
          choice = int(input('''
1-calculate the determinant of a matrix
option: '''))
          if choice ==1:
           print("This will enable you to perform the determinant of a matrix(2*2 matrix or 3*3 matrix)")
           choice2 = int(input('''
1-calculate the determinant of a 2*2 matrix
2-calculate the determinant of a 3*3 matrix
option: '''))
          if choice2 ==1:
           print('''the matrix will be in this form
ax+by
cx+dy''')
           a =float(input("please can you enter the value of a: "))
           b =float(input("Please can you enter the value of b: "))
           c =float(input("Please can you enter the value of c: "))
           d =float(input("Please can you enter the value of d: "))
           determinant = (a*d)-(c*b)
           print('the determinant of the 2*2 matrix is {}'.format(determinant))

          elif choice2 ==2:
           print('''the matrix will be in this form
ax+by+cz
dx+ey+fz
gx+hy+iz''')
           a = float(input("Enter the value of A: "))
           b = float(input("Enter the value of B: "))
           c = float(input("Enter the value of C: "))
           d = float(input("Enter the value of D: "))
           e = float(input("Enter the value of E: "))
           f = float(input("Enter the value of F: "))
           g = float(input("Enter the value of G: "))
           h = float(input("Enter the value of H: "))
           i = float(input("Enter the value of I: "))
           determinant = a*((e*i)-(f*h))-b*((d*i)-(f*g))+c*((d*h)-(e*g))
           print('the determinant of the 3*3 matrix is {}'.format(determinant))

        again =(input("do you want to continue (yes/y) or (no/n): "))
        if again.strip().lower() in ["yes","yep","y"]:
           continue
        elif again.strip().lower() in ["nope","no","n"]:
           print("Thanks for using our calculator!")
           break 
        else:
          print("error!")
                     
calculator()     