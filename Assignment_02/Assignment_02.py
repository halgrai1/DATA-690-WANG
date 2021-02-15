# welcome message + instructions
print("Please Enter 10 Integers to Calculate: \n Minimum, Maximum, \n Mean , Range, \n Variance, and Standard Deviation")
list1= []
# while loop to prompt user
# until all 10 integers are entered
# based on the length of the list
# will not stop prompting until 10
while len(list1)<10:
    try:
        user_input = int(input("Please enter an integer:")) 
    # adding each new item
    #list is not appended unless it's an integer 
        list1.append(user_input) 
        print(f"You have entered {len(list1)} integers:",user_input)
    except:
       print("This is not an integer. Please try again.")
print("The 10 integers you entered are:",list1)

#order the list with .sort()
list1.sort()
print("The MINIMUM is:", list1[0])
# to refer to the largest in the sorted list
# use the length of the list -1
print("The MAXIMUM is:", list1[len(list1)-1])

# create a new variable range
# subtract max from min
range1 = list1[len(list1)-1] - list1[0]
print ("The RANGE is:", range1)

# mean i.e. average
# create a new variable
avg = sum(list1) / len(list1)
print("The MEAN is:", avg)

#variance
var = sum((x-avg)**2 for x in list1) / len(list1)
print("The VARIANCE is:", var)

# standard deviation
# square root of var
std = var**0.5
print("The STANDARD DEVIATION:", std)