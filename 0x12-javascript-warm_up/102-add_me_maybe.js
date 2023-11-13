#!/usr/bin/node
exports.performOperationMaybe = function (inputNumber, targetFunction) {
  targetFunction.call(this, inputNumber + 1);
};
