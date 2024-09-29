# Higher-or-lower
This is a simple web application built using Flask that allows users to guess a random number between 0 and 9. The application provides feedback for each guess and includes fun visual responses based on the user's input.

## Features
- A randomly generated number between 0 and 9 at each session start.
- Users can input a guess in the URL, and the application will respond with one of three messages:
  - "Too low" (if the guess is lower than the random number)
  - "Too high" (if the guess is higher than the random number)
  - "You found me!" (if the guess is correct)
- Each response is styled with different colors and includes an accompanying GIF for a fun user experience.

## Code Structure
- Home Route (/): Displays a welcome message and prompts the user to guess a number.
- Guess Route (/<int:guess>): Checks the user's guess against the random number and provides feedback:
  - Too low: Red text with a GIF.
  - Too high: Purple text with a GIF.
  - Correct guess: Green text with a GIF.
