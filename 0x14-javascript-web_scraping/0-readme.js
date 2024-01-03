#!/usr/bin/node

const fs = require('fs');
// imports the built-in Node.js module fs (File System)

fs.readFile(process.argv[2], 'utf-8', (error, content) {
  if (error) {
    console.error('Error reading the file:', error);
  } else {
    console.log(content);
  }
});
