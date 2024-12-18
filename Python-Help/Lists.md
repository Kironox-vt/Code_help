# Python lists help page
Lists are variables that can keep multiple values.

## Declare lists
To declare a list, you need to name a variable and put brackets before putting in the values. To seperate the values, put a comma in between each value.
```python
List = [1, 3, 4, 5]
```

You can put different types of values in the same list.

```python
List = [1, 3, "peanuts", 3.3, True]
```
## Calling specific values in a list

Each value is assigned a position, 0 for the one on the far left and you at 1 each time the value is towards the right.

```python
List = [1, 3, "peanuts", 3.3, True]
```
In the code above, the value 1 corresponds to position 0; the value 3 corresponds to position 1, etc


With this in mind we will call for a specific value in the list. To ask for a specific value, you will put you variable's/list's name and the put parenthese, after that, you put the position of the value you want to have.

```python
List = [1, 3, "peanuts", 3.3, True]
print(List(2))
```
In this code, we declare a list and then we decide to print the value in position 2 which is "peanuts". In console, we will see the word peanuts appear.

## Adding a value to a list

It is really simple to add a variable to a list, all you need to do is use (variable name).append

```python
List = [1, 3, "peanuts", 3.3, True]
print(List)
List.append(304)
print(List)
```
This will declare the list, print the first version, add a new value to the end and then reprint the modified list with the new value

## Copying a list into another list

To copy a list into another list, you shouldnt do this:

```python
List = [1, 3, "peanuts", 3.3, True]
List2 = List
```
This will copy the list into the other list but it will link them together so if one of the values changes in one variable, it will also change in another variable.

Instead you will be asking for the length of the variable by using len()

```python
List = [1, 3, "peanuts", 3.3, True]
print(len(List))
```
This will return the amount of values in the list, so here it will say 5

With this in mind we will procede to the copying of a variable that is not linked. We will use a ranged loop to do this

```python
List = [1, 3, "peanuts", 3.3, True]
new_list = []
for i in range (len(List)):
    new_list.append(List[i])
print(new_list)
```

This will copy the list to a new list and then print it in console. You can now modify both lists without changing the other one.

## Dictionaries

These are a bit more complicated than normal lists, it is a list that has values inside of a specified name

A dictionary looks like this:

```python
List = {"Val_1" : 0, "Val_2" : "mep", "model" : "idk", "real" : False}
```
To declare a dictionary you need to put these brackets: {}, then inside you put the name of you the thing you want to define, after that put a colon. To seperate each defined variable put a comma.

### Modify dictionaries
To modify a value in a dictionary, put the name of the list, put normal brackets and then in quotation marks, the name of the value you want to change and then do just as if it is a normal variable

```python
List = {"Val_1" : 0, "Val_2" : "mep", "model" : "idk", "real" : False}
List["model"] = "The third one"
print(List["model"])
```

This will modify the model value to "the third one" and then print the model.

This is also how you add a new value to the dictionary.