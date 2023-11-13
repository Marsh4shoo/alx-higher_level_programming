#!/usr/bin/node
const squareSize = parseInt(process.argv[2]);

if (Number.isNaN(squareSize)) {
  console.log('Error: Please provide a valid size');
} else {
  for (let i = 0; i < squareSize; i++) {
    let row = '';
    for (let j = 0; j < squareSize; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
