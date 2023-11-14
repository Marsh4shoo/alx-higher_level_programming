#!/usr/bin/node
let counter = 0;

exports.logIncrement = function (value) {
  console.log(counter + ': ' + value);
  counter++;
};
