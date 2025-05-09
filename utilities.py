import msvcrt
import time
import os

# --- Format/design function ---
#region


#Funtion like print but writes each letter with delay
def write(string):
    # For-loop which writes each letter with delay
    for cha in string:
        print(cha,end="",flush=True)
        # Wait before repeat loop
        time.sleep(0.05)
    print("")

# Prints a line to devide information
def row_devider():
    row = "-"*100
    print(row)

#Clear console if player clicks on something
def clear_console():
    write("Press any button to continue...")

    #Waiting for any key on keyboard to be pressed to contine
    msvcrt.getch()

    #clearing console
    os.system('cls')
#endregion