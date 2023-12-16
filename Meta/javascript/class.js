const bicycle = {
  bell: function () {
    return "Ring, ring! Watch out, please!";
  },
};
const door = {
  bell: function () {
    return "Ring, ring! Come here, please!";
  },
};

function ringTheBell(thing) {
  console.log(thing.bell());
}

function ringTheBell(thing) {
  console.log(thing.bell());
}

ringTheBell(bicycle); // Ring, ring! Watch out, please!
ringTheBell(door); // "Ring, ring! Come here, please!"

"abc".concat("def"); // 'abcdef'
["abc"].concat(["def"]); // ['abc', 'def']
["abc"] + ["def"]; // ["abcdef"]

class Bird {
  useWings() {
    console.log("Flying!");
  }
}
class Eagle extends Bird {
  useWings() {
    super.useWings();
    console.log("Barely flapping!");
  }
}
class Penguin extends Bird {
  useWings() {
    console.log("Diving!");
  }
}
var baldEagle = new Eagle();
var kingPenguin = new Penguin();
baldEagle.useWings(); // "Flying! Barely flapping!"
kingPenguin.useWings(); // "Diving!"

class Animal {
  constructor(classification, sound, legs, name) {
    this.classification = classification;
    this.sound = sound;
    this.legs = legs;
    this.name = name;
  }
}

class Dog extends Animal {}

let bingo = new Dog("Dog", "Bark", 4, "Bingo");

console.log(bingo);

today_date = new Date();
console.log(today_date);

function Icecream(flavor) {
  this.flavor = flavor;
  this.meltIt = function () {
    console.log(`The ${this.flavor} icecream has melted`);
  };
}

let kiwiIcecream = new Icecream("kiwi");
let appleIcecream = new Icecream("apple");
kiwiIcecream; // --> Icecream {flavor: 'kiwi', meltIt: ƒ}
appleIcecream; // --> Icecream {flavor: 'apple', meltIt: ƒ}

/*
new Date();
new Error();
new Map();
new Promise();
new Set();
new WeakSet();
new WeakMap();
*/
