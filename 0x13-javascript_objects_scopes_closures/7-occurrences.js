#!/usr/bin/node
const ParentSquare = require('./my-square');

class CustomSquare extends ParentSquare {
  displayCharPrint (character) {
    if (character === undefined) {
      character = 'X';
    }
    for (let row = 0; row < this.height; row++) {
      let rowString = '';
      for (let col = 0; col < this.width; col++) {
        rowString += character;
      }
      console.log(rowString);
    }
  }
}

module.exports = CustomSquare;
