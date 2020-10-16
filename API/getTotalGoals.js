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
 * Complete the 'getTotalGoals' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. STRING team
 *  2. INTEGER year
 */

async function getTotalGoals(team, year) {
    const axios = require('axios');
    let page = 1;
    const url1 = `https://jsonmock.hackerrank.com/api/football_matches?year=${year}&team1=${team}&page=${page}`;
    const url2 = `https://jsonmock.hackerrank.com/api/football_matches?year=${year}&team2=${team}&page=${page}`;

    const fetchData = async(url, teamNumber) => {
        const {data} = await axios.get(url);
        const pages = data.total_pages;
        // const allData = [data.data];
        let total = 0;

        for (let matchData of data.data) {
            const goalsKey = `team${teamNumber}goals`;
            total += Number(matchData[goalsKey]);
        }

        if (pages > 1) {
            const promises = [];
            const baseUrl = url.slice(0, -1);
            for (let i=2; i<=pages; i++) {
                promises.push(axios.get(baseUrl+i));
            }
            const bigData = await Promise.all(promises)
            for (let response of bigData) {
                for (let matchData of response.data.data) {
                    const goalsKey = `team${teamNumber}goals`;
                    total += Number(matchData[goalsKey]);
                }
            }
        }
        return total;
    }

    try {
        const team1total = await fetchData(url1, 1);
        const team2total = await fetchData(url2, 2);
        return team1total + team2total
    } catch(err) {
        console.log(err)
    }
}
async function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const team = readLine();

    const year = parseInt(readLine().trim(), 10);

    const result = await getTotalGoals(team, year);

    ws.write(result + '\n');

    ws.end();
}