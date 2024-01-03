#!/usr/bin/node

const request = require('request');
// imports the built-in Node.js module request (File System)

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
