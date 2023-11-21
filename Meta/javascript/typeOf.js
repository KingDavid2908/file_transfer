// A Typeof operator is an operator that identifies the datatype of elements in Javascript
var car = {};
car.name = "Bugatti";
car.makeYear = 2002;
car.age = function (currentYear) {
  return currentYear - car.makeYear;
};
function sum(x, y) {
  return x + y;
}
newArray = [3, 5, 7, 11];
console.log(typeof "My name is Akachukwu");
console.log(typeof 23);
console.log(typeof true);
console.log(typeof undefined);
console.log(typeof null);
console.log(typeof car);
console.log(typeof car.age);
console.log(typeof car.age(2023));
console.log(car.age(2023));
console.log(typeof sum);
console.log(typeof newArray);
console.log(typeof newArray[1]);
