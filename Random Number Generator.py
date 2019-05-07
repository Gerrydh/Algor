# Ger Hanlon. April 2019. Generate random numbers and text file containing the numbers
# Source Code- https://stackoverflow.com/questions/43175324/python-random-number-file-writer


import random

random_numbers = open('ran_numbers.txt', 'w')

# execute program when ran in python
def main():

    writeFunction(getRandom())

def getRandom():
    
    # Enter the number of random integers to be generated
    qty_numbers = int(input('How many random numbers should be written to     the file? '))

    # append randomlyu generated numbers 1 and 15000
    nums = []
    for count in range (qty_numbers):
        nums.append(random.randint(1,15000))
    return nums

def writeFunction(a_list):
    random_nums = '\n'.join([str(x) for x in a_list])
    random_numbers.write(random_nums)
    random_numbers.close()
    print('Your list of random numbers have been written to the file named')
    print('ran_numbers.txt')

main()
