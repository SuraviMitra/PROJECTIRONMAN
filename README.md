# PROJECTIRONMAN

<----------------------------------------------------Project IRON MAN--------------------------------------------------------------------------------------->


1.speak()--->
   *The first and foremost thing for an A.I assistant is that it should be able to speak.
   *This function will take audio as an argument, then it will pronounce it.


  

2.pyttsx3--->
   (pip install pyttsx3)
   *The next thing we need is audio for that we are going to install a module called pyttsx3.
   *It is a python library that helps to convert text to speech.




3.After successfully installing pyttsx3 we will import a module 
-------------------------------------------------------------------------------------------------------------------------------------------------------  
     import pyttsx3

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voice[1].id)
--------------------------------------------------------------------------------------------------------------------------------------------------------

*spi5-->It is a microsoft developed speech API.
*void[0].id-->male voice 
*void[1].id-->female voice
*finally set the voice



4.speak()-->
  *It will convert text into speech.
  *engine.say(audio)-->engine will say the audio.



5.main method()-->
  *Inside this main() Function, we will call our speak function.
  *Whatever you will write inside this speak() function will be converted into speech.
 

6.wishme() function--->
  *function that will make our J.A.R.V.I.S. wish or greet the user according to the time of computer or pc.
  *To provide current or live time to A.I., we need to import a module called datetime. Import this module to your program by:

                            import datetime
  *Here, we have stored the current hour or time integer value into a variable named hour. Now, we will use this hour value inside an if-else loop.



7.takeCommand()-->
  *The next most important thing for our A.I. assistant is that it should take command with the help of the microphone of the user's system.
  *With the help of the takeCommand() function, our A.I. assistant will return a STRING OUTPUT by taking microphone input from the user.



8.speechRecognition--->
   *Before defining the takeCommand() function, we need to install a module called speechRecognition. 
 
       pip install speechRecognition


9.We have successfully created our takeCommand() function. Now we are going to add a try and except block to our program to handle errors effectively.



10.wikipedia--->
    *To do Wikipedia searches, we need to install and import the Wikipedia module into our program.
   
     pip install wikipedia
 

11.After successfully installing the Wikipedia module, import it into the program by writing an import statement.


12.webbrowser(youtube, google, stackoverflow)--->
   *To open any website, we need to import a module called webbrowser. It is an in-built module, and we do not need to install it with a pip statement; we can directly import it into our program by writing an import statement.


13.Play Music----->
   *To play music, we need to import a module called os. Import this module directly with an import statement.
   * we first opened our music directory and then listed all the songs present in the directory with the os module's help. With the help of os.startfile, you can play any song of your choice.



14.current Time--->
   *we are using the datetime() function and storing the current or live system time into a variable called strTime. After storing the time in strTime, we are passing this variable as an argument in speak function. Now, the time string will be converted into speech.


15.open VS CODE--->
   *To open the VS Code or any other application, we need the code path of the application.


16.send Email---->
    *To send an email, we need to import a module called smtplib.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
SMTP--->Simple Mail Transfer Protocol (SMTP) is a protocol that allows us to send emails and route emails between mail servers.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Note: Do not forget to 'enable the less secure apps' feature in your Gmail account. Otherwise, the sendEmail function will not work properly.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



16.Tempreature--->

17.Power Left--->

18.Internet Speed-->




