#!/usr/bin/env node

const affirmations = [
	"Affirmation 1",
	"Affirmation 2",
	"etc."
];

const randomIndex = Math.floor(Math.random() * affirmations.length);
const randomAffirmation = affirmations[randomIndex];

const affirmationLength = randomAffirmation.length;
const hashtag = "#".repeat(affirmationLength + 4);

console.log(hashtag);
console.log(" " + randomAffirmation);
console.log(hashtag);