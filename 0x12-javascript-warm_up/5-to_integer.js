#!/usr/bin/node
const inputNumber = Number(process.argv[2]);

if (isNaN(inputNumber)) {
  console.log('Invalid input: Not a number');
} else {
  console.log('My number: ' + inputNumber);
}
