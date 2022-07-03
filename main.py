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
record = arr.array('i', [0, 0, 0])  # x,y,f
total_jobs: int = 0
avg_time: float = 0
max_time: float = 0
max_time_name = ""
min_time: float = 0
min_time_name = ""

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
#                                   check_start_command
#   NORTH : 1, SOUTH: 2, EAST: 3, WEST: 4

def check_start_command(line):
    # print(f" check_start_command {line}")

    data = line.split(',')
    if len(data) == 3:
        v1 = int(data[0])
        v2 = int(data[1])
        v3 = str(data[2])
        v3 = v3.replace('\n', '', 1)

        record_x: int = 0
        record_y: int = 0
        record_f: int = 0

        # get 'x'
        if 0 <= v1:
            if v1 > 5:
                # print(f" oops  out of range x:{v1}, limit to 5 (max)")
                v1 = 5
            record_x = v1
            # print(f" true -1 rec:{record_x}{v1}- {record}")

        if 0 <= v2:
            if v2 > 5:
                # print(f" oops  out of range y:{v2}, limit to 5 (max)")
                v2 = 5
            record_y = v2
            # print(f" true -1 rec:{record_y}{v2}- {record}")

        # get 'f'
        if v3 == 'NORTH':
            record_f = 1
        elif v3 == 'SOUTH':
            record_f = 2
        elif v3 == 'EAST':
            record_f = 3
        elif v3 == 'WEST':
            record_f = 4
        else:
            # print(f" ignore :  false -3 {v3}- {record}")
            # print(f" invalid direction f:{v3} ")
            return False

        # update the record , only if x,y,f are valid
        record[0] = record_x
        record[1] = record_y
        record[2] = record_f

        return True
    else:
        return False


#############################################################################################
#                                   validate_start_command
#

def validate_start_command(dline):
    # print(f"validate_start_command called :: {line} ")
    index = 0

    if len(dline.strip()) <= 0:  # check for NULL
        return False
    line = dline  # assign and process

    data = line.split(' ')  # parse the header line
    # print(len(data))

    # check for the 'PLACE' command
    if len(data) > 0:
        if not data[0] == "PLACE":
            return False
        # else:
        # print(f" data[0] = {data[0]}")

    # if the first element is PLACE and the count ==2 return true
    if len(data) == 2:  # start of header has more than what its needed
        for char in data:
            index = index + 1
            # print(f" {index} = {char}")

        validate_ret = check_start_command(data[1])
        # print(f" validate_ret = {validate_ret}")

        if validate_ret:
            # print("valid header packet Received ")
            return True
        else:
            # print("NOT a valid header ")
            return False

    else:
        # print(" invalid - Start of Header")
        return False


#############################################################################################
#                                   check_other_command
#

def get_direction(line):
    direction = ""
    if line == 1:
        direction = "NORTH"
    elif line == 2:
        direction = "SOUTH"
    elif line == 3:
        direction = "EAST"
    elif line == 4:
        direction = "WEST"
    return direction


#############################################################################################
#                                   validate_other_command
#


def validate_other_command(dline):
    iv3 = 0
    iv2 = 0

    print(f"validate_other_command called {dline}")
    # print(f"len(dline.strip()) = {len(dline.strip())}")

    if len(dline.strip()) == 0:  # check for NULL
        # print(f"len(dline.strip()) = {len(dline.strip())}")
        return False

    line = dline  # assign and process

    data = line.split('\n')  # parse the header line
    # print(len(data))
    # print(data)
    # print(f" data[0] = {data[0]}")

    if data[0] == 'MOVE' or data[0] == 'LEFT' or data[0] == 'RIGHT' or data[0] == 'REPORT':
        if data[0] == 'MOVE':
            # print(f"[REPORT] {record}")
            if record[2] == 1:  # NORTH - y axis+
                record[1] = record[1] + 1
            elif record[2] == 2:  # SOUTH - y axis-
                record[1] = record[1] - 1
            elif record[2] == 3:  # EAST - x axis+
                record[0] = record[0] + 1
            elif record[2] == 4:  # WEST - x axis-
                record[0] = record[0] - 1
        elif data[0] == 'LEFT':  # LEFT direction
            if record[2] == 1:  # NORTH
                record[2] = 4  # (WEST)
            elif record[2] == 4:  # WEST
                record[2] = 2  # (SOUTH)
            elif record[2] == 2:  # SOUTH
                record[2] = 3  # (EAST)
            elif record[2] == 3:  # EAST
                record[2] = 1  # (NORTH)
        elif data[0] == 'RIGHT':  # RIGHT direction
            if record[2] == 1:  # NORTH
                record[2] = 3  # (EAST)
            elif record[2] == 3:  # EAST
                record[2] = 2  # (SOUTH)
            elif record[2] == 2:  # SOUTH
                record[2] = 4  # (WEST)
            elif record[2] == 4:  # WEST
                record[2] = 1  # (NORTH)
        elif data[0] == 'REPORT':
            print(f"Output: {record[0]},{record[1]},{get_direction(record[2])}")
            # print(f"[REPORT] {record}")
        else:
            return False

        # boundary limit
        if record[0] > 5:
            # print("oops... cant go any further")
            record[0] = 5
        if record[1] > 5:
            # print("oops... cant go any further")
            record[1] = 5
        if record[0] < 0:
            # print("mmm... cant go any further")
            record[0] = 0
        if record[1] < 0:
            # print("mmm... cant go any further")
            record[1] = 0

        # print(f"[REPORT] {record}")
        return True
    else:
        # print(f"validate_other_command invalid command {dline}")
        return False


