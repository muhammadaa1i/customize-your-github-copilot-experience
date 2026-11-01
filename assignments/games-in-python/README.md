# 📘 Assignment: Hangman Game

## 🎯 Objective

Build the classic Hangman word-guessing game in Python. You will practice string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️	Pick a Secret Word

#### Description
Use the starter code to randomly choose a secret word from the predefined list and set up the variables that track the game state.

#### Requirements
Completed program should:

- Randomly select a word from the `words` list using the `random` module
- Store the guessed letters and the number of incorrect guesses
- Set a maximum number of incorrect guesses (for example, 6)


### 🛠️	Guess Letters and Show Progress

#### Description
Write the main game loop that asks the player for a letter and shows which letters of the word have been revealed so far.

#### Requirements
Completed program should:

- Accept one letter per guess from the player
- Show the current progress using underscores for hidden letters (for example, `_ y _ h o n`)
- Show how many incorrect guesses are remaining after each turn

```
Word: _ _ _ _ _ _
Guess a letter: o
Word: _ _ _ _ o _
Incorrect guesses left: 6
```


### 🛠️	End the Game

#### Description
Stop the game when the player has guessed the whole word or has run out of attempts, and tell the player the result.

#### Requirements
Completed program should:

- End the loop when every letter is revealed or no attempts are left
- Print a win message that includes the word when the player wins
- Print a lose message that reveals the word when the player loses
