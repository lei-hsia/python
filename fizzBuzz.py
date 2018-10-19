'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def main():
    # print("enter the number of test cases:")
    name = input()
    # print(name)
    # print("enter the all real numbers in this test:")
    nums = input()
    # print(nums)
    
    nums_int = []
    for n in nums.split():
        n = int(n)
        nums_int.append(n)
    
    print('1')
    print('2')
    print('Fizz')
    for num in range(1, 1+nums_int[-1]):
        string=''
        if num %15 == 0:
            string += 'FizzBuzz'
        elif num %3 == 0:
            string += 'Fizz'
        elif num %5 == 0:
            string += 'Buzz'
        else:
            string += str(num)
        print(string)
    
if __name__ == "__main__":
    main()