#!/usr/bin/node
const fs = require('fs');

const firstFileContent = fs.readFileSync(process.argv[2]).toString();
const secondFileContent = fs.readFileSync(process.argv[3]).toString();
const outputFile = process.argv[4];

fs.writeFileSync(outputFile, firstFileContent + secondFileContent);
 
