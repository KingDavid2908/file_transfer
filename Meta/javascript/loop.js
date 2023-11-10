// Wrote a code for countdown for New year
for (var i = 10; i > 0; i--) {
    console.log("Countdown:", i);
}
console.log("Happy New Year!");

// Wrote a code to output the sum of the first n numbers
var sum = 0;
var n = 10;
var i = 0;
while (i <= n) {
    sum += i;
    i += 1;
}
console.log(sum);

// Nested For loop
for (var x = 1; x < 6; x++) {
    console.log(x, "times table");
    for (var y = 1; y < 13; y++) {
        console.log(y + ".", x, "x", y, "=", x*y);
    }
    console.log("");
}

// Looping through a string
var myName = "chukwumam";
for (var i = 0; i < myName.length; i++) {
    console.log(myName[i])
}