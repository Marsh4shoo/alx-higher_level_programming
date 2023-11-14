#!/usr/bin/node
class CustomShape {
  constructor (widthVal, heightVal) {
    if ((widthVal > 0) && (heightVal > 0)) {
      this.width = widthVal;
      this.height = heightVal;
    }
  }

  render () {
    for (let row = 0; row < this.height; row++) {
      let rowString = '';
      for (let col = 0; col < this.width; col++) {
        rowString += 'X';
      }
      console.log(rowString);
    }
  }

  rotateShape () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  scaleUp () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = CustomShape;
