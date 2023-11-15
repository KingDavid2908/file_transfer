// Creation of javascript object is similar to how to create dictionaries in python.

var human = {};
human.iq = 50;
human.lifetime = 80;
human.violence = 70;
human.creativity = 90;
human.health = 80;

var dolphin = {
  iq: 70,
  lifetime: 60,
  violence: 40,
  creativity: 70,
  health: 50,
};

var dog = {};
dog["iq"] = 20;
dog["lifetime"] = 10;
dog["violence"] = 90;
dog["creativity"] = 20;
dog["health"] = 10;

dolphin.health = 60;
console.log(human);
console.log(dolphin["creativity"]);
console.log(dog.iq);
keyArray = ["iq", "lifetime", "violence", "creativity", "health"];

for (var i = 0; i < keyArray.length; i++) {
  console.log(i + 1, ")", keyArray[i], ":", dolphin[keyArray[i]]);
}
