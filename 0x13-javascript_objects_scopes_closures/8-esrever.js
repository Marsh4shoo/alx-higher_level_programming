#!/usr/bin/node
exports.reverseList = function (array) {
  let lastIndex = array.length - 1;
  let firstIndex = 0;
  while ((lastIndex - firstIndex) > 0) {
    const temp = array[lastIndex];
    array[lastIndex] = array[firstIndex];
    array[firstIndex] = temp;
    firstIndex++;
    lastIndex--;
  }
  return array;
};
