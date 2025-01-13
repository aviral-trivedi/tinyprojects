
def entries():
    Info = {}
    flag = True
    while flag:
        roll = int(input("Roll Number "))
        name = input("Name ")
        marks = float(input("Marks "))

        Info[roll] = [name,marks]

        try:
            if input("Keep Going? Y/N ").lower() != "y":
                flag = False
                print()
        except ValueError:
            print("Invalid Answer")
    return Info

def write_data(Data):

    with open("/home/cleon/Local-Files/Old-Backup/Code Files/VS Code/Learning/ProjectH3ll/Students/Report.txt", "a") as file:
        file.write("#"*50)
        file.writelines("\n")
        for roll_no, details in Data.items():
            name, marks = details  # Unpack the list into name and marks
            file.write(f"Roll No: {roll_no:<8} Name: {name:<10} Marks: {marks:<5}\n")
        file.write("#"*50)


def display_data(Data):

    if input("Display Data? Y/N ").lower() != "y":
        return
    else:
        pass

    for key,value in Data.items():
        print(f"Roll No: {key}\t",end="",sep="")
        print(f"Name: {value[0]}\t",end="",sep="")
        print(f"Marks: {value[-1]}")


    
Data = {1:["Aviral",75], 2:["Trix",50], 13:["Viv",70], 1456:["Zy",60], 18:["Zin",70], 10:["Xyx",72]}
#Data = entries()

#display_data(Data)

write_data(Data)

    



    