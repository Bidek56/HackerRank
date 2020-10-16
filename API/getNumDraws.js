'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}



/*
 * Complete the 'getNumDraws' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER year as parameter.
 */

const https = require("https"); 

const getJSONAsync = url => new Promise((resolve, reject) => {       // define a function getJSONAsync which returns a Promise that wraps the https.get call, getJSONAsync is awaitable
  let req = https.get(url, res => {                                  // make the https.get request
    if(res.statusCode < 200 || res.statusCode >= 300) {              // if the status code is an error one
      return reject(new Error('statusCode=' + res.statusCode));      // reject and skip the rest
    }

    let body = [];                                                   // otherwise accumulate..
    res.on('data', chunk => body.push(chunk));                       // ..the data
    res.on('end', () => {                                            // on end                               
      try {
        body = JSON.parse(Buffer.concat(body).toString());           // try to JSON.parse the data
      } catch(e) {
        reject(e);                                                   // reject if an error occurs
      }
      resolve(body);                                                 // resolve the parsed json object otherwise
    });
  });

  req.on("error", error => reject(error));                           // reject if the request fails too (if something went wrong before the request is sent for example)
});

async function getNumDraws(year) {
  let result = 0;

  for(let goal = 0; goal < 11; goal++) {
    let data = await getJSONAsync(`https://jsonmock.hackerrank.com/api/football_matches?year=${year}&team1goals=${goal}&team2goals=${goal}`);
    result += data.total;
  }

  return result;
}

async function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const year = parseInt(readLine().trim(), 10);

    const result = await getNumDraws(year);

    ws.write(result + '\n');

    ws.end();
}