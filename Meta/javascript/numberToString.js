function numberToString(num) {
  if (typeof num == "number") {
    return num.toString();
  } else {
    throw new TypeError("Your input should be a number");
  }
}
