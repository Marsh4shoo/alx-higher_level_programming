#!/usr/bin/node
class CustomRectangle {
  constructor(width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print() {
    if (!this.width || !this.height) return;

    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += 'X';
      }
      console.log(line);
    }
  }

  rotate() {
    if (!this.width || !this.height) return;
    
    [this.width, this.height] = [this.height, this.width];
  }

  double() {
    if (!this.width || !this.height) return;

    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = CustomRectangle;

