import random

random_numbers = open('ran_numbers.txt', 'w')

def main():

    writeFunction(getRandom())

def getRandom():
    qty_numbers = int(input('How many random numbers should be written to     the file? '))

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
