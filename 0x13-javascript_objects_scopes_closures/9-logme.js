let count = 0;

exports.printLog = function (item) {
  console.log(count + ': ' + item);
  count++;
};

