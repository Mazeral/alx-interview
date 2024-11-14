#!/usr/bin/node

const get_names = async () => {
const request = require('request');

const uri = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

let characters = [];
  const data = await request.get(uri).then(res => { return res.json(); });
  characters = data.characters;
  for (const character of characters) {
    const name = await request.get(character).then(res => { return res.json(); });
    console.log(name.name);
  }
};

get_names();
