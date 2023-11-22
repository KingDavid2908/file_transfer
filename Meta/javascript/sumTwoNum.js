function addTwoNums(a, b) {
  try {
    if (typeof a != "number") {
      throw new ReferenceError("the first argument is not a number");
    } else if (typeof b != "number") {
      throw new ReferenceError("the second argument is not a number");
    } else {
      return a + b;
    }
  } catch (err) {
    return "Error!", err;
  }
}
addTwoNums(5, 5);

console.log(addTwoNums(2, 3));
console.log(addTwoNums(2, "3"));
console.log(addTwoNums("2", "3"));
