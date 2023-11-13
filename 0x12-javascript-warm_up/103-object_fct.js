#!/usr/bin/node
const customEntity = {
  category: 'entity',
  numericValue: 12
};
console.log(customEntity);
customEntity.increment = function () {
  this.numericValue++;
};
customEntity.increment();
console.log(customEntity);
customEntity.increment();
console.log(customEntity);
customEntity.increment();
console.log(customEntity);
