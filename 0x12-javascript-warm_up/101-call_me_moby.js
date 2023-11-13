#!/usr/bin/node
exports.invokeFunctionMultipleTimes = function (count, targetFunction) {
  while (count > 0) {
    targetFunction.call();
    count--;
  }
};
