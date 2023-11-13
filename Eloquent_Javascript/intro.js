function sumRangeOfValues(startValue, endValue) {
  var sum = 0;
  for (var x = startValue; x <= endValue; x++) {
    sum += x;
  }
  return sum;
}

console.log(sumRangeOfValues(1, 10));
