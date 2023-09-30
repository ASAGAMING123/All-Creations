myList = [22,4,16,38,13]
choice = 0
for attempt in range (17179869184):
    print("Attempt number:",attempt)
    print("The list 'myList' has the following elements",myList)
    print("L I S T O P E R A T I O N S")
    print("1. Append an element")
    print("2. Delete an existing elmenht by its value")
    print("3. Sort the list in ascending order")
    choice = int(input("Enter your choice (1-3):"))
    if choice == 1:
        element = eval(input("Enter the element to be appended:"))
        myList.append(element)
        print("The element has been appended")
    elif choice == 2:
        element = int(input("Enter the element to be deleted:"))
        if element in myList:
            myList.remove(element)
            print("The element",element,"has been deleted")
        else:
            print("The element",element,"is not present in the list")
    elif choice == 3:
        myList.sort()
        print("The  list has been shorted")
        print(myList)
    else:
        print("Choice is not valid")
         
