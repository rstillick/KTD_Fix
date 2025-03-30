Python script that reads in a Hypack KTD file and replaces values that have 999.99 with the average of the surrounding values that are not 999.99. The contents of the ktd file is stored in a two dimensional list. A nested for loop is used to look at each ktd value in the file. If a 999.99 is present, then the program will look for the adjacent values at each cardinal dircetion, and then use any of the values to compute an average to replace the 999.99 with.

Time Complextiy
  The most time complex operation in the script are the two nested loops, which are approximately the same siz, which is quatdratic time complexity O(n^2). 
Space Complexity
  The ktd_array store every line and every ktd value as an element in a 2d list. This is O(nm) space complexity. 
  
TODO
Need to figure out a way to keep the values from propogating too many spaces from the known values. One simple solution was to calculate a replacement number if there were two or more adjacent values. When using only one value, i.e., the 999.99 value is surrounded by other 999.99 values for three of the four directions, then somehow all the 999.99 values in the whole file were replaced. 
I think if I assign a weight to each value, then I can tell which 999.99 values are completly surrounding by other 999.99 values and stop those values from being updated. This would required two passes throught the nested for loops. The first pass would use the same logic from the ktd_math method, but instead of calculating values to replace 999.99 values, it would assign a weight of 0 to the value if it is surrounded by 999.99 in all cardinal dirctions. This would require a means of storing the weight, possibly a dictionary. 

This was a Sunday afternoon project for the fun of it. 