#############################################################################################
#                                   main
#


def main():
    name: str = ""
    sec: int = 0
    sel: int = 0
    y: int = 0
    avg_time = 0
    min_time = 0
    max_time = 0

    filenames = []
    total_jobs = 0
    ans: str = "999"
    max_time_name: str = ""
    min_time_name: str = ""
    curr_file_name: str = ""

    # create folder - stats,logs
    # logs folder
    # stats folder

    while True:
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

            filenames.clear()
            for x in os.listdir(os.getcwd()):
                if x.endswith(".inp"):
                    filenames.append(x)
            filenames.sort()
            # print(f"filename = {filenames}")
            for x in filenames:
                print(f"({i}) {x} ")
                i = i + 1

        elif ans == "2":
            sel1 = input("\n Enter input file number to test :")
            sec = int(sel1) - 1
            sel = int(sec)
            totFiles = 0
            # print(f"-----------------> sel = {sel}")
            # throw the error if file not exist in the current folder/ or specified folder.
            # logs folder
            # stats folder
            start_time = datetime.now()
            # try:
            # load the file
            # read the first line and all the lines until you reach a valid start
            totFiles = len(filenames)
            if totFiles == 0 or sel >= totFiles:
                print(f"no input / invalid selection : {sel} total:{totFiles}")
                continue
            # print(f"------selected file -----------> filenames[{sel}]={filenames[sel]}")

            ##############################################
            # read lines to get the first valid start line
            ##############################################
            # step 1
            curr_file_name = filenames[sel]
            keyfile = open(filenames[sel])
            # keyfile = open("test3.inp")
            # keyfile = open("test3.inp")
            # keyfile = open("input4.inp")
            # keyfile = open("no-header.inp")
            # keyfile = open("invalid-input.inp")
            header_recd = False
            for line in keyfile:
                if not header_recd:
                    ret = validate_start_command(line)
                    if bool(ret):
                        header_recd = bool(ret)
                        # print(f" **** {line} ****  invalid first command")
                        # print()
                    # else:
                    #     print()
                    #     # print(f" xxxx {line} xxxx  is not a valid start packet ")
                    #     # print()
                else:
                    ret = validate_other_command(line)
                    if bool(ret):
                        # print(f" **** {line} ****  is a valid command")
                        print()
                    # else:
                    #     # print(f" xxxx {line} xxxx  is not a valid command packet ")
                    #     # print()
                    #     # print(f" [record]{record}")
                    #     print()

            if not header_recd:
                print()
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print(f"No valid first command found")
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print()
            # else:
            #     print()
            #     print("---------------------------------------------------")
            #     # print(f" [record]{record}")
            #     # print("---------------------------------------------------")
            #     # print()

            print("---------------------------------------------------")
            end_time = datetime.now()
            time_diff = (end_time - start_time)
            execution_time = time_diff.total_seconds() * 1000
            # print(f"start time={start_time}, end time={end_time}, Total={round(execution_time, 4)} milliseconds")
            print(f"Total execution time={round(execution_time, 4)} milliseconds")

            total_jobs = total_jobs + 1
            if total_jobs == 1:
                min_time: float = round(execution_time, 4)
                min_time_name = curr_file_name
                max_time: float = round(execution_time, 4)
                max_time_name = curr_file_name
            else:
                if round(execution_time, 4) < min_time:
                    min_time: float = round(execution_time, 4)
                    min_time_name = curr_file_name

                if round(execution_time, 4) > max_time:
                    max_time: float = round(execution_time, 4)
                    max_time_name = curr_file_name

            avg_time = (avg_time + execution_time) / total_jobs

        elif ans == "3":
            name = input("\n Please enter the name of input file :  ")
            fullname: str = name + ".inp"
            f = open(fullname, "w")
            f.write("# Add the commands, PLACE command is a valid first command")
            f.close()

        elif ans == "4":
            print(f"----------------")
            print(f"some cool Stats:")
            print(f"----------------")
            print(f"  Number of jobs run :{total_jobs}")
            print(f"  average time [ job exec time] : {round(avg_time, 4)}  milliseconds")
            print(f"Job execution times:")
            print(f"  maximum : {round(max_time, 4)}  milliseconds, input file name : {max_time_name}")
            print(f"  minimum : {round(min_time, 4)}  milliseconds, input file name : {min_time_name}")
        elif ans == "5":
            print("\n Goodbye")
            exit(0)
        elif ans == "":
            print("\n Can't be empty")

        print('                                                     ')
        print('                                                     ')
        print('*****************************************************')
        print(' *                                                  *')
        print('  *                                                *')
        print(' *                                                  *')
        print('*____________________________________________________*')
        print('                                                     ')
    # wait to show menu
    sleep(1)


#############################################################################################
#                                   Begin
#
if __name__ == '__main__':
    main()
