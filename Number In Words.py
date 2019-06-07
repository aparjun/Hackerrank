#PF-Prac-33
def integer_to_english(number):
    l=len(number)
    s=""
    o={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    teen={11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
    t={0:"",1:"ten",2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninty"}
    h={0:"",1:"one hundred",2:"two hundred",3:"three hundred",4:"four hundred",5:"five hundred",6:"six hundred",7:"seven hundred",8:"eight hundred",9:"nine hundred"}
    if(int(number)<1 or int(number)>1000):
        return -1
    elif(l==1):
        s=o[int(number)]
    elif(l==2):
        if(int(number)%10==0):
            s=t[int(number[0])]
        elif(int(number)<20):
            s=teen[int(number)]
        else:
            s+=t[int(number[0])]
            s+=" "
            s+=o[int(number[1])]
    else:
        if(l==4):
            s+="one thousand"
        else:
            s+=h[int(number[0])]
            if(int(number[1:3])!=0):
                s+=" and "
            if(int(number[1:3])<10 and int(number[1:3])>0):
                s+=o[int(number[2])]
            elif(int(number[1:3])%10==0):
                s+=t[int(number[1])]
            elif(int(number[1:3])<20):
                s+=teen[int(number[1:3])]
            else:
                s+=t[int(number[1])]
                s+=" "
                s+=o[int(number[2])]
    return s        
        
    

number=input()
print(integer_to_english(number))
