function sumTwoNums(x, y) {
  datatype = typeof x;
  if (typeof y == datatype) {
    return x + y;
  } else {
    return "The inputs should only be numbers";
  }
}

console.log(sumTwoNums(2, 3));
console.log(sumTwoNums(2, "3"));
console.log(sumTwoNums("2", "3"));
