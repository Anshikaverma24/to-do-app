print("        -📋YOU HAVE TO DO✅-           ")

options=["edit - add" , "delete"]
tasks_for_today=input("enter the asks you want to do today - ")
to_do=[]
to_do.append(tasks_for_today)
print("would you like to do modifications with your tasks? ")

edit=input("say yes if you would like edit your tasks - ")
if edit=="yes":

 add=input("say yes if you would like add some more tasks -  ")

 if add=="yes":
    added=input("enter the task you would like to add - ")
    to_do.append(added)

 delete=input('say yes if you would like delete your tasks - ')
 for i in range(len(to_do)):
    print(to_do[i])
 if delete=="yes":
    delte=input("enter the task you want to delete - ")
    to_do.remove(delte)
    for i in range(len(to_do)):
        print(to_do[i])

print("NUMBER OF TASKS YOU HAVE TO DO TODAY")
i=0
tasks=0
while i<len(to_do):
    tasks=tasks+1
    i+=1
print(tasks)

done_tasks=int(input("enter the total number of tasks that you have completed : "))
in_progress=int(input("enter the number of tasks which are in progress : "))
not_done=int(input("enter the number of tasks which you haven't done : "))
status=[done_tasks , in_progress , not_done]
i=0
sum=0
while i<len(status):
   sum=sum+status[i]
   print(sum)
   i+=1
if sum>len(to_do):
   print("your tasks is more than total number of tasks, please check the tasks once")
elif sum<len(to_do):
   print("your tasks is less than the total number of tasks,please check the tasks once")
else:
   print("your schedule have been set")
