#!/usr/bin/node

const request = require('request');

const getNames = async () => {
  const uri = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

  let characters = [];

  // A helper function to wrap 'request' in a Promise
  const makeRequest = (uri) => {
    return new Promise((resolve, reject) => {
      request(uri, { json: true }, (error, response, body) => {
        if (error) reject(error);
        else resolve(body);
      });
    });
  };

  try {
    // Fetch the film data
    const data = await makeRequest(uri);
    characters = data.characters;

    // Loop through each character and fetch their name
    for (const character of characters) {
      const characterData = await makeRequest(character);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
};

getNames();
