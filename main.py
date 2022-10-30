#DICTIONARY TO-DO LIST CAUSE ASI TOLD ME TO MAKE :))))))))))))))))

lists = {}

#ALL FUNCTIONS ----------------------------------------------------------------------------------------------------------------------------------------------------------

#function to check if should continue or quit
def contin(quit, cont):
    while True:
            ListInput = input("Would you like to " + quit.upper() + ", or " + cont.upper() + ":")
            ListInput.lower()
            if ListInput not in (str(quit), str(cont)):
                print("We didn't quite get that, please try again ")
                continue
            if ListInput == str(quit):
                return 1
                break
            if ListInput == str(cont):
                return 2
                break

#function to check if given input matches with given list of accepted inputs
def checkstr(checkinput, checklist):
    checkinput.lower()
    while True:
        if checkinput not in checklist:
            checkinput = input("This is not a valid option, please try again: ")
            continue
        elif checkinput in checklist:
            return checkinput

def printlist(a):
    print("placement")

#function to view a certain dictionary
def view():
    while True:     
        viewinput = input("Would you like to view ALL lists, view the contents in a CERTAIN list, or QUIT? ")
        checkreturn = checkstr(viewinput , "'all', 'certain'")
        if checkreturn == "all":
            #used to see all dictionary
            print("current lists: ")
            for key in lists.keys(): 
                print(key)
            break
        elif checkreturn == "certain":
            while True:
                listname = input("What list would you like to view? ")
                if listname not in lists.keys():
                    editinput = input("This is not a list, would you like to RETRY or QUIT? ")
                    checkreturn = checkstr(editinput , "'retry', 'quit'")
                    if checkreturn == "retry":
                        continue
                    elif checkreturn == "quit":
                        break
                else:
                    #used to see items in list
                    print("These are all the items in the list, " + listname)
                    for key, value in lists[listname].items(): 
                        print("{}: {}".format(key, value))
                break
            break
        elif checkreturn == "quit":
             break
    

#function to delete a dictionary
def delete():
    while True:
        print("current lists: ")
        for key in lists.keys(): 
            print(key)
        listname = input("What list would you like to delete? ")
        if listname not in lists.keys():
            editinput = input("This is not a list, would you like to RETRY or QUIT? ")
            checkreturn = checkstr(editinput , "'retry', 'quit'")
            if checkreturn == "retry":
                continue
            elif checkreturn == "quit":
                break
        else:
            del(lists[listname])
            print("The list, " + listname + ", has been deleted")
            break
    
   
        


#function to remove a certain key:value inside a dictionary
def remove(a):
    if a == 1:
        while True:
            print("Current Lists: ")
            for key in lists.keys(): 
                print(key)
            listname = input("What list would you like to remove from? ")
            if listname not in lists.keys():
                editinput = input("This is not a list, would you like to RETRY or QUIT? ")
                checkreturn = checkstr(editinput , "'retry', 'quit'")
                if checkreturn == "retry":
                    continue
                elif checkreturn == "quit":
                    break
            else:
                break
    else:
        listname = a
    while True:
        print("These are all the items in the list, " + listname)
        for key, value in lists[listname].items(): 
            print("{}: {}".format(key, value))
        listtype = input("Enter an item you want to remove from the list, " + listname + ": ")
        if listtype not in lists[listname]:
            editinput = input("This is not in a value in the " + listname + " list, would you like to RETRY or QUIT? ")
            checkreturn = checkstr(editinput , "'retry', 'quit'")
            if checkreturn == "retry":
                continue
            elif checkreturn == "quit":
                break
        else:
            del(lists[listname][listtype])

            print("These are the items remaining in the list, " + listname)
            for key, value in lists[listname].items(): 
                print("{}: {}".format(key, value))

            userinput = input("Would you like to REMOVE more or FINISH your list? ")
            checkreturn = checkstr(userinput , "'remove', 'finish'")
            if checkreturn == "remove":
                continue
            elif checkreturn == "finish":
                break
    

#function to add to a certain dictionary
def add(a):
    if a == 1:
        while True:
            print("Current Lists: ")
            for key in lists.keys(): 
                print(key)
            listname = input("What list would you like to add to? ")
            #fix this - if there are no lists at all, ask if they want to create one or quit
            
            if listname not in lists.keys():
                print("This is not a list, please try again")
                continue
            else:
                break
    else:
        listname = a
    while True:
        listtype = input("Enter an item you want to do add to the list? ")
        listcount = input("How many do you want? ")
        lists[listname][listtype] = listcount

        print("These are all the items in the list, " + listname)
        for key, value in lists[listname].items(): 
            print("{}: {}".format(key, value))
        userinput = input("Would you like to ADD more or FINISH your list? ")
        checkreturn = checkstr(userinput , "'add', 'finish'")
        if checkreturn == "add":
            continue
        else:
            break

    
#function to create a dictionary, and then add key:values to it
def create(a): 
    while True:
        if a == 1:
            listname = input("What would you like to name your list? ")
        else:
            listname = a

        if listname in lists.keys():
            print("Current Lists: ")
            for key in lists.keys(): 
                print(key)
            userinput = input("This is already a list, would you like to ADD or REMOVE something from " + listname + "? ")
            checkreturn = checkstr(userinput , "'add', 'remove'")
            if checkreturn == "add":
                add(listname)
            elif checkreturn == "remove":
                remove(listname)
        else:
            lists[listname] = {}
            add(listname)
            break
        break

#function to edit any key:value in any dictionary
def edit():
    while True:
        print("current lists: ")
        for key in lists.keys(): 
            print(key)
        listname = input("What list would you to edit? ")
        if listname not in lists.keys():
            userinput = input("This is not a list, would you like to CREATE this list or RETRY? ")
            checkreturn = checkstr(userinput , "'create', 'retry'")
            if checkreturn == "create":
                create(listname)
                end = True
                break
            elif checkreturn == "retry":
                continue
        else:
            print("These are all the items in the list, " + listname)
            for key, value in lists[listname].items(): 
                print("{}: {}".format(key, value))
            userinput = input("What item do you want to change in the list? ")
            while True:
                if userinput not in lists[listname]:
                    editinput = input("This is not in a value in the" + listname + "list, would you like to ADD it or RETRY? ")
                    checkreturn = checkstr(editinput , "'add', 'retry'")
                    if checkreturn == "add":
                        add(listname)
                        break
                    elif checkreturn == "retry":
                        break
                else:
                    changekey = input("What do you want to change this item to? ")
                    changevalue = input("What do you want its value to be? ")
                    lists[listname][changekey] = lists[listname].pop(userinput) 
                    lists[listname][changekey]= changevalue
                    break
            break
        
# USER INTERFACE -------------------------------------------------------------------------------------------------------------------------------------------------------

while True:
    userinput = input("Would you like to CREATE a list, ADD items, EDIT items, REMOVE items, DELETE a list, VIEW a list, or QUIT? ")
    userinput.lower()
    checkreturn = checkstr(userinput , "'create', 'add', 'edit', 'remove', 'delete', 'view', 'quit'")
    if checkreturn == "create":
        create(1)
    elif checkreturn == "add":
        add(1)
    elif checkreturn == "edit":
        edit()
    elif checkreturn == "remove":
        remove(1)
    elif checkreturn == "delete":
        delete()
    elif checkreturn == "view":
        view()
    elif checkreturn == "quit": 
        break

input("Press any button to exit")
