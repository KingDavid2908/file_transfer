function matchInString(regexp, string) {
  return string.match(regexp);
}

console.log(matchInString(/a/, "my name is david"));
