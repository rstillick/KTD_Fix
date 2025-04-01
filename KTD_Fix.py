import os
working_directory = "/home/roger/Documents/Hypack_Python/KTD_fix/"
ktd_file = "USACE_RTX_KTD_TX_South-Central-SPC-Zone_w-SP_16Dec2024.KTD"
path = working_directory + ktd_file
ktd_array = []

def load_ktd(path):
    try:
        with open(path, 'r') as in_file:
            for line in in_file.readlines():
                ktd_array.append(line.split())

    except IOError:
        print("Error in opening or reading file.")

def write_ktd(ktd_list):
    try:
        with open(working_directory + "ktd_out", 'w') as out_file:

            for line in ktd_list:
                out_file.write(" ".join(line) + "\n")

    except IOError:
        print("Error in opening or writing file.")

'''
This function enumerates over the nested list called "ktd_array.
sources: 
https://www.geeksforgeeks.org/iterate-over-a-list-of-lists-in-python/
https://realpython.com/python-enumerate/
i is for columns, and j is for rows. 

'''
def ktd_math(ktd_list):
    t_east = 0
    t_south = 0

    # set the loop to start at 2
    for i in range(3, len(ktd_list), 1):
        for j in range(3, len(ktd_list[i]), 1):
            if (ktd_list[i-1][j-1] == "999.99"):
                west = 0.00
                east = 0.00
                north = 0.00
                south = 0.00
                avg_ktd = 0.00
                # keep track of how many values are going to be used for the average
                tally = 0


                if (ktd_list[i-1][j-2] != "999.99"):
                    north = float(ktd_list[i-1][j-2])
                    print ("north: ", north)
                    tally += 1

                if (ktd_list[i][j-1] != "999.99"):
                    east = float(ktd_list[i][j-1])
                    print("east: ", east)
                    tally += 1
                    t_east +=1

                if (ktd_list[i-1][j] != "999.99"):
                    south = float(ktd_list[i-1][j])
                    print("south: ", south)
                    tally += 1
                    t_south +=1

                if (ktd_list[i-2][j-1] != "999.99"):
                    west = float(ktd_list[i-2][j-1])
                    print("west: ", west)
                    tally += 1

                # calculate the average of any real ktd values and replace
                if (tally > 0):
                    avg_ktd = str(round(((west + east + north + south) / float(tally)),2))
                    ktd_list[i-1][j-1] = avg_ktd

                    print("Tally: ", tally)
                    print("new ktd value: " + avg_ktd)
    print("tally South: ", t_south)
    print("tally East: ", t_east)

if __name__ == '__main__':
    load_ktd(path)

    ktd_math(ktd_array)

    write_ktd(ktd_array)


