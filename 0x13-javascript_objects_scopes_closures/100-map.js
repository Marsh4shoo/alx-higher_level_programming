#!/usr/bin/node
const originalList = require('./100-data').list;

const multipliedList = originalList.map(function (number, index) {
  return number * index;
});

console.log("Original List:", originalList);
console.log("Multiplied List:", multipliedList);

