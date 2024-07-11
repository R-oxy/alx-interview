#!/usr/bin/node

const request = require('request');
const myArgs = process.argv.slice(2);
const movieId = myArgs[0];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching film details:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`API request failed with status ${response.statusCode}`);
    return;
  }

  try {
    const filmData = JSON.parse(body);
    const characterUrls = filmData.characters;

    // Fetch character details in parallel
    Promise.all(characterUrls.map(fetchCharacterDetails))
      .then((characters) => characters.forEach((char) => console.log(char.name)))
      .catch((error) => console.error('Error fetching character details:', error));
  } catch (error) {
    console.error('Error parsing JSON:', error);
  }
});

async function fetchCharacterDetails (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        try {
          const characterData = JSON.parse(body);
          resolve(characterData);
        } catch (error) {
          reject(new Error('Invalid character data from API'));
        }
      }
    });
  });
}
