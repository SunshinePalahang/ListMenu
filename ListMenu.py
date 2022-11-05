from colorama import Fore, Style
list1 = [15, 4, 20, 31, 19, 30, 58, 64, 90, 91]
print("Array: ", list1)
def menu():
    print("Menu:")
    print(Fore.MAGENTA+"   1 -> Add an element")
    print(Fore.CYAN+ "   2 -> Insert an element")
    print(Fore.GREEN+"   3 -> Modify an element")
    print(Fore.BLACK+"   4 -> Delete an element")
    print(Fore.YELLOW+"   5 -> Arrange in ascending order")
    print(Fore.RED+"   6 -> Arrange in descending order")
    print(Fore.BLUE+"   7 -> Show the smallest element")
    print(Fore.MAGENTA+"   8 -> Show the largest element")
    print(Fore.GREEN+"   9 -> Show the sum of the elements")
    print(Fore.BLACK+"   0 -> Exit the Program")
    print(Style.RESET_ALL)


while True:
    menu() 
    option = int(input("What do you want to do? (0-9): "))
    if option == 1:
        select1 = int(input("Enter an element you want to add: "))
        list1.append(select1)
        print(Fore.MAGENTA+"\nNew list with added element")
        print(list1)
        print(Style.RESET_ALL)
    elif option == 2:
        select2 = int(input("Enter an element you want to insert: "))
        index = int(input("At what particular index?: "))
        list1.insert(index,select2)
        print(Fore.CYAN+"\nNew list with inserted element")
        print(list1)
        print(Style.RESET_ALL)
    elif option == 3:
        select3 = int(input("Enter an element you want to modify: "))
        index = int(input("At what particular index?: "))
        list1[index] =select3
        print(Fore.GREEN+"\nNew list with modified element")
        print(list1)
        print(Style.RESET_ALL)
    elif option == 4:
        select4 = int(input("Enter an element you want to delete: "))
        list1.remove(select4)
        print(Fore.BLACK+"\nNew list with deleted element")
        print(list1)
        print(Style.RESET_ALL)
    elif option == 5:
        list1.sort()
        print(Fore.YELLOW+"\nNew list sorted in ascending order")
        print(list1)
        print(Style.RESET_ALL)
    elif option == 6:
        list1.sort(reverse=True)
        print(Fore.RED+"\nNew list sorted in descending order")
        print(list1)
        print(Style.RESET_ALL)
    elif option == 7:
        print(Fore.BLUE+"Smallest element: ") 
        print(min(list1)) 
        print(Style.RESET_ALL) 
    elif option == 8:
        print(Fore.MAGENTA+"Largest element: ") 
        print(max(list1))
        print(Style.RESET_ALL) 
    elif option == 9:
        print(Fore.GREEN+"Total: ")
        print(sum(list1)) 
        print(Style.RESET_ALL)
    elif option == 0:
        print(Fore.BLACK+"THANK YOU FOR USING MY PROGRAM! \n ©️ 2022 All rights reserved.") 
        break
    else:
        print(Fore.RED+"Invalid input. Please Try Again.")
        print(Style.RESET_ALL)
