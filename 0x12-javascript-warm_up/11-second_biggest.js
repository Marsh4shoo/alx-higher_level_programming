#!/usr/bin/node
function calculateFactorial(num) {
  if (Number.isNaN(num) || num === 1) {
    return 1;
  }
  return calculateFactorial(num - 1) * num;
}

const inputNumber = parseInt(process.argv[2]);
console.log('Factorial:', calculateFactorial(inputNumber));
