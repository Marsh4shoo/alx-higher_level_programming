#!/usr/bin/node
class CustomRectangle {
  constructor(width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }
}

module.exports = CustomRectangle;

