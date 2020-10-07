import random
l1=['Stone','Paper','Scissor']
a=b=n=0
ch="y"
while (n<5)and(ch=="y"or ch=="Y"):
    user=input("YOUR TURN \n")
    comp=random.choice(l1)
    if((comp=="Stone"or comp=="stone"or comp=="STONE")and (user=="Paper"or user=="paper"or user=="PAPER"))or((comp=="Paper"or comp=="PAPER"or comp=="paper")and (user=="Scissor"or user=="scissor"or user=="SCISSOR"))or((comp=="Scissor"or comp=="scissor"or comp=="SCISSOR")and (user=="Stone"or user=="stone"or user=="STONE")):
        a=a+1
        print(comp)
        n=n+1
    elif((comp=="Paper"or comp=="PAPER"or comp=="paper")and(user=="Stone"or user=="stone"or user=="STONE"))or((comp=="Scissor"or comp=="scissor"or comp=="SCISSOR") and  (user=="Paper"or user=="paper"or user=="PAPER"))or((comp=="Stone"or comp=="STONE"or comp=="stone") and (user=="Scissor"or user=="scissor"or user=="SCISSOR")) :
        b=b+1
        print(comp)
        n=n+1
    elif((comp=="Paper"or comp=="PAPER"or comp=="paper")and(user=="Paper"or user=="paper"or user=="PAPER"))or((comp=="Scissor"or comp=="scissor"or comp=="SCISSOR") and  (user=="Scissor"or user=="scissor"or user=="SCISSOR"))or((comp=="Stone"or comp=="STONE"or comp=="stone") and (user=="Stone"or user=="stone"or user=="STONE")) :
        a=a+1
        b=b+1
        n=n+1
        print(comp)
    else:    
        print("INVALID INPUT")
        n=n+1
        ch=input("Want to continue (y/n)")

if(a>b):
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tYOU WIN")
elif(b>a):
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tYOU LOSE")
else:
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tTIE")
