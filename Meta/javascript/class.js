const bicycle = {
  bell: function () {
    return "Ring, ring! Watch out, please!";
  },
};
const door = {
  bell() {
    return "Ring, ring! Come here, please!";
  },
};

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
  constructor(classification, sound, legs) {
    this.classification = classification;
    this.sound = sound;
    this.legs = legs;
  }
  sayName() {
    console.log(
      `My name is ${
        this.firstName
      }, and I am a ${this.classification.toLowerCase()}.`
    );
  }
  sayAge() {
    console.log(
      `The maximum age as a ${this.classification.toLowerCase()} I can live to is ${
        this.ageLimit
      } years old.`
    );
  }
  getSelf() {
    console.log(this);
  }
  getPrototype() {
    var proto = Object.getPrototypeOf(this);
    console.log(proto);
  }
}

class Dog extends Animal {
  constructor(firstName) {
    super();
    this.classification = "Dog";
    this.sound = "Bark";
    this.legs = 4;
    this.firstName = firstName;
    this.ageLimit = 10;
  }
}

class Birds extends Animal {
  constructor(classification, sound, firstName) {
    super(classification, sound);
    this.legs = 2;
    this.firstName = firstName;
  }
}

let cat = new Animal("Cat", "meow", 4);
let bingo = new Dog("Bingo");
let john = new Birds("Parrot", "talk", "John");

bingo.sayName();
bingo.sayAge();
bingo.getSelf();
cat.getSelf();
cat.getPrototype();
john.getSelf();
john.getPrototype();

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

class Train {
  constructor(color, lightsOn) {
    this.color = color;
    this.lightsOn = lightsOn;
  }
  toggleLights() {
    this.lightsOn = !this.lightsOn;
  }
  lightsStatus() {
    console.log("Lights on?", this.lightsOn);
  }
  getSelf() {
    console.log(this);
  }
  getPrototype() {
    var proto = Object.getPrototypeOf(this);
    console.log(proto);
  }
}

class HighSpeedTrain extends Train {
  constructor(passengers, highSpeedOn, color, lightsOn) {
    super(color, lightsOn);
    this.passengers = passengers;
    this.highSpeedOn = highSpeedOn;
  }
  toggleHighSpeed() {
    this.highSpeedOn = !this.highSpeedOn;
    console.log("High speed status:", this.highSpeedOn);
  }
  toggleLights() {
    super.toggleLights();
    super.lightsStatus();
    console.log("Lights are 100% operational.");
  }
}

var myFirstTrain = new Train("red", false);
console.log(myFirstTrain); // Train {color: 'red', lightsOn: false}
var mySecondTrain = new Train("blue", false);
var myThirdTrain = new Train("blue", false);

var train4 = new Train("red", false);
train4.toggleLights(); // undefined
train4.lightsStatus(); // Lights on? true
train4.getSelf(); // Train {color: 'red', lightsOn: true}
train4.getPrototype(); // {constructor: f, toggleLights: f, ligthsStatus: f, getSelf: f, getPrototype: f}

var train5 = new Train("blue", false);
var highSpeed1 = new HighSpeedTrain(200, false, "green", false);

train5.toggleLights(); // undefined
train5.lightsStatus(); // Lights on? true
highSpeed1.toggleLights(); // Lights on? true, Lights are 100% operational.

train5.getPrototype(); // {constructor: ƒ, toggleLights: ƒ, lightsStatus: ƒ, getSelf: ƒ, getPrototype: ƒ}
highSpeed1.getPrototype(); // Train {constructor: ƒ, toggleHighSpeed: ƒ, toggleLights: ƒ}

HighSpeedTrain.prototype.__proto__;

class StationaryBike {
  constructor(position, gears) {
    this.position = position;
    this.gears = gears;
  }
}

class Treadmill {
  constructor(position, modes) {
    this.position = position;
    this.modes = modes;
  }
}

class Gym {
  constructor(openHrs, stationaryBikePos, treadmillPos) {
    this.openHrs = openHrs;
    this.stationaryBike = new StationaryBike(stationaryBikePos, 8);
    this.treadmill = new Treadmill(treadmillPos, 5);
  }
}

var boxingGym = new Gym("7-22", "right corner", "left corner");

console.log(boxingGym.openHrs); //
console.log(boxingGym.stationaryBike); //
console.log(boxingGym.treadmill); //
