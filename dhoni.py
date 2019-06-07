string1="dhoni"
string2=input()
c=0 
status=0
for i in range(0,len(string1)):
    for j in range(0,len(string2)):
        if(string2[j] in string1):
            if(string1[i]==string2[j]):
                string1[i].replace(string1[i],'*')
                c+=1
        else:
            status=1
        
if(len(string1)==c and status==0):
    print('yes')
else:
    print('no')
