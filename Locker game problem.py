#Locker game problem

Lockers = [False]*100
Skip = 1
Start = 0
StuLim = 100
Open = []

while Start <= StuLim:
    for i in range(Start,len(Lockers),Skip):
        if Lockers[i] == False:
            Lockers.remove(False)
            Lockers.insert(i,True)
        else:
            Lockers.remove(True)
            Lockers.insert(i,False)
    Skip+=1
    Start+=1
for i in range(0,len(Lockers)):
    if Lockers[i] == True:
        print("Locker", i,"is open")

