function numToSignFigs(num, signFig) {
  try {
    return Number(num).toPrecision(signFig);
  } catch (e) {
    console.log("There was an error");
  }
}

console.log(numToSignFigs(197834, 4));
