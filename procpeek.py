import os

pidFlag = False

while pidFlag == False:
    try:
        processId = int(input("Enter PID: "))

        if processId > 0:
            processPath = f"/proc/{processId}"
            processExists = os.path.exists(processPath)

            if processExists:
                print("Process exists here:", processPath)

                with open(f"{processPath}/status", "r") as file:
                    content = file.read()
                print(content)
                pidFlag = True

            else:
                print("PID",processId,"does not exist, please try again")

        else:
            print("PID",processId,"is invalid, please try again")   

    except ValueError:
        print("Please enter a valid integer")

