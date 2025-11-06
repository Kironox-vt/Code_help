Console.ReadKey() = when a key is typed in console it detects and thats it
Console.WriteLine() = writes something in console

variables:
u need to tell the program what type you want to store (string, integer, float, boolean,...)
double is float but w more decimals
using "var" also works if u dont know what type it is going to be...
ex: (type) (name of variable) = (value)
 or: int age = 17;

 converting a type to another type:
 Convert.To(type)(Value)
 ex: 
 int num1 (declaring an empty variable)
 num1 = Convert.ToInt32(Console.ReadLine())

 this coverts the string from console to an integer


if statements:
if(condition){

}

ex:
if (age == 13){
    Console.WriteLine("Your almost old enough to take over the world")
}
else if (age == 14){
    Console.WriteLine("Your old enough to take over the world")
}
else{
    Console.WriteLine("aight cool, cya")
}

diff types of conditions:
==: is equal to
!=: is not equal to
<: less than
>: greater than
<=: less than or equal to
>=: greater than or equal to

if u want multiple conditions in the same if statement:
&&: means and
||: means or