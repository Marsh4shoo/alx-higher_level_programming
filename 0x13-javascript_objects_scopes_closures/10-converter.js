#!/usr/bin/node

exports.baseConverter = function (inputBase) {
  return function (number) {
    return number.toString(inputBase);
  };
};
