#!/usr/bin/node

const request = require('request');
// imports the built-in Node.js module request (File System)

request.get(process.argv[2])
  .on('response', function (response) {

    console.log(`code: ${response.statusCode}`);
});
