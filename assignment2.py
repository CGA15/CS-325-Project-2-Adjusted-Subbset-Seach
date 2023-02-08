'''
    This file contains the template for Assignment2.  For testing it, I will place it
    in a different directory, call the function <minimumimum_allowable_attendance_for_long_weekend>, 
    and check its output. So, you can add/remove  whatever you want to/from this file.  But, don't change the name
    of the file or the name/signature of the following function.
index
    Also, I will use <python3> to run this code.
'''
import math
import numpy as np

#Received Help on implementaition of the coding portion from Joshua Negreanu

def threeDaySubsets(groupsArr, output_file):
    maxArr = sum(groupsArr) #Variable to hold the sum of all the groups
    # create a 4D array to store potential day values
    daysArr = [[[[False for i in range(maxArr + 1)] for j in range(maxArr + 1)] for k in range(maxArr + 1)]for l in range(maxArr + 1)]
    # Start with the base case of having no groups so all days would be empty
    daysArr[0][0][0][0] = True
    # O(n)
    for index, i in enumerate(groupsArr):
        # O(nl)
        for a in range(maxArr): #day 1
            # O(nl)
            for b in range(maxArr): #day 2
                # O(nl)
                for c in range(maxArr): #day 3
                    if daysArr[index][a][b][c]:
                        daysArr[index + 1][a + i][b][c] = True #add i to day 1
                        daysArr[index + 1][a][b + i][c] = True #add i to day 2
                        daysArr[index + 1][a][b][c + i] = True #add i to day 3

    minimum = maxArr
    for a in range(maxArr):
        for b in range(maxArr):
            for c in range(maxArr):
                if daysArr[len(groupsArr)][a][b][c]:
                    minimum = min(max(a, b, c), minimum)

    print("smallest minimum group size found:" + str(minimum))
    output_file.write(str(minimum))





def minimumimum_allowable_attendance_for_long_weekend(input_file_path, output_file_path):
    '''
        This function will contain your code.  It wil read from the file <input_file_path>,
        and will write its output to the file <output_file_path>.
    '''
    #open files into varablies to be read and manipulated
    input_file = open(input_file_path, "r")
    output_file = open(output_file_path, "r+")
    output_file.truncate(0)



    #setup variables

    groupsArr = []
    i = 0

    for line in input_file:
        groupsArr = line.split(",")
    groupsArr = [int(i) for i in groupsArr]

    groupsArr.sort(reverse=True)
    threeDaySubsets(groupsArr, output_file)
    #close files
    input_file.close()
    output_file.close()

'''
    To test your function, you can uncomment the following command with the the input/output
    files paths that you want to read from/write to.
'''
minimumimum_allowable_attendance_for_long_weekend('input9.txt', 'output.txt')



