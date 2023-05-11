# Wordle

This is a Python terminal game of [Wordle](https://en.wikipedia.org/wiki/Wordle#:~:text=Wordle%20is%20a%20web%2Dbased,York%20Times%20Company%20since%202022.) and is deployed on Heroku using the Code Institutes mock terminal template.

Users are greeted by a main menu which has 3 different options to choose from, they can start a game, read the rules or if they decide they don't want to play they can exit. After choosing to start the game they have six attempts to correctly guess a random five letter word which is pulled in from a long list of five letter words. If they run out of attempts it is game over and they can try again, and every time the word is random so its very rare that they will get the same word twice in a row. 

The live application can be found at [WordlePy](https://wordlepy.herokuapp.com/).

## UX & Design

### User Stories
- As a user, I want to play a guesing game.
- As a user, I want to be able to view the rules of the game.
- As a user, I want to see how many letters I have guessed.
- As a user, I want to be able to visually see what letters I have already guessed.
- As a user, I want to be able to see how many attempts I have left.
- As a user, I want to be able to restart the game upon completion without having to exit the program and come back.

## Features
- Home Screen/Main Menu
    - From this menu, users can, play the game, view the rules or exit the program.
    - ![Main Menu](/assets/img/main-menu.png)

- Rules
    - This displays the rules of the games and what is required of the users to play the game, also from here users can play the game by entering the correct input.

    - ![Rules](/assets/img/rules.png)

- Wordle
    - This is the main feature of this program. The user is prompted to enter their guess and from there the program works the same as wordle, a right letter in the correct postion will be coloured green, a letter in the word but in the wrong postion will be coloured yellow, and finally a letter that is not in the word an underscore will be printed and that will be coloured red.
    - ![Game Start](/assets/img/game-start.png)

    - ![Letters](/assets/img/correct-and-incorrect-position-letters.png)

    - ![Incorrect](/assets/img/incorrect-letters.png)

- Invalid Input
    - To the best of my knowledge all invalid inputs are handled and the user is prompted to try again, mainly what is tested is, is there a special character in their guess, is their guess blank/empty, if any of these are true then they are prompted to try again and no attempts are deducted if this is the case.
    
    - ![Data Validation](/assets/img/data-validation1.png)

    - ![Data Validation](/assets/img/data-validation2.png)

    - ![Data Validation](/assets/img/data-validation3.png)

- Game Over - Win
    - ![You Win](/assets/img/you-win.png)

- Game Over - Lost
    - ![You Lose](/assets/img/you-lost.png)

### Future Implementations
- I would like to do all the data validation in one function instead of how I do it at the moment but I tried and ran out of time and was not able to get it to work.
- I would also like to add multiple difficulties for example you can choose between 5 letter words, 6 letter words and so on.
- Add a proper GUI as it currently just runs in the terminal.


### Technologies Used
The following is a list of technologies that I used to create this project.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [HTML](https://en.wikipedia.org/wiki/HTML5)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [GitHub](https://github.com/)
    - Github was used to store the projects code.

- [Gitpod](https://gitpod.io/)
    - Gitpod was used to code this project and to push commits to GitHub.

- [Git](https://git-scm.com/)
    - Git was used to handle version control of this project via the gitpod terminal.

### Imported Libraries and Packages
- [random](https://docs.python.org/3/library/random.html) was used to select a random word from the list of words.
- [os](https://docs.python.org/3/library/os.html) was used to create the clear_screen function to reduce clutter and enhance the overall experience for the user.
- [Colorama](https://pypi.org/project/colorama/) was used to add colour for functionality of the game and to make the program slightly prettier.

## Testing and Validation
- At various stages PEP8 validation was done, I am getting one warning that I cant seem to get rid of but it does not effect the program from what I can tell
![PEP8](/assets/img/pep8.png)
## Bugs
| No | Bug | How I solved the issue |
| :--- | :--- | :--- |
| 1 | After the user guesses the word the loop would keep going instead of stopping. | I fixed it by adding a loop inside the game_logic function that asks would they like to play again or quit and that solved the issue.
| 2 | The Congratulations message was printing the incorrect number of attempts taken to complete the game. | I changed the while loop within the game_logic function from attempts > 0 to attempts < 6 and added a new variable called "turns" to get the right output.
| 3 | When entering a blank string it exits the program. | Changed the condition of the if statement where the data validation is done and now users can enter a blank string without it breaking the program.
| 4 | When the users guess contained special characters and/or numbers it was taking a turn away from the user | I added a check and within that check I just negated the taking a turn away from the user |
| 5 | When the users guess contains a special character or number it is still printed out as if they are playing the game | I fixed this and now the program tells the user that they entered a special character or number and to please try again without taking a life off them |
| 6 | If you enter a word with the same letter occuring sometimes it won't print it out properly | I changed the function to ensure that the proper output is being displayed to the user | 

A bug that I found that I don't have time to fix is when a user enters a string like the following "ggggg" the game will still take a life away from them, I would like to fix this but I do not have the time to do so in future implementations this is something that I would fix.

## Deployment & Local Development
### Deployment
The site is deployed using Heroku. To deploy to Heroku:
1. To deploy on Heroku successfully you first have to create some files: requirements.txt and a procfile.

2. The requirements.txt file contains the dependencies required to run the program successfully. To create a requirements.txt file do the following
    ```bash
    pip3 freeze --local > requirements.txt
    ```

3. The procfile lets Heroku know which files actually run the app and where they can be found. To create this file run the following command in the terminal:
    ```bash
    echo web: python app.py > Profile
    ```

4. If the Procfile has been created successfully it will have the Heroku logo next to it. Make sure to save both of these files (Procile and requirements.txt) then add, commit and push them go GitHub.

5. Login to [Heroku](https://www.heroku.com) (sign up if you do not have an account).

6. Click on the new button then click create new app.

7. From here you will be asked to name your app and select a region. Once these are completed click create app.

8. You will need to connect Heroku to the Github repo where the project code is located. Select Github in the deployment section, find the correct repo and then click connect.

9. Once the repo is connected, you will need to provide Heroku with some config variables it needs to build the app if necessary, if not then you can ignore this step.

10. You're now ready to enable automatic deployment and the create button. Now Heroku will start building your app. Once this done your app is ready to be viewed by the world!

### Local Development

#### How to Fork
To fork the repo:

1. Log in or sign up to Github.

2. Go to the repo for this project, [WordlePy](https://github.com/ShaneCDev/Wordlepy)

3. Click the fork button in the top right corner.

#### How to Clone
To clone the repo:

1. Log in or sign up to Github.

2. Go to the repo for this project, [WordlePy](https://github.com/ShaneCDev/Wordlepy)

3. Click on the code button, select whether you would like to clone the repo with HTTPS, SSH or Github CLI and copy the link shown.

4. Open the terminal in your IDE of choice and change the currect working directory to the location you want to use for the cloned directory.

5. Type the following command into the terminal (after the clone you will need to paste the link you copied in step 3):
    ```bash
    git clone {Link from step 3 goes here}
    ```
6. Set up a virtual environment.

7. Install the dependencies from the requirements.txt file, you can do this via running the following command in the terminal:
    ```bash
    pip3 install -r requirements.txt
    ```

## Credits

### Code Used
- [Stack Overflow](https://stackoverflow.com/) was used throughout this project especially with the regex patterns.
- For the wordle algorithm itself I read a ton of different articles and kind of mashed how they did it together. 
- This [video](https://youtu.be/Ce6dIj-FKb4) also helped me for creating the wordle logic and I built upon it and expanded it out.

### Acknowledgements
I would like to thank:
 - The slack community.
