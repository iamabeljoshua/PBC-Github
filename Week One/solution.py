
# SOLUTION TO EXERCISE ONE

'''

QUESTION: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5 
between 2000 and 3200 (both included).


EXPLANATION:

There are many ways that this problem can be solved. 
If you're an intermediate or close to intermediate level coder, you should be able to come up with two solutions (if not, don't beat yourself up, 
it's part of the journey to not understand how everything works when you're just starting out)


This exercise isn't a tricky one (compared to the third excersise) and it's pretty simple to solve.
Any python coder that understands loops, range function and basic modulo maths 
should be able to come up with a solution to this problem.


One way to solve this problem is to go through the sets of integers between the start number(2000)
and the end number (3200) and check if the interger is a multiple of 7 but not a multiple of 5. 

'''


start = 2000  # start number

end = 3200  # end number

# our list of numbers that are multiple of 7 but aren't multiple of 5. 
# We will fill this list up as we loop through the sets of integers between start number and end number.
listofnumbers = []

for n in range(start, end+1):
    if n % 7 == 0 and n % 5 != 0:  # if number is a multiple of 7 but not a multiple of 5
        # we will append the number to our list of numbers.
        listofnumbers.append(n)

print(listofnumbers, end="\n")



# SOLUTION TO EXERCISE TWO

'''
QUESTION:  Write a program that accepts a sentence and calculates the number of letters and digits. 
Suppose the following input is supplied to the program:

hello world! 123

Then, the output should be:

LETTERS 10

DIGITS 3


EXPLANATION:

The second exercise is similar to the first one. We will simply loop through the characters in the input string and 
check if it's an alphabetic character (letter) or just a number (digit).

If you don't know what looping is about, I advice you go give that a read.

'''

sentence = input("Hi, go ahead and give me an input: ") #capture input from the user

'''
Once we've captured input from the user, we can go ahead and loop through the charactors of the input and do our thing.

Looping through characters of a string is as easy as looping through elements of a list. Because, string in python is an iterable.
(Iterable means we can iterate or loop through it. )
'''

digitscount = 0 # variable holding the number of digits

letterscount = 0 # variable holding the number of alphabetic characters (letters)

for char in sentence:  

    if char.isalpha(): # if this is an alphabetic character
        letterscount += 1 

    elif char.isdigit(): #if this is a digit
        digitscount += 1

print("DIGITS: ", digitscount)

print("LETTERS: ", letterscount, end="\n")



#SOLUTION TO EXERCISE THREE

''' 
QUESTION: This exercise is a codility test question. We are to find the binary gap of any input number.
If you don't understand what binary gap is all about, check out: https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
for the full explanation of this question.


This exercise is pretty tricky but simple to solve. First thing we have to do is to understand the question, the second is
to come up with a solution. If you like, you can write down the psuedocode of your solution before implementing it.

1. Get number from the user and convert to binary

2. Strip out (remove) every zero digits at the start and end of the binary representation of the number if present.

3. Seperate or split out all the sequences of zeros enclosed by 1. Checkout the test question if you don't understand

4. Find the count of the longest running zero sequence

5. Return the count

Nice, we've come up with simple steps to follow for our solution. All we have to do now is to implement it.

'''

number = int(input("Enter any integer number: ")) # Grab an input from the number

binaryNumber = bin(number) # Convert the input to binary.

binaryNumber = binaryNumber[2:] # In python, when you convert a number to binary, it prepends the result with 0b, we have to get rid of the '0b' '

binaryNumber = binaryNumber.strip("0") #We strip out every zero digits at both end of the binary string

sequence  = binaryNumber.split("1") # Here we split the sequences of zero out by using 1 as a delimeter

binaryGapSequence =  max(sequence) # We find the max (longest running zero-sequence) from the list

binaryGap = len(binaryGapSequence) # Find the length of the string holding the longest zero-sequence

print("Binary gap is: ", binaryGap)


'''

If you don't understand the solution to the third exercise, don't worry. You will, if you keep learning
and keep exploring. If you've come this far and you're living in the year 2020 and you're not a member of
Python Book Club, be sure to DM me on twitter (https://twitter.com/iamabeljoshua) and I will send you an invitation link
to our group where you'll find super-friendly python coders learning and sharing ideas daily. 

I promise you'll find the group to be an excellent learning community.

'''