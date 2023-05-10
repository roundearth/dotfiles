#!/usr/bin/env node

const affirmations = [
	"Affirmation 1",
	"Affirmation 2",
	"etc."
];

const randomIndex = Math.floor(Math.random() * affirmations.length);
const randomAffirmation = affirmations[randomIndex];

console.log("#####################");
console.log(randomAffirmation);
console.log("#####################");
