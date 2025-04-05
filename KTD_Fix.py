import os
working_directory = "/home/roger/Documents/Hypack_Python/KTD_fix/"
ktd_file = "USACE_RTX_KTD_TX_South-Central-SPC-Zone_w-SP_16Dec2024.KTD"
path = working_directory + ktd_file
ktd_array = []

'''
Loads in the KTD file line by line and writing the contents to an array.
'''
def load_ktd(path):
    try:
        with open(path, 'r') as in_file:
            for line in in_file.readlines():
                ktd_array.append(line.split())

    except IOError:
        print("Error in opening or reading file.")

'''
Creates a file with the new KTD values. Named the same
as the working file, but has the suffix "_out". 
'''
def write_ktd(ktd_array, path):
    out_path = path.replace(".KTD", "_out.KTD")

    try:
        with open(out_path, 'w') as out_file:

            for line in ktd_array:
                out_file.write(" ".join(line) + "\n")

        print("write successful")

    except IOError:
        print("Error in opening or writing file.")

'''
loops through the ktd file and marks each point that has no
usable KTD values next to it. The keeps the interpolations 
restricted to the localized values. 
'''
def assign_weights(ktd_array):
    null_weight = "0"

    for i in range(3, len(ktd_array), 1):
        for j in range(3, len(ktd_array[i]), 1):
            tally = 0

            if (ktd_array[i-1][j-1] == "999.99"
                or ktd_array[i-1][j-1] == "0"):

                # North
                if (ktd_array[i - 1][j - 2] == "999.99"
                    or ktd_array[i - 1][j - 2] == "0"):
                    tally += 1
                # East
                if (ktd_array[i][j - 1] == "999.99"
                    or ktd_array[i][j - 1] == "0"):
                    tally += 1
                # South
                if (ktd_array[i - 1][j] == "999.99"
                    or ktd_array[i - 1][j] == "0"):
                    tally += 1
                # West
                if (ktd_array[i - 2][j - 1] == "999.99"
                    or ktd_array[i - 2][j - 1] == "0"):
                    tally += 1

                if tally == 4:
                    ktd_array[i-1][j-1] = null_weight




'''
This function enumerates over the nested list called "ktd_array.
sources: 
https://www.geeksforgeeks.org/iterate-over-a-list-of-lists-in-python/
https://realpython.com/python-enumerate/
i is for columns, and j is for rows. 
'''
def ktd_compute(ktd_array):
    t_north = 0
    t_east = 0
    t_south = 0
    t_west = 0

    # set the loop to start at 2
    for i in range(3, len(ktd_array), 1):
        for j in range(3, len(ktd_array[i]), 1):
            if (ktd_array[i-1][j-1] == "999.99"):
                west = 0.00
                east = 0.00
                north = 0.00
                south = 0.00
                avg_ktd = 0.00
                # keep track of how many values are going to be used for the average
                tally = 0

                # North
                if (ktd_array[i-1][j-2] != "999.99"):
                    if (ktd_array[i-1][j-2] != "0"):
                        north = float(ktd_array[i-1][j-2])
                        print ("north: ", north)
                        tally += 1
                        t_north += 1
                # East
                if (ktd_array[i][j-1] != "999.99"):
                    if (ktd_array[i][j-1] != "0"):
                        east = float(ktd_array[i][j-1])
                        print("east: ", east)
                        tally += 1
                        t_east += 1

                # South
                if (ktd_array[i-1][j] != "999.99"):
                    if (ktd_array[i - 1][j] != "0"):
                        south = float(ktd_array[i-1][j])
                        print("south: ", south)
                        tally += 1
                        t_south += 1

                # West
                if (ktd_array[i-2][j-1] != "999.99"):
                    if (ktd_array[i-2][j-1] != "0"):
                        west = float(ktd_array[i-2][j-1])
                        print("west: ", west)
                        tally += 1
                        t_west += 1

                # calculate the average of any real ktd values and replace
                if (tally > 0):
                    avg_ktd = str(round(((west + east + north + south) / float(tally)),2))
                    ktd_array[i-1][j-1] = avg_ktd

                    print("Tally: ", tally)
                    print("new ktd value: " + avg_ktd)

    print("tally North: ", t_north)
    print("tally South: ", t_south)
    print("tally East: ", t_east)
    print("tally West: ", t_west)

'''
Loop through the array and replace any alone "0" values with "999.99" 
'''
def ktd_normalize(ktd_array):
    for i in range(3, len(ktd_array), 1):
        for j in range(3, len(ktd_array[i]), 1):
            if (ktd_array[i - 1][j - 1] == "0"):
                ktd_array[i - 1][j - 1] = "999.99"

if __name__ == '__main__':
    load_ktd(path)
    assign_weights(ktd_array)
    ktd_compute(ktd_array)
    ktd_normalize(ktd_array)
    write_ktd(ktd_array, path)


