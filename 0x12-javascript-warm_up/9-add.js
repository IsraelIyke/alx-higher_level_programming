#!/usr/bin/node
const alpha = Math.floor(Number(process.argv[2]));
const beta = Math.floor(Number(process.argv[3]));

function add(a, b) {
  if (isNaN(a)) {
    return b;
  } else if (isNaN(b)) {
    return a;
  } else {
    return a + b;
  }
}

console.log(add(alpha, beta));
