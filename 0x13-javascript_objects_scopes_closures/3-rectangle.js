#!/usr/bin/node
class CustomRectangle {
  constructor (widthValue, heightValue) {
    if ((widthValue > 0) && (heightValue > 0)) {
      this.width = widthValue;
      this.height = heightValue;
    }
  }

  drawRectangle () {
    for (let row = 0; row < this.height; row++) {
      let rowString = '';
      for (let col = 0; col < this.width; col++) {
        rowString += 'X';
      }
      console.log(rowString);
    }
  }
}

module.exports = CustomRectangle;
