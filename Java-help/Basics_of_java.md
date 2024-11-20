#Begining stuff 

```java
public class Main {}
```
class = container for one or more related functions (use classes to organise the code) give it a proper descriptive name
access modifiers= public or private

```java
public static void main(String[] args){}
```
void = return type (some return types return values and stuff and others dont)
main = name of the function, inside the paranthese, we add the parameters for the function
every java program should have at least one function (main)


#All THESE ARE PRIMITIVE TYPES
```java
byte age = 30;
long viewsCount = 3_123_456_789L;
```
Int can only take a certain amount of numbers, long is what u should use for very big numbers (add l at the end too). byte is what u use for smaller numbers
U can use underscores to make spaces to make the numbers readable
```java
float price =10.99F;
```
use another suffix bc java thinks its automatically a double


#Strings:
```java        
char letter = 'a';
```
char = 1 character only, str represents multiple.

```java
boolean isEligible = false;
```


#Reference Types
this part of the code prints out the current time and date
```java
Date now = new Date();
```
allocate memory for reference types
print to console
reference types have stuff to add on to em, primitives dont
```java     
System.out.println(now);
```

u can write sout and press  tab to get: System.out.println();

#POINTS?:

This makes 2 points, kinda work like lists in python (when one of the 2 changes, the other one changes too

```java
Point point1 = new Point(1,  1);
Point point2 = point1;
point1.x = 2;
System.out.println(point2);
```
String Stuff:
```java
String message = "Hello world" + "!!";
String lolsies = " lols";
```
or this works too:
```java
 String message1 = new String("Hello world");
```

```java
System.out.println(message.startsWith("!!"));
```
message.endswith("...") also works and so do other things after the dot. message.length() gives the number of characters.  message.indexof() gives the position of the letter in the message. message.replace("x", "z") replaces the first w the 2nd.  message.toLowerCase() makes message lower case toUpperCase works the same but opposite
        
```java
message.trim 
```
removes the whitespace
none of these change the originale string, they just make a change to a new string
