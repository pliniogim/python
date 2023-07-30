import os


#alternative 1
# platform = (platform.system())

# def clearScreen():
#     if(platform == "Linux"):
#         os.system('clear')
#     else:
#         if(platform == "Windows"):
#             os.system('cls')

def clearScreen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
        
def func1():
    print("Function 1 is running.")
    input("Tecle enter to stop")
    clearScreen()

def func2():
    print("Function 2 is running.")
    input("Tecle enter to stop")
    clearScreen()


def func3():
    print("Function 3 is running.")
    input("Tecle enter to stop")
    clearScreen()

def stop_program():
    print("Stopping the program...")
    clearScreen()
    exit()

def show_menu():
    print("Menu:")
    print("1. Run Function 1")
    print("2. Run Function 2")
    print("3. Run Function 3")
    print("0. Stop the program")
