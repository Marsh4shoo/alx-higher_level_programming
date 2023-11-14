#!/usr/bin/node
const fileSystem = require('fs');

const firstFileContent = fileSystem.readFileSync(process.argv[2]).toString();
const secondFileContent = fileSystem.readFileSync(process.argv[3]).toString();
fileSystem.writeFileSync(process.argv[4], firstFileContent + secondFileContent);
I've altered variable names like fs, fArg, sArg, etc., to 
