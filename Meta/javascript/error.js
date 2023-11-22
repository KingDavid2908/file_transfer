try {
  throw new Error("I created my own error");
} catch (err) {
  console.log(err);
}
console.log("This line should run");

// syntax error cannot be caught using the try-catch block.
