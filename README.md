# Flash Card App

This application is for language learning, specifically to learn the Russian language. The methodology employed for this purpose is learning through repetition and memorization. The game will show the front of a card where is a russian word. The user has 5 seconds to guess the english translation of that card before time runs out and the card automatically flips to the other side, showing the english meaning of that card. The interface has two buttons: correct, incorrect, and the user has to press one depending on if he correctly guessed the word or not. The game contains 50.000 cards, but at the beginning, it focuses on the 1.000 most frequently used russian words, so the user will get inmediately the vocabulary for inmediate and effective communication.


1. CSV to Json.

Why? The JSON format is syntactically similar to the code for creating JavaScript objects.

JSON data can easily be sent between computers. Json is a str.

2. Target

The objective is to learn 1000 words. From russian to spanish.

3. Automatic flipping cards

The script starts with the card in russian.
The script waits 3-5 seg to flip the card to spanish,
the objective is that you guess the meaning of the word in that time.
User has to click "correct" button is guessed, and click "wrong" button if wrong.
Program will store the results in 2 list for each. And store them.
The program will keep the list of wrong guesses in the iteration.
And so on.

4. Cleaner

raw_data_ru.csv is the input.
clean the data, add hedares to columns, add the column esp with the translation of the data.
store the result dataset in the preferred format. save in file .csv


