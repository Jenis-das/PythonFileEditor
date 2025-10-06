import os

i = 0
print("Type view for Commands")
file_name = ""




#   ==================== Commands ==================
while True:
    cmd = input("-> ").lower().strip()
    if cmd == "view":
        print("")
        print("To View File : v")
        print("To Write Over File : w")
        print("To Update File : a or edit")
        print("To create File : x")
        print("To Run Operations on new File : new")
        print("To view name of the file : fileName")
        print("To know Where the cursor is : tell")
        print("To move the cursor : seek")
        print("To read the line of the file : readL")
        print("To read the lines of the file : readLs")
        print("")
#   ==================== Commands ==================





#   ==================== File Check ==================
    if not file_name:
        while True:
            file_name = input("File name -> ")
            if file_name == "exit":
                cmd = "exit"
                break


            if not "." in file_name:
                print("--- Enter a Valid File Name ---")
                continue
            if not os.path.exists(file_name):
                file = input(f"File Doesnt Exists 'Y' for Create New File With {file_name} -> ")
                if "." in file_name:
                    if file == "Y" or file == "y":
                        with open(file_name, "x"):
                            print("File is Created")
                            break
            else:
                break
            
    elif cmd == "new":
        file_name = input("New File -> ")
#   ==================== File Check ==================





#   ==================== Read Mode ==================
    if cmd == "v" and file_name:
        print("Viewing in reading Mode")
        print("To View in readline Mode Type readL")
        print("To View in readlines Mode Type readLs")
        mode = input("View Mode Specify Default is 'Reading' : ")
        print("--------- File Opened ---------")
        print("")
        if mode == "readL":
            with open(file_name, "r") as f:
                print(f.readline())
        elif mode == "readLs":
            with open(file_name, "r") as f:
                print(f.readlines())
        else:
            with open(file_name, "r") as f:
                print(f.read())

        print("--------- File Closed ---------")
#   ==================== Read Mode ==================




    
#   ==================== Write Mode ==================
    elif cmd == "w" and file_name:
        print("Writing Mode Executed")
        print("")
        print("WARNING WRITE MODE OVERWRITES YOUR FILE")
        print("")
        with open(file_name, "r") as f:
                f.read()
        mode = input("Data already Presented in your file Y To Overwrite : ")
        if mode == "Y" or mode == "y":
            print("--------- File Opened ---------")
            print("")   
            with open(file_name, "w+") as f:
                f.read()
                f.write(input("You Are In Write Mode : "))
            print("")   
            print("--------- File Closed ---------")
#   ==================== Write Mode ==================




    
#   ==================== Append Mode ==================
    elif (cmd == "a") and file_name:
        print("You are Now in Append Mode")
        print("")
        print("--------- File Opened ---------")
        print("")   
        with open(file_name, "a+") as f:
            m = f.tell()
            f.seek(0)
            f.read()
            f.seek(m)
            f.write(input(""))
        print("")   
        print("--------- File Closed ---------")

#   ==================== Append Mode ==================




#   ==================== Edit Mode ==================
    elif (cmd == "edit") and file_name:
        print("You are Now in editing Mode")
        print("")
        print("--------- File Opened ---------")
        print("")
        m = "" 
        with open(file_name, "r") as f:
            m = f.read()
        with open(file_name, "w") as f:
            f.write(m)
            f.write(input(m))
        print("")   
        print("--------- File Closed ---------")
#   ==================== Edit Mode ==================




#   ============== File Namme View ===============
    if cmd == "fileName" and file_name:
        f = open(file_name, "r")
        print(f.name)
        f.close()
    elif not file_name:
        print("File name Not mentioned")
#   ============== File Namme View ===============
        




#   ==================== Exit ====================
    if cmd == "exit":
        print("Good Bye Bro 🙃")
        break
#   ==================== Exit ====================

    if i == 100:
        break
    i+=1











