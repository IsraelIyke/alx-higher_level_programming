#!/usr/bin/node
const a = Math.floor(Number(process.argv[2]));
const b = Math.floor(Number(process.argv[3]));

if (isNaN(a)) {
  console.log("Missing");
} else if (isNaN(b)) {
  console.log("Missing");
} else {
  function add(a, b) {
    return a + b;
  }
}

console.log(add(a, b));
