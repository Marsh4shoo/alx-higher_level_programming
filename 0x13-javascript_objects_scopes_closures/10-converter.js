#!/usr/bin/node

function createConverter(base) {
  return function convertNumber(num) {
    return num.toString(base);
  };
}

exports.converter = createConverter;

