// Get a reference to the generate idea button
const generateIdeaBtn = document.getElementById('generate-idea-btn');

// Get a reference to the idea output div
const ideaOutput = document.getElementById('idea-output');

// Define an array of ideas
const ideas = [
    'Start a blog about your favorite hobby',
    'Take a cooking class',
    'Volunteer at a local animal shelter',
    'Join a book club',
    'Learn a new language',
    'Take up gardening',
    'Plan a weekend camping trip',
    'Explore a new city or town nearby',
    'Attend a concert or music festival',
    'Take a dance class',
    'Join a sports league',
    'Take a painting or art class',
    'Start a podcast',
    'Learn to code',
    'Join a theater group',
    'Try a new restaurant or cuisine',
    'Go on a road trip',
    'Take up photography',
    'Join a hiking group',
    'Organize a game night with friends'
];

// Function to generate a random idea
function generateIdea() {
    // Generate a random index for the ideas array
    const randomIndex = Math.floor(Math.random() * ideas.length);

    // Get the idea at the random index
    const randomIdea = ideas[randomIndex];

    // Display the idea in the idea output div
    ideaOutput.innerHTML = `<p>${randomIdea}</p>`;
}

// Add a click event listener to the generate idea button
generateIdeaBtn.addEventListener('click', generateIdea);
