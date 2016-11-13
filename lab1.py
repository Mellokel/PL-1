import requests
import re
import time

StartRef='http://www.mosigra.ru/'
maxdeep=2
d=requests.get(StartRef)
emails=[]
reference=[]

time.clock()
def lookfor(d):
    result=re.findall(r'\b[\w_.+-]+@[\w.]+', d.text)
    k=0
    for i in range(len(result)):
            for j in range(len(emails)):
                if result[i]==emails[j]:
                    k=1
            if k==0:
                emails.append(result[i])
            k=0
    result=[]

#print(time.clock())

def page(d, deep):
    reference.append(d.StartRef)

    deep+=1
    deep1=deep
    lookfor(d)

    newref=StartRef + '([\w-/+=&?_$]+)'
    refs = re.findall(r'<a href=[\"\']'+newref + '[\"\']>', d.text)
    if deep < maxdeep:
            k=0
            for i in range(len(refs)):
                for j in range(len(reference)):
                    if StartRef+refs[i]==reference[j]:
                        k=1
                    if k==0:
                        dop=requests.get(StartRef +refs[i])
                        page(dop, deep)
                    k=0
                deep=deep1
page(d,0)


print(emails)
print(len(emails))
print(time.clock())
print('Max deep'  + str(maxdeep))
