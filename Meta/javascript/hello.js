// This is a single line comment
/*
This is a multiline comment
*/
// The next line can be used on chrome browser to add css to output
console.log("%cHello, World", "color: blue; font-size: 40px");
/*
The next two lines can be used to represent the same meaning. Would 
output: Hello there, world
*/
console.log("Hello", "there,", "world");
console.log("Hello " + "there, " + "world");
// Trying out variable assignment
var personName; // This is variable declaration
var personName = "David"; // This is variable assignment
var greeting = "Hello";
console.log(greeting, personName); // outputs "Hello David"
personName = "Akachukwu"; // This is reassignment and you don't need to
// use any initial keyword.
console.log(greeting, personName);
/* 
There are seven data types in Javascript:
1. String
2. Number
3. Boolean
4. Null
5. Undefined
6. BigInt
7. Symbol
*/
var fullName = "Chukwumam Akachukwu David"; // This is a string
var age = 21; // This is a number
console.log("My name is", fullName, "and I am", age, "years old.");
// Outputs: My name is Chukwumam Akachukwu David and I am 21 years old.
var handsome = true; // This is a boolean
var ugly = false; // This is a boolean
/*
Null means the absence of a value 
Undefined means a variable has not been assigned a value
*/
