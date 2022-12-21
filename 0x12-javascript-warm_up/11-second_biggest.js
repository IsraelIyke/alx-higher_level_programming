#!/usr/bin/node
const arr = process.argv;
const newArray = [];
if (arr.length < 3 || arr.length === 3) {
  console.log(0);
} else {
  for (let i = 2; i < arr.length; i++) {
    newArray.push(Math.floor(Number(arr[i])));
  }
  const max = Math.max(...newArray);
  const largest = newArray.indexOf(max);
  newArray.pop(largest);
  const maxTwo = Math.max(...newArray);
  console.log(maxTwo);
}
