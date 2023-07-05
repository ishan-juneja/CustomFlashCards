# CustomFlashCards
This program reeanacts using flashcards to study!

## Structure
- `main.py` behaves as the nucleus and runs the entirety of the program
- `french_words.csv` is a file containing the french words in this case that the user is rying to learn from. This will generally be a csv file the user will edit and rename as to what they desire to learn.
- `words_to_learn.csv` is a file containing the words or info that the user incorrectly answers.
## Dependencies & Configurations
1. The [Pandas Library](https://pandas.pydata.org/) used to make it simple to work with our spreadsheet data.
2. The program utilizes [turtle graphics](https://docs.python.org/3/library/turtle.html) for all the graphical displays.

## Demo
The program displays a flashcard for the user to memorize
<img width="867" alt="Screenshot 2023-07-05 at 8 58 08 AM" src="https://github.com/ishan-juneja/CustomFlashCards/assets/69048541/bf88d72f-5487-4d28-9d45-d4b1485486d7">

After a set time of 3 seconds or through user input, the flash card then reveals the answer. Depending on the user input of correct or incorrect then, the question will be stored in the relearn file.
<img width="897" alt="Screenshot 2023-07-05 at 8 58 21 AM" src="https://github.com/ishan-juneja/CustomFlashCards/assets/69048541/499755d2-760a-41d8-8f7f-ccb01102f955">
