#   Given an array of integers, find the sum of its elements.

##### ##### ##### #####

#   A solution using a built in python method.
#   Reference python docs for details.

def solutionOne(integer_array):
    return sum(integer_array)

##### ##### ##### #####

#   An iterative solution.
#   O(n).  n is the length of the input array.

def solutionTwo(integer_array):
    array_sum = 0
    for integer in integer_array:
        array_sum += integer
    return array_sum
    
##### ##### ##### #####

#   A recursive solution.
#   O(n).  n is the length of the input array.

def solutionThree(integer_array):
    if len(integer_array) == 1:
        return integer_array[0]
    else:
        return integer_array.pop() + solutionThree(integer_array)
    
##### ##### ##### #####

def test():

    border = '##### ##### ##### #####'

    sample_array_one = [1,2,3]
    sa1_expected = 6

    s1 = solutionOne(sample_array_one)
    s2 = solutionTwo(sample_array_one)
    s3 = solutionThree(sample_array_one)

    print()
    print(border)
    print()

    print('Solution One Result: ' + str(s1))
    print('Expected Result: ' + str(sa1_expected))

    print()
    print(border)
    print()

    print('Solution Two Result: ' + str(s2))
    print('Expected Result: ' + str(sa1_expected))

    print()
    print(border)
    print()

    print('Solution Three Result: ' + str(s3))
    print('Expected Result: ' + str(sa1_expected))

    print()
    print(border)
    print()

    return None
