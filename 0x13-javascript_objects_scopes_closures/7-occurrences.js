exports.countOccurrences = function (array, target) {
  let occurrences = 0;
  for (let i = 0; i < array.length; i++) {
    if (target === array[i]) {
      occurrences++;
    }
  }
  return occurrences;
};

