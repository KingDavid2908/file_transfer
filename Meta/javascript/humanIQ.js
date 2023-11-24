var human = {
  iq: 50,
  checkiq: function () {
    if (this.iq <= 0) {
      return "Fool";
    } else if (this.iq > 0 && this.iq < 30) {
      return "Dull";
    } else if (this.iq >= 30 && this.iq <= 70) {
      return "Average";
    } else if (this.iq > 70 && this.iq < 100) {
      return "Smart";
    } else {
      return "Genius";
    }
  },
  read: function () {
    this.iq += 10;
  },
  study: function () {
    this.iq += 30;
  },
  play: function () {
    this.iq -= 10;
  },
  joker: function () {
    this.iq -= 30;
  },
};

human.study();
console.log(human.checkiq());
human.study();
console.log(human.checkiq());
human.play();
console.log(human.checkiq());
human.joker();
console.log(human.checkiq());
human.joker();
console.log(human.checkiq());
human.joker();
console.log(human.checkiq());
human.read();
console.log(human.checkiq());
human.joker();
console.log(human.checkiq());
