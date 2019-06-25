s=input()
li=[]
def fi():
    c=0
    for i in s:
        if (not li and i==")"):
            return -1
        if not li:
            li.append(i)
        else:
            l=len(li)
            if(li[l-1]=="(" and i==")"):
                li.remove(li[l-1])
                c+=1
            else:
                li.append(i)
    if not li:
        return c
    else:
        return -1
print(fi())
            
        
