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
