#!/usr/bin/node

const request = require('request');

const uri = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

request(uri, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    });
  }
});
