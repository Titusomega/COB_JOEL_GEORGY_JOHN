import re
def remove_punctuation(string):
        return re.sub(r'[^\w\s]', '', string)
try:
    
    
    s=input("Enter the file location")
    a=open("D:\Games\joel.txt","r+")
    dic=dict()
    srr=""
    for i in a:
        i=i.strip()
        i=i.lower()
        lst=i.split(" ")
        for j in lst:
            j=remove_punctuation(j)
            if(j not in dic and j.isspace()==False and j!=''):
                print(j)
                dic[j]=1
            elif j!='':
                dic[j]=dic[j]+1
                    
    for i in dic:
        print("The number of occurence of ",i," is ",dic[i])
except FileNotFoundError:
    print("File location is wrong")
