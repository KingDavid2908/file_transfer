console.log(Math.PI); // Maths constant for pie
console.log(Math.E); // Maths constant for euler constant
console.log(Math.LN2); // Maths constant for the natural logarithm of 2
console.log(Math.ceil(23.56)); // Maths method to round up to the nearest whole number
console.log(Math.floor(23.56)); // Maths method to round down to the nearest whole number
console.log(Math.round(23.56)); // Maths method to round to the nearest whole number
console.log(Math.round(23.46));
console.log(Math.trunc(23.56)); // Maths method to trim the decimal leaving only the integers
console.log(Math.pow(2, 5));
console.log(Math.sqrt(36));
console.log(Math.cbrt(216));
console.log(Math.abs(-23));
console.log(Math.log(4));
console.log(Math.log2(4));
console.log(Math.log10(4));
console.log(Math.min(1, 23, 92));
console.log(Math.max(1, 23, 92));
console.log(Math.sin(Math.PI), Math.cos(90), Math.tan(10));

// Want to create a function to perform an action based on a result
function randomAction() {
  randomVariable = Math.random();
  randomVariable = Math.round(randomVariable * 10);
  console.log(randomVariable);
  if (randomVariable < 5) {
    return false;
  } else {
    return true;
  }
}

console.log("Is the random number greater than 4:", randomAction());

function createRandomArray() {
  var randomArray = [];
  for (var x = 0; x < 5; x++) {
    randomArray.push(Math.round(Math.random() * 10));
  }
  console.log(randomArray);
  return randomArray;
}

function maxRandomArray(array) {
  return array.reduce((a, b) => Math.max(a, b));
}

function minRandomArray(array) {
  return array.reduce((a, b) => Math.min(a, b));
}

function createAndAnalyseArray() {
  newArray = createRandomArray();
  return (
    "The min no from the array is " +
    minRandomArray(newArray) +
    " and the max no is " +
    maxRandomArray(newArray)
  );
}

console.log(createAndAnalyseArray());
