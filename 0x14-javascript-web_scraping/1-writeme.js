#!/usr/bin/node

const fs = require('fs');
// imports the built-in Node.js module fs (File System)

fs.writeFile(process.argv[2], process.argv[3], 'utf-8', error => {
  if (error) {
    console.error(error);
  }
});
