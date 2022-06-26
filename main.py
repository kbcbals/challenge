#############################################################################################
#                                 Tiny Robot Navigation System
#############################################################################################

#############################################################################################
#                                   imports
#############################################################################################

import os
from time import sleep  # sleep
from datetime import datetime  # current date and time
import array as arr  # x,y,direction variables

#############################################################################################
#                                   declarations
#############################################################################################
ans = True
record = arr.array('i', [0, 0, 0])  # x,y,f

# get the date and time
now = datetime.now()  # current date and time
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

#############################################################################################
#                                   BANNER
#############################################################################################
print('************************************************************************************')
print('+                                                                                  +')
print('+                       Tiny Robot Navigation System                               +')
print(f'+                          {date_time}                                    +')
print('+                                                                                  +')
print('************************************************************************************')


#############################################################################################
#                                   functions
#############################################################################################


#############################################################################################
#                                   validate_start_command
#

def validate_start_command(line):
    # print(f"validate_start_command called :: {line} ")
    index = 0
    data = line.split(' ')
    # print(len(data))

    # if the first element is PLACE and the count ==2 return true
    if len(data) == 2:  # start of header has more than what its needed
        for char in data:
            index = index + 1
            # print(f" {index} = {char}")
        print("valid header packet Received ")
        return True
    else:
        print(" invalid - Start of Header")
        return False


#############################################################################################
#                                   validate_other_command
#


def validate_other_command(line):
    # print(f"validate_other_command called {line}")
    return True


#############################################################################################
#                                   screen_clear
#


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platform
        _ = os.system('cls')


#############################################################################################
#                                   main
#


def main():
    ans = "999"
    name = ""
    filenames = []

    # create folder - stats,logs
    # logs folder
    # stats folder

    while ans:
        # now call function we defined above
        # screen_clear()
        print("     Menu List:")
        print("""
           1. List input files  
           2. Input File Number to load
           3. Create default input file
           4. Stats
           5. Exit/Quit           
           """)
        ans = input("What would you like to do? ")
        if ans == "1":
            print("\nList input files :")
            i = 1
            for x in os.listdir(os.getcwd()):
                if x.endswith(".inp"):
                    print(f"({i}) {x}")
                    i = i + 1
        elif ans == "2":
            print("\n Enter the file number to load:")
            # throw the error if file not exist in the current folder/ or specified folder.
            # logs folder
            # stats folder
            start_time = datetime.now()
            # try:
            # load the file
            # read the first line and all the lines until you reach a valid start

            ##############################################
            # read lines to get the first valid start line
            ##############################################
            # step 2
            # validate the remaining commands
            # do the thing here
            # validate_start_command
            # except:
            # open the file
            # process the code
            # print the result

            # step 1
            keyfile = open("input4.inp")
            header_recd = False
            for line in keyfile:
                if not header_recd:
                    ret = validate_start_command(line)
                    if bool(ret):
                        header_recd = bool(ret)
                        print(f" **** {line} ****  is a valid start packet ")
                        print("")
                    else:
                        print(f" xxxx {line} xxxx  is not a valid start packet ")
                        print("")
                        # break
                else:
                    ret = validate_other_command(line)
                    if bool(ret):
                        print(f" **** {line} ****  is a valid command")
                        print("")
                    else:
                        print(f" xxxx {line} xxxx  is not a valid command packet ")
                        print("")

            end_time = datetime.now()
            time_diff = (end_time - start_time)
            execution_time = time_diff.total_seconds() * 1000
            # print(f"start time={start_time}, end time={end_time}, Total={round(execution_time, 4)} milliseconds")
            print(f"Total execution time={round(execution_time, 4)} milliseconds")
        elif ans == "3":
            name = input("\n Please enter the name of input file :  ")
        elif ans == "4":
            print("\n some cool Stats:")
            print("\n Number of jobs run :")
            print("\n average time of tot jobs:")
            print("\n maximum time [ Single job]: job-num : time in secs")
            print("\n minimum time [ Single job]:time in secs")
        elif ans == "5":
            print("\n Goodbye")
            exit(0)
        elif ans != "":
            print("\n Not Valid Choice Try again")
        elif ans == "":
            print("\n Can't be empty - Goodbye ")

        print('                                                     ')
        print('*____________________________________________________*')
        print('                                                     ')

        # wait for 2 seconds to show menu
        sleep(2)
        # screen_clear()


#############################################################################################
#                                   Begin
#


if __name__ == '__main__':
    main()
