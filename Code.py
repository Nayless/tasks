sIn=open("start.txt", "r")
sOut=open("result.txt","w")
c=0
summ=0
for i in sIn:
    summ+=int(i)
    c+=1
sOut.write(str(summ//c))
sOut.close()
sIn.close()
