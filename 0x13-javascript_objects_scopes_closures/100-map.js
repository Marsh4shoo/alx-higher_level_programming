#!/usr/bin/node
const dataList = require('./my-data.js').dataList;
console.log(dataList);
console.log(dataList.map((element, idx) => element * idx));
