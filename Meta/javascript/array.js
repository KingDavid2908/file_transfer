var emptyArray = [];

var phoneArray = ["Apple", "Samsung", "Tecno", "Infinix", "Huawei"];

for (var x = 0; x < phoneArray.length; x++) {
  console.log(phoneArray[x]);
}

var pcArray = ["Dell", "Lenovo", "HP", "Apple"];
var gadgetArray = phoneArray.concat(pcArray);
gadgetArray.pop();
console.log(gadgetArray);
