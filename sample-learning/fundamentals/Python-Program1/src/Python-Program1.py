# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "scott_r_parker"
__date__ = "$Jul 10, 2017 4:41:45 PM$"

if __name__ == "__main__":
    print "Characters and outputs"
    print ('A\nB\nC') #showing the \n special character (line break)
    print ('D\tE\tF') #showing the \t special character (tab)
    print ('WX\bYZ') #showing the \b special character (backspace)
    print ('1\a2\a3\a4\a5\a6') #showing the \a special character (System beep on some systems)
                               #in Netbeans seems to be a whitespace
    print ('123456') 
    print ('\n')
    
    print "User inputs"
    x = input('Please enter a numeric value: ')
    num1=int(x)
    num2=float(x)
    print "value entered was: ", x
    print('Type x: ', type(x))
    print ('num1 value is: ', num1)
    print ('Type num1: ', type(num1))
    print ('num2 value is: ', num2)
    print ('Type num2: ', type(num2))
    num3=num1+num2
    print ('num3 value is: ', num3)
    print ('Type num3: ', type(num3))
    
    x = input('please enter some text: ')
    print ('value entered was: ', x)
    print ("Type x: ", type(x))
    