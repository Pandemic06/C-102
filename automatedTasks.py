number=int(input("Enter the number of classes that are to be attended"))
tasks=[]
for i in range(0,number):
    subject=input("Specify the subjects")
    time=int(input("Specify the timings"))
    task=[subject,time]
    tasks.append(task)

ask=int(input("What is the time?"))
for i in range(0,number):
    if(tasks[i][1]==ask):
        print("your class for ",tasks[i][0],"has started")
        break
    elif(tasks[i][1]>ask):
        dif=tasks[i][1]-ask
        print("Your class for ",tasks[i][0],"starts in ",dif)
    
    elif(tasks[i][1]<ask):
        dif=ask-tasks[i][1]
        print("Your class for ",tasks[i][0],"started ",dif,"ago")