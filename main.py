import os
# import time  # execution time
from time import sleep  # sleep
from datetime import datetime # current date and time

# get the date and time
now = datetime.now()  # current date and time
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

ans = True
print('************************************************************************************')
print('+                                                                                  +')
print('+                       Tiny Robot Navigation System                               +')
print(f'+                          {date_time}                                    +')
print('+                                                                                  +')
print('************************************************************************************')


#  This system will load the input file from the
#
#
#

# The screen clear function
def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platform
        _ = os.system('cls')


def main():
    ans = "999"
    name = ""

    # create folder - stats,logs
    # logs folder
    # stats folder

    while ans:
        # now call function we defined above
        # screen_clear()
        print("     Menu List:")
        print("""
           1. List input files  
           2. File to load (can be obtained with list command)
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
                    i = i+1
        elif ans == "2":
            print("\n Enter the file number to load:")
            # throw the error if file not exist in the current folder/ or specified folder.
            # logs folder
            # stats folder
            start_time = datetime.now()

            # open the file
            # process the code
            # print the result

            end_time = datetime.now()
            time_diff = (end_time - start_time)
            execution_time = time_diff.total_seconds() * 1000
            # print(f"start time={start_time}, end time={end_time}, Total={round(execution_time, 4)} milliseconds")
            print(f"Total execution time={round(execution_time, 4)} milliseconds")
        elif ans == "3":
            name = input("\n PlCreate default input file")
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

        print('                                                     ')
        print('*____________________________________________________*')
        print('                                                     ')

        # wait for 2 seconds to show menu
        sleep(2)
        # screen_clear()


if __name__ == '__main__':
    main()
