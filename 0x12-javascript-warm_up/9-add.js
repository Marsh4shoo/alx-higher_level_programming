#!/usr/bin/node
function sumValues(a, b) {
  console.log('Sum:', parseInt(a) + parseInt(b));
}

sumValues(process.argv[2], process.argv[3]);
