#!/usr/bin/node

const fs = require('fs');
// imports the built-in Node.js module fs (File System)

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
