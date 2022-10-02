# COM411
University Work - Problem Solving Through Programming com411

* **Week One basic input and output**
  +  **Output**

      The first section was looking at basic output using the Python Print() command. Started in the folder [basic][basic] working in the class with others. We looked at escape characters to deal with new lines, tabs and using them to display speach marks etc.

   + **Input**

      I contiuned my work in the folder [Week01\Basic][week01].

      [ascii-robot][robot] The aim of this exercise was to work with user input and to have an effect on changing the output. Uses a menu to offer the user a choice of robots to display along with an exit option.  I used one of the examples from [asciiart][asciiart] and selected two images of Pacman. So instead of just letting the user input the character to be used for the eyes I used the input to display different image.

      The images were originaly togeter as two seperate functions.  image01 and image02 but some of the lines were identical in each images. So I sliced the images and then stiched them back using shared code in both images. I try not to duplicate code where I can.  It was not really a practical approach as it makes it more difficult to maintain.

      Next we looked at different data types in [Data_Types.py][data_type].  We had to get some data from the user and then calculate the BMI and display this on the console.  I created a class called human to hold the properties that the user inputed.  This was then used to print the message back to the console.  I used "if" and "elseif" statements to display a health message related to the BMI and display this on the console.

      The final section was dealing with getting data from the user to set the health, energy and shield values.  This was then used to display that number of utf-8 characters for each property.  I found a useful [tool][utf-8tool] to get the ascii Hex code for the characters so we could print using the hex codes instead of using the character a strings.  I wanted to get some practice on using TDD in Python and to see how Github works with workflows. There are a couple of tests that check the class and the function.  Theses tests will be run when a pull request is made in GitHub.







[basic]:/basics/
[week01]:/Week01/Basic/
[robot]:/Week01/Basic/Output/ascii-robot.py
[asciiart]:https://asciiart.website/
[data_type]:/Week01/Basic/Input/Data_Types.py
[utf-8tool]:https://www.cogsci.ed.ac.uk/~richard/utf-8.html
