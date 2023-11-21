var emptyArray = [];

var phoneArray = ["Apple", "Samsung", "Tecno", "Infinix", "Huawei"];

for (var x = 0; x < phoneArray.length; x++) {
  console.log(phoneArray[x]);
}

var pcArray = ["Dell", "Lenovo", "HP", "Apple"];
var gadgetArray = phoneArray.concat(pcArray);
console.log(gadgetArray.pop());
console.log(gadgetArray);

function convertArrayToString(array) {
  var string = "";
  var length = array.length;
  for (var i = 0; i < length; i++) {
    if (i == length - 1) {
      var newString = array[i] + ".";
      string = string.concat(newString);
    } else {
      var newString = array[i] + ", ";
      string = string.concat(newString);
    }
  }
  return string;
}

console.log("The array consists of", convertArrayToString(gadgetArray));
