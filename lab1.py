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
    result=re.findall(r'\b[\w\d]+@[\w\d.]+', d.text)
    k=0
    for i in range(len(result)):
            for j in range(len(emails)):
                if result[i]==emails[j]:
                                    k=1
            if k==0:
                emails.append(result[i])
            k=0
    result=[]
def page(d, deep):
    reference.append(d.url)

    deep+=1
    deep1=deep
    lookfor(d)

    newref=StartRef + '([A-z0-9-/+=&?_$]+)'
    refs = re.findall(r'<a href=[\"\']'+newref + '[\"\']>', d.text)
    if deep < maxdeep:
            z=0
            for i in range(len(refs)):
                    for j in range(len(reference)):
                            if StartRef+refs[i]==reference[j]:
                                        z=1
                    if z==0:
                            dop=requests.get(StartRef +refs[i])
                            page(dop, deep)
                    z=0
            deep=deep1
page(d,0)


print(emails)
print(len(emails))
print(time.clock())
print('Max deep'  + str(maxdeep))
