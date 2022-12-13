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


### Flowchart
Flowchart goes here.

### Favicon
Favicon goes here.

## Features
- Home Screen/Main Menu
    - From this menu, users can, play the game, view the rules or exit the program.
    - Screenshot to go here

- Rules
    - This displays the rules of the games and what is required of the users to play the game, also from here users can play the game by entering the correct input.
    - Screenshot to go here.

- Wordle
    - This is the main feature of this program. The user is prompted to enter their guess and from there the program works the same as wordle, a right letter in the correct postion will be coloured green, a letter in the word but in the wrong postion will be coloured yellow, and finally a letter that is not in the word an underscore will be printed and that will be coloured red.
    - Game start screenshot to go here
    - Correct letter at correct position screen to go here
    - Correct letter at incorrect position screen to go here
    - Incorrect letter screen to go here.

- Invalid Input
    - To the best of my knowledge all invalid inputs are handled and the user is prompted to try again, mainly what is tested is, is there a special character in their guess, is their guess blank/empty, if any of these are true then they are prompted to try again and no attempts are deducted is this is the case.
    - Screenshots to go here

- Game Over - Win
    - Screenshot of ascii art to go here

- Game Over - Lost
    - Screenshot of ascii art to go here.

### Future Implementations
- To be filled in.

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
- To be done

## Bugs
- To be added.

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
To be filled out.

### Media
To be filled out.

### Acknowledgements
To be filled out.
