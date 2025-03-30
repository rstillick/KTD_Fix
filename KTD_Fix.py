import os
#from decimal import Decimal
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
source: https://www.geeksforgeeks.org/iterate-over-a-list-of-lists-in-python/

'''
def ktd_math(ktd_list):
    for i, inner_list in enumerate(ktd_list):
        for j, element in enumerate(inner_list):
            if (i > 0 and i < len(ktd_list)):
                if (element == "999.99"):
                    a = 0.00
                    b = 0.00
                    c = 0.00
                    d = 0.00
                    # keep track of how many values are going to be used for the average
                    tally = 0.0

                    if (j > 0 and inner_list[j-1] != "999.99"):
                        a = float(inner_list[j-1])
                        print ("a: ", a)
                        tally += 1.0

                    if (j > 0 and j+1 < len(inner_list)):
                        if (inner_list[j+1] != "999.99"):
                            b = float(inner_list[j+1])
                            print("b: ", b)
                            tally += 1.0

                    if (j > 0 and i > 1) and ktd_list[i - 1][j] != "999.99":
                        c = float(ktd_list[i - 1][j])
                        print("c: ", c)
                        tally += 1.0

                    if (j > 0 and i+1 < len(ktd_list)):
                        if (ktd_list[i+1][j] != "999.99") :
                            d = float(ktd_list[i+1][j])
                            print("d: ", d)
                            tally += 1.0

                    if (tally > 1):
                        element = str(round(((a+b+c+d) / tally),2))
                        ktd_list[i][j] = element

                        print("Tally: ", tally)
                        print("element: " + element)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    load_ktd(path)
    #print(ktd_array[1][111])
    ktd_math(ktd_array)

    write_ktd(ktd_array)


