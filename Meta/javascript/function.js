function checkSalary(age) {
  var salary = "wage";
  if (age <= 18) {
    salary = "allowance";
  } else if (age >= 60) {
    salary = "pension";
  }
  return "If a person is " + age + ", the person is paid " + salary + ".";
}

console.log(checkSalary(30));

function lengthOfArray(array) {
  var x = 0;
  var y = 1;
  while (x < y) {
    if (array[0] == undefined) {
      return 0;
    }
    if (array[y] == undefined && array[x] != undefined) {
      return y;
    } else if (array[y] == undefined && array[x] != undefined) {
      x -= 1;
      y -= 1;
    } else if (array[y] != undefined && array[x] != undefined) {
      x += 1;
      y += 1;
    }
  }
}

console.log(lengthOfArray(["david", "boy", "girl", "akachukwu", "beautiful"]));

function range(start = 0, end, step = 1) {
  var newArray = [];
  for (var x = start; x < end; x += step) {
    newArray = newArray.concat([x]);
  }
  return newArray;
}

console.log(range(0, 5, 2));

function sum(array) {
  var sum = 0;
  for (var x = 0; x < array.length; x++) {
    sum += array[x];
  }
  return sum;
}
console.log(sum(range(1, 5)));
