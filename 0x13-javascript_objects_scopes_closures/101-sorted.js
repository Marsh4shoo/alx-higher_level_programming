#!/usr/bin/node
const dataObject = require('./my-data').dataObject;

const entriesList = Object.entries(dataObject);
const values = Object.values(dataObject);
const uniqueValues = [...new Set(values)];
const transformedData = {};

for (const value of uniqueValues) {
  const keyList = [];
  for (const entry of entriesList) {
    if (entry[1] === value) {
      keyList.unshift(entry[0]);
    }
  }
  transformedData[value] = keyList;
}

console.log(transformedData);
