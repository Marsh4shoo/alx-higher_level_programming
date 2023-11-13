#!/usr/bin/node
const occurrenceCount = Number(process.argv[2]);

if (isNaN(occurrenceCount)) {
  console.log('Error: Please provide a valid number of occurrences');
} else {
  for (let i = 0; i < occurrenceCount; i++) {
    console.log('Learning C is enjoyable');
  }
}-
