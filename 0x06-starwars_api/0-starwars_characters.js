#!/usr/bin/node
// script that prints all characters of a Star Wars movie

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Please provide a valid Movie ID as a command-line argument.');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Fetch movie data from the Star Wars API
request(apiUrl, (error, response, movieData) => {
  if (error) {
    console.error(`Error fetching movie: ${error.message}`);
    return;
  }

  // Parse the JSON movie data
  const movie = JSON.parse(movieData);
  const characters = movie.characters;

  // Loop through character URLs and fetch character data
  characters.forEach(characterUrl => {
    request(characterUrl, (error, response, characterData) => {
      if (error) {
        console.error(`Error fetching character: ${error.message}`);
        return;
      }

      // Parse the JSON character data
      const character = JSON.parse(characterData);
      console.log(character.name);
    });
  });
});
