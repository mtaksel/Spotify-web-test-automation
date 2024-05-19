Test Cases for Spotify Web Application

User Authentication
    
Register

``
        Test Case: User can make a new account.
            Accept cookies.
            Click Register button.
            Enter a valid email address.
            Click on the "Continue" button.
            Enter a valid password.
            Click on the "Continue" button.
            Enter a profile name.
            Select a date of birth.
            Select a gender.
            Click on the "Continue" button.
            Accept Marketing box
            Accept Privacy box
            Click on the "Continue" button.
            Verify register name from profile
``

Valid Login

``
        Test Case: User can log in with valid credentials.
        Steps:
            Open the Spotify web app.
            Click on the "Log In" button.
            Enter valid email and password.
            Click the "Log In" button.
        Expected Result: User is redirected to the homepage and logged in successfully.
``

Invalid Login

``
        Test Case: User cannot log in with invalid credentials.
        Steps:
            Open the Spotify web app.
            Click on the "Log In" button.
            Enter invalid email or password.
            Click the "Log In" button.
        Expected Result: An error message is displayed, and the user remains on the login page.
``

Logout

``
        Test Case: User can log out successfully.
        Steps:
            Log in to the Spotify web app.
            Click on the profile icon.
            Select "Log Out" from the dropdown menu.
        Expected Result: User is logged out and redirected to the login page.

``

Music Playback

Play a Song

``

        Test Case: User can play a song from a playlist.
        Steps:
            Log in to the Spotify web app.
            Navigate to any playlist.
            Click on a song to play.
        Expected Result: The song starts playing, and the play icon changes to a pause icon.

``

Pause a Song

``

        Test Case: User can pause a currently playing song.
        Steps:
            Play a song from any playlist.
            Click the "Pause" button.
        Expected Result: The song pauses, and the pause icon changes back to a play icon.

``

Skip to Next Song

``

        Test Case: User can skip to the next song in a playlist.
        Steps:
            Play a song from any playlist.
            Click the "Next" button.
        Expected Result: The next song in the playlist starts playing.

``

Playlist Management

Create a New Playlist

``

        Test Case: User can create a new playlist.
        Steps:
            Log in to the Spotify web app.
            Click on "Create Playlist" in the sidebar.
            Enter a name for the playlist and click "Create".
        Expected Result: A new playlist is created and appears in the user's playlist list.

``

Add a Song to a Playlist

``

        Test Case: User can add a song to an existing playlist.
        Steps:
            Navigate to any song.
            Click on the "More" button (three dots) next to the song.
            Select "Add to Playlist" and choose an existing playlist.
        Expected Result: The song is added to the selected playlist.

``

Remove a Song from a Playlist

``

        Test Case: User can remove a song from a playlist.
        Steps:
            Open an existing playlist.
            Click on the "More" button (three dots) next to the song.
            Select "Remove from this Playlist".
        Expected Result: The song is removed from the playlist.

``

UI Interactions

Search for a Song

``

        Test Case: User can search for a song using the search bar.
        Steps:
            Log in to the Spotify web app.
            Enter a song name in the search bar.
            Press "Enter".
        Expected Result: Search results display songs matching the search query.

``

Navigate to Artist Page

``

        Test Case: User can navigate to an artist's page.
        Steps:
            Search for an artist.
            Click on the artist's name in the search results.
        Expected Result: The user is taken to the artist's page displaying their songs and albums.

``

Volume Control

``

        Test Case: User can adjust the volume.
        Steps:
            Play a song.
            Use the volume slider to adjust the volume.
        Expected Result: The volume changes according to the slider's position.

``

Edge Cases

Login with Empty Credentials

``

        Test Case: User cannot log in with empty email or password.
        Steps:
            Open the Spotify web app.
            Click on the "Log In" button.
            Leave email and/or password fields empty.
            Click the "Log In" button.
        Expected Result: An error message is displayed, prompting the user to fill in the required fields.

``

Play Song without Login

``

        Test Case: User cannot play a song without logging in.
        Steps:
            Open the Spotify web app without logging in.
            Try to play a song.
        Expected Result: The user is prompted to log in or sign up to play the song.

``

Invalid Search Query

``

        Test Case: Handle invalid or empty search queries gracefully.
        Steps:
            Enter an invalid or gibberish search query in the search bar.
            Press "Enter".
        Expected Result: A message indicating no results found is displayed.

``

These test cases cover various functionalities and ensure the Spotify web application operates correctly for different scenarios.