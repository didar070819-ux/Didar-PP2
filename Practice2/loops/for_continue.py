#for loop comtinue
x="Didar"
cnt=0
for i in x:
    if i.islower():
        cnt+=1
    elif i.isupper():
        continue
print(cnt)

#some basic example

#print only odds
for i in range(1,8):
    if i%2==0:
        continue
    print(i)

#skip D, d
name="Didar"
for i in name:
    if i=="D" or i=="d":
        continue
    print(i,end=" ")