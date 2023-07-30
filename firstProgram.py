import functions_app



def main():
    while True:
        
        functions_app.clearScreen()
        functions_app.show_menu()
        choice = input("Enter your choice: ")
        functions_app.clearScreen()
        
        if choice == "1":
            functions_app.func1()
        elif choice == "2":
            functions_app.func2()
        elif choice == "3":
            functions_app.func3()
        elif choice == "0":
            functions_app.stop_program()
        else:
            print("Invalid choice. Please try again.")
            input()
        
                
        functions_app.clearScreen()

if __name__ == "__main__":
    main()
