# Python help page

Python is a case sensitive coding language, please be careful about that.

To write comments in python, you use # 

## Types

There are multiple types in python:

First of all, the booleans or bool for short, these take only 2 values, true or false:

```python
#This is how you write true in python
True
```

```python
#This is how you write false in python
False
```

```python
#in python you will write bool to convert things to boolean values for example a text or a string will become a boolean if you do the following things (only works if the word is True or False)
bool("True")
```

Then there are strings or str for short, these are text elements that can be shown in console or are a user's input via the console:

```python
"My name is Kironox"
```
That is a string, it is introduced an ended with "

You can also convert from any of the other types to string value by using str():

```python
str(True)
```

This will convert the boolean True into a string : "True" 

Then there are integers or int for short, these are only numbers.

You can only convert strings into numbers and only if they are numbers by using int():

```python
int("102")
```

This will convert the string into a number

And then there are floats which are numbers with decimals: 

```python
33.13
```

You can also convert strings and integers into floats float():

```python
float(33)
float("33")
```

both will return the number 33.0

## Showing something in console

```python
print()
```

Each print is printed on a new line of the console

## Variables

variables are very simple, imagine putting an object in a box and that the box can only contain 1 object, if you try to add a new/ other object into the object, it will change to the new object

```python
x = 1
x = 2
```

x will be equal to 2 in the end

```python
x = 1
x = x + 2
y= x
x =5
```

x will be equal to 5 and y will be equal to 3

variables can take any type inside of them.

Only integers and floats can use mathematical equations like the times, the plus, the minus and the divide

```python
#the plus in python
+
#the minus in python
-
#the times in python
*
#the divide in python
/
#the modulo in python
%
```

The strings can use the times sign but only to display the content n amount of times

```python
print("Hi, my name is Kironox" * 5)
```

This will print out the string 5 times in a row

## If statements

You can make your code do stuff on specific conditions

```python
if (condition):
    ...
```

You also have the possibility of making you code do something else if the condition is not true. In that case you use "else":

```python
if (condition):
    ...
else:
    ...
```

And the last thing you can do is putting a different condition if the first one isnt met using "elif" which means else if:

```python
if (condition):
    ...
elif:
    ...
else:
    ...
```

You can stack multiple conditions on each other using

```python
and
```
or

```python
or
```

example: 

```python
contrat = input("Quel contrat voulez-vous choisir? ")
if contrat == "Les 1" or contrat == "les 1" or contrat == "Les 2" or contrat == "les 2" or contrat == "Les 3" or contrat == "les 3" or contrat == "Les 4":
    print("Contract acccepted")
elif contrat == "nul":
    print("Contract is considered as nul, nothing will happen")
else:
    print("Contract not accepted")
```

## Loops

You can make loops via multiple ways.

An infinite loop:

```python
while True:
    ...
```

A loop that can can changed from infinite to end

```python
lols == 0
Continue = True
while Continue:
    if lols == 3:
        Continue = False
    lols += 1
```

You can also predetermine how long your loop will go for

```python
for i in range (x, y, z):
```
Definitions of variables above:
i: The name of a variable used for the loop (i will take the number of the turn it currently is)
x: The number at which the loop starts
y: The number where the loop ends
z: The interval in between each number the loop chooses

examples:

You can put one value in the loop, the maximum:

```python
for i in range (10):
    print(i)
```

This will print the number 0 to 9 because python will start the count at 0 and not at 1

You can put 2 values in the loop, the minimum and the maximum:

```python
for i in range (1, 10):
    print(i)
```

You will see the numbers 1 to 10 because we told it to start at 1 and not at 0

You can also put all 3 values:

```python
for i in range (2, 20, 2):
    print(i)
```

This will print the equal numbers from 2 to 20 as the step is set to 2

## Importing

```python
import (your import)
```

example:

```python
import random
```

## Functions:

### Defining ur function:

```python
def (function name) ([The paramaters you want in your function]):
```

example:

```python
def function (list):
```

### Returning a value from your function:
The values, variables and things that happen inside of your functions dont exist outside of the function so you need to return what you want to use from your function. You dont have to add in a return if there is nothing to return

```python
return (type, variable, ...)
```

example:
```python
return True
```
```python
return list
```

Full function example:

```python
def afficher_des(main):
    for main_des in range (len(main)):
        print("dés", main_des+1, "vaut", main[main_des])
    return
```