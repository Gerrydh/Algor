input_file = open('C:\\Users|\Desktop\\data.txt') 
for line in input_file:
    print line

print('Before: ', input_file)
insertion_sort(input_file)
print('After : ', input_file)
def insertion_sort(items):
    """ Implementation of insertion sort """
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1
