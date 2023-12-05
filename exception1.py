from ex import InvalidOperator

try:
    a=int(input("ENTER NUMBER      :"))
    b=int(input("ENTER NUMBER      :"))
    op=input("ENTER THE OPERATOR   :")
    if(op=="/"):
        c=a/b
        print("DIVISION OF ",a,"AND",b,"IS",c)
    if op not in["*","+","-","/"] :
        raise InvalidOperator("please enter operators between +,-,*,/")   

except InvalidOperator as x:
    print(x)


except ValueError:
    print("PLEASE ENTER NUMBERS ONLY !!")
except ZeroDivisionError:
    print("PLEASE ENTER NUMBERS GREATER THAN ZERO !!")    
except:
    print("SOMETHING WENT WRONG !!!")
else:
    if(op=="+"):
        c=a+b
        print("ADDITION OF ",a,"AND",b,"IS",c)
    elif(op=="-"):
        c=a-b
        print("SUBTRACTION OF ",a,"AND",b,"IS",c)
    elif(op=="*"):
        c=a*b
        print("MULTIPLICATION OF ",a,"AND",b,"IS",c)            
  
    else:
        pass

