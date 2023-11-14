#!/usr/bin/node
const CustomRectangle = require('./my-rectangle');

class CustomSquare extends CustomRectangle {
  constructor (sideSize) {
    super(sideSize, sideSize);
  }
}

module.exports = CustomSquare;
