# SI 507 Final Project (iTunes)

Amanda Jung

[Link to this repository](https://github.com/amajung/SI507-FinalProject)

---

## Project Description

The project will allow users to view and add songs to their playlist database.

## How to run

1. First, you should install all requirements with `pip install -r requirements.txt`
2. Second, you should run the file `SI507project_tools.py` with the code `python SI507project_tools.py`
3. To access the Flask web application, you need to locate, copy, and paste the web address given through the console into a web browser

## How to use

1. To begin, start adding songs to your playlist database through the route `/<add/song/<artist/<song>`. Input your favorite artists and songs in the placeholders accordingly as indicated by the route.
  - Note 1: Artist names and songs must be entered with accurate and complete spelling and punctuation in order for the application to work. A message indicating so will appear.
  - Note 2: If a song already exits in the playlist, a messaged indicating so will appear.

2. Once you correctly input the song you want to add in the route `/<add/song/<artist/<song>`, the song will automatically add it to your playlist database and the page corresponding to the route will appear with information about the song (i.e. song name, artist, cover art, and audio preview). The page will also have a button labeled `Playlist Options` that can be toggled opened by clicking on it.

The options that appear underneath the button `Playlist Options` when clicked on include `View Complete Playlist`, `View Playlist by Artist`, and `View Playlist by Genre`.
  - Clicking on the option `View Complete Playlist` redirects the user to the page that corresponds with the route `/`, which displays the playlist with all the songs that were previously added.
  - Clicking on the option `View Playlist by Artist` redirects the user to the page that corresponds with the route `/<artist>`, which displays the playlist with all the songs based on the artist of the song that was just added.
  - Clicking on the option `View Playlist by Genre` redirects the user to the page that corresponds with the route `/<genre>`, which displays the playlist with all the songs based on the artist of the genre that was just added.

2. Once you have songs added to your playlist, you can view your complete playlist or by artist or genre based on the routes indicated above.
  - Note 1: Empty playlists will indicate so on the page (i.e. 'There are no songs in this playlist yet', 'There are no songs by this artist yet.', 'There are no songs of this genre yet.').

## Routes in this application
- `/` -> This is the home page and will show the current songs in the playlist that the user has added.
- `/<add/song/<artist/<song>`-> This route will show the song based on the artist and song input and add it to the user's playlist.
- `/<artist>` -> This route will list songs in the user’s playlist based on the artist input.
- `/<genre>` -> This route will list songs in the user’s playlist based on the genre input.

## How to run tests
1. First, access the project directory (e.g. access a certain directory if necessary)
2. Second, run the test file `SI507project_tests.py` using the following code `python SI507project_tests.py` in your respective terminal

## In this repository:
- README_template.md
- requirements.txt
- SI507project_tools.py
- SI507project_tests.py
- templates
  - index.html
  - add_song.html
  - artists.html
  - genres.html
- static
  - toggle_button.js


---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [x] This is a completed requirement.
- [ ] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [x] Project is submitted as a Github repository
- [x] Project includes a working Flask application that runs locally on a computer
- [ ] Project includes at least 1 test suite file with reasonable tests in it.
- [ ] Includes a `requirements.txt` file containing all required modules to run program
- [x] Includes a clear and readable README.md that follows this template
- [x] Includes a sample .sqlite/.db file
- [ ] Includes a diagram of your database schema
- [x] Includes EVERY file needed in order to run the project
- [ ] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [x] Includes at least 3 different routes
- [x] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [x] Interactions with a database that has at least 2 tables
- [x] At least 1 relationship between 2 tables in database
- [x] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [ ] Use of a new module
- [ ] Use of a second new module
- [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [x] A many-to-many relationship in your database structure
- [ ] At least one form in your Flask application
- [x] Templating in your Flask application
- [x] Inclusion of JavaScript files in the application
- [x] Links in the views of Flask application page/s
- [ ] Relevant use of `itertools` and/or `collections`
- [ ] Sourcing of data using web scraping
- [x] Sourcing of data using web REST API requests
- [x] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [ ] Caching of data you continually retrieve from the internet in some way

### Submission
- [x] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [x] I included a summary of my project and how I thought it went **in my Canvas submission**!
