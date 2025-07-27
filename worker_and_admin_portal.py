from datetime import datetime

print("Hello welcome to the HR portal")
print("Please enter your details as per asked by the portal")

while True:
    userinput = input("Please enter -w- for worker, -a- for Admin and -e- for exit: ").lower()

    if userinput == 'w':
        print("Please enter common entry id and password")
        cid = "gtpl1234"
        cpass = "1234567890"
        ecid = input("Please enter the common entry id: ")
        ecpass = input("Please enter the common entry password: ")

        if (ecid, ecpass) == (cid, cpass):
            name = input("Please enter your name: ")
            Id = input("Please enter your Employee ID (EID): ")
            now = datetime.now()

            print("To mark attendance enter -p-; to add leave enter -l-")
            entry = input("Submit your response: ").lower()

            if entry not in ['p', 'l']:
                print("Invalid entry type. Please enter 'p' or 'l'.")
                continue

            with open("workerlog.txt", "a") as file:
                file.write(f'{name} EID {Id} has marked for {entry} at {now}\n')

            print("Entry recorded successfully.")
        else:
            print("Wrong ID or password entered. Please try again.")

    elif userinput == 'a':
        adminid = "admin1234"
        adminpass = "123456789"
        eadminid = input("Please enter the admin ID: ")
        eadminpass = input("Please enter the admin password: ")

        if (eadminid, eadminpass) == (adminid, adminpass):
            print("Would you like to see worker log?")
            print("Type 'log' to see worker log")
            print("Type 'clear' to clear the log file")
            admininput = input("Please enter your response: ").lower()

            if admininput == 'log':
                try:
                    with open("workerlog.txt", "r") as file:
                        log = file.read()
                    print("\n--- Worker Log ---")
                    print(log if log else "The log file is empty.")
                    print("------------------\n")
                except FileNotFoundError:
                    print("No log file found. No entries recorded yet.")

            elif admininput == 'clear':
                with open("workerlog.txt", "w") as file:
                    pass
                print("Log file cleared.")

            else:
                print("Invalid input. Please enter 'log' or 'clear'.")

        else:
            print("Wrong admin credentials. Please retry.")

    elif userinput == 'e':
        print("Thank you for using the HR portal. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 'w', 'a', or 'e'.")



