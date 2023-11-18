#!/usr/bin/node
const CustomRectangle = require('./4-rectangle');

class Square extends CustomRectangle {
  constructor(size) {
    super(size, size);
  }
}

module.exports = Square;

