#!/usr/bin/node
// script that prints all characters of a Star Wars movie

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Please provide a valid Movie ID as a command-line argument.');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Function to fetch character data for a given URL
const fetchCharacter = characterUrl => {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, characterData) => {
      if (error) {
        reject(error);
        return;
      }

      const character = JSON.parse(characterData);
      resolve(character.name);
    });
  });
};

// Fetch movie data from the Star Wars API
request(apiUrl, async (error, response, movieData) => {
  if (error) {
    console.error(`Error fetching movie: ${error.message}`);
    return;
  }

  const movie = JSON.parse(movieData);
  const characters = movie.characters;

  // Fetch and print character names in order using async/await
  for (const characterUrl of characters) {
    try {
      const characterName = await fetchCharacter(characterUrl);
      console.log(characterName);
    } catch (error) {
      console.error(`Error fetching character: ${error.message}`);
    }
  }
});
