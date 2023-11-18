#!/usr/bin/node
class CustomRectangle {
  constructor(width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  printRectangle() {
    if (!this.width || !this.height) return;
    
    for (let row = 0; row < this.height; row++) {
      let line = '';
      for (let col = 0; col < this.width; col++) {
        line += 'X';
      }
      console.log(line);
    }
  }
}

module.exports = CustomRectangle;

