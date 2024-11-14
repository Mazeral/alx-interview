#!/usr/bin/node

const request = require('request');

const getNames = async () => {
  const uri = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

  const helper = (uri) => {
    return new Promise((resolve, reject) => {
      request.get(uri, { json: true }, (err, res, body) => {
        if (err) reject(err);
        else resolve(body);
      });
    });
  };

  const films = await helper(uri);
  const characterLinks = films.characters;
  for (const link of characterLinks) {
    const character = (await helper(link));
    console.log(character.name);
  }
};

getNames();
