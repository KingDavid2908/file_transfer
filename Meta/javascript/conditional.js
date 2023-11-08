// A conditional that checks whether a number is positive, negative or neither
var x = 1;
if (x > 0) {
    console.log("x is a positive number");
}
else if (x < 0) {
    console.log("x is a negative number");
}
else {
    console.log("x is neither positive or negative");
}

// A switch statement is best used instead of an if-else etatement when you have a lot of conditions to check.
var myName = "akachukwu";
switch(myName) {
    case "akachukwu":
        console.log(myName, "is my middle name.")
        break;
    case "chukwumam":
        console.log(myName, "is my first name.")
        break;
    case "david":
        console.log(myName, "is my last name.")
        break;
    default:
        console.log(myName, "is not part of my names.")
}