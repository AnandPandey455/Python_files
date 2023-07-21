dict={}

def user_action(a):
    if(a==1):
        new_name=input("Enter a new name --> ")
        new_content=input("Enter a new content --> ")
        new_dict={str(new_name):str(new_content)}
        dict.update(new_dict)
        print("UPDATED")
        b=int(input(" ~Enter 1 for adding a new name \n ~Enter 2 for searching amy content in the list \n ~Enter 3 for deleting a name --> "))
        user_action(b)
    if(a==2):
        find=str(input("Enter a name to find person --> "))
        print("Searching...")
        print("result found",dict[find])
        c=int(input(" ~Enter 1 for adding a new name \n ~Enter 2 for searching amy content in the list \n ~Enter 3 for deleting a name --> "))
        user_action(c)
        
    if(a==3):
        name=input("Enter a name which you want to delete --> ")
        dict.pop(name)
        print("deleted")
        print(dict)
        w=int(input(" ~Enter 1 for adding a new name \n ~Enter 2 for searching amy content in the list \n ~Enter 3 for deleting a name --> "))
        user_action(w)
    
    
a = int(input(" ~Enter 1 for adding a new name \n ~Enter 2 for searching amy content in the list \n ~Enter 3 for deleting a name --> "))
user_action(a)
