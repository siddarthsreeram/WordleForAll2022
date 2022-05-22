
# only works on Python 3.6.8

#imports necessary packages
from time import sleep
import speech_recognition as sr
import pyttsx3
from selenium import webdriver
from selenium.webdriver.support.color import Color

#creates varaibles that will be used to keep track of quantities
MyText = '0'
strCorrect='Correct'
strElseWhere='Elsewhere'
strIncorrect='Incorrect'
entercount=0

#strings that will be used to keep track of user's guesses for each Wordle row
strRow1 = ''
strRow2 = ''
strRow3 = ''
strRow4 = ''
strRow5 = ''
strRow6 = ''

#30 strings that remember the user's 30 character guesses' correct-status
recall1 = ''
recall2 = ''
recall3 = ''
recall4 = ''
recall5 = ''
recall6 = ''
recall7 = ''
recall8 = ''
recall9 = ''
recall10 = ''
recall11 = ''
recall12 = ''
recall13 = ''
recall14 = ''
recall15 = ''
recall16 = ''
recall17 = ''
recall18 = ''
recall19 = ''
recall20 = ''
recall21 = ''
recall22 = ''
recall23 = ''
recall24 = ''
recall25 = ''
recall26 = ''
recall27 = ''
recall28 = ''
recall29 = ''
recall30 = ''


#the method that takes in a String as a paramter and returns the spoken String
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


# get to wordlegame website
r = sr.Recognizer()
driver = webdriver.Chrome()
driver.get("https://wordlegame.org/")
sleep(2)


#a loop that keeps running while program is active
while (True):
    #a try statement to avoid cancelling the code due to noise detection errors
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            print("ambient")
            r.adjust_for_ambient_noise(source2, duration=0.2)
            print("ambientover")

            # listens for the user's input
            strSpeak1="Speak Now"
            SpeakText(strSpeak1)
            audio2 = r.listen(source2)
            sleep(2)
            strSpeak2="Speak End"
            SpeakText(strSpeak2)

            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("Did you say " + MyText)
            SpeakText(MyText)

     #except statments for possible errors in noise detection
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        strError="Error, try again"
        SpeakText(strError)

    #code for the alphabet and backspace and enter keys - xpaths are used to get the button on the site and if statments used for checking which guess this is
    # a
    if MyText == 'letter a':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[2]/div[1]') \
            .click()
        if entercount==0:
          strRow1+="a"
        if entercount==1:
          strRow2+="a"
        if entercount==2:
          strRow3+="a"
        if entercount==3:
          strRow4+="a"
        if entercount==4:
          strRow5+="a"
        if entercount==5:
          strRow6+="a"
        sleep(3)
        

    # b
    if MyText == 'letter b':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[3]/div[6]') \
            .click()
        if entercount==0:
          strRow1+="b"
        if entercount==1:
          strRow2+="b"
        if entercount==2:
          strRow3+="b"
        if entercount==3:
          strRow4+="b"
        if entercount==4:
          strRow5+="b"
        if entercount==5:
          strRow6+="b"
        sleep(3)

    # c
    if MyText == 'letter c':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[3]/div[4]') \
            .click()
        if entercount==0:
          strRow1+="c"
        if entercount==1:
          strRow2+="c"
        if entercount==2:
          strRow3+="c"
        if entercount==3:
          strRow4+="c"
        if entercount==4:
          strRow5+="c"
        if entercount==5:
          strRow6+="c"
        sleep(3)

    # d
    if MyText == 'letter d':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[2]/div[3]') \
            .click()
        if entercount==0:
          strRow1+="d"
        if entercount==1:
          strRow2+="d"
        if entercount==2:
          strRow3+="d"
        if entercount==3:
          strRow4+="d"
        if entercount==4:
          strRow5+="d"
        if entercount==5:
          strRow6+="d"
        sleep(3)

    # e
    if MyText == 'letter e':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[1]/div[3]') \
            .click() 
        if entercount==0:
          strRow1+="e"
        if entercount==1:
          strRow2+="e"
        if entercount==2:
          strRow3+="e"
        if entercount==3:
          strRow4+="e"
        if entercount==4:
          strRow5+="e"
        if entercount==5:
          strRow6+="e"  
        sleep(3)

    # f
    if MyText == 'letter f':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[2]/div[4]') \
            .click()
        if entercount==0:
          strRow1+="f"
        if entercount==1:
          strRow2+="f"
        if entercount==2:
          strRow3+="f"
        if entercount==3:
          strRow4+="f"
        if entercount==4:
          strRow5+="f"
        if entercount==5:
          strRow6+="f"
        sleep(3)

    # g
    if MyText == 'letter g':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[2]/div[5]') \
            .click()
        if entercount==0:
          strRow1+="g"
        if entercount==1:
          strRow2+="g"
        if entercount==2:
          strRow3+="g"
        if entercount==3:
          strRow4+="g"
        if entercount==4:
          strRow5+="g"
        if entercount==5:
          strRow6+="g"
        sleep(3)

    # h
    if MyText == 'letter h':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[2]/div[6]') \
            .click()
        if entercount==0:
          strRow1+="h"
        if entercount==1:
          strRow2+="h"
        if entercount==2:
          strRow3+="h"
        if entercount==3:
          strRow4+="h"
        if entercount==4:
          strRow5+="h"
        if entercount==5:
          strRow6+="h"
        sleep(3)

    # i
    if MyText == 'letter i':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[1]/div[8]') \
            .click()
        if entercount==0:
          strRow1+="i"
        if entercount==1:
          strRow2+="i"
        if entercount==2:
          strRow3+="i"
        if entercount==3:
          strRow4+="i"
        if entercount==4:
          strRow5+="i"
        if entercount==5:
          strRow6+="i"
        sleep(3)

    # j
    if MyText == 'letter j':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[2]/div[7]') \
            .click()
        if entercount==0:
          strRow1+="j"
        if entercount==1:
          strRow2+="j"
        if entercount==2:
          strRow3+="j"
        if entercount==3:
          strRow4+="j"
        if entercount==4:
          strRow5+="j"
        if entercount==5:
          strRow6+="j"
        sleep(3)

    # k
    if MyText == 'letter k':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[2]/div[8]') \
            .click() 
        if entercount==0:
          strRow1+="k"
        if entercount==1:
          strRow2+="k"
        if entercount==2:
          strRow3+="k"
        if entercount==3:
          strRow4+="k"
        if entercount==4:
          strRow5+="k"
        if entercount==5:
          strRow6+="k"
        sleep(3)

    # l
    if MyText == 'letter l':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[2]/div[9]') \
            .click()
        if entercount==0:
          strRow1+="l"
        if entercount==1:
          strRow2+="l"
        if entercount==2:
          strRow3+="l"
        if entercount==3:
          strRow4+="l"
        if entercount==4:
          strRow5+="l"
        if entercount==5:
          strRow6+="l"
        sleep(3)

    # m
    if MyText == 'letter m':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[3]/div[8]') \
            .click()
        if entercount==0:
          strRow1+="m"
        if entercount==1:
          strRow2+="m"
        if entercount==2:
          strRow3+="m"
        if entercount==3:
          strRow4+="m"
        if entercount==4:
          strRow5+="m"
        if entercount==5:
          strRow6+="m"
        sleep(3)

    # n
    if MyText == 'letter n':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[3]/div[7]') \
            .click()
        if entercount==0:
          strRow1+="n"
        if entercount==1:
          strRow2+="n"
        if entercount==2:
          strRow3+="n"
        if entercount==3:
          strRow4+="n"
        if entercount==4:
          strRow5+="n"
        if entercount==5:
          strRow6+="n"
        sleep(3)

    # o
    if MyText == 'letter o':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[1]/div[9]') \
            .click()
        if entercount==0:
          strRow1+="o"
        if entercount==1:
          strRow2+="o"
        if entercount==2:
          strRow3+="o"
        if entercount==3:
          strRow4+="o"
        if entercount==4:
          strRow5+="o"
        if entercount==5:
          strRow6+="o"
        sleep(3)

    # p
    if MyText == 'letter p':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[1]/div[10]') \
            .click() 
        if entercount==0:
          strRow1+="p"
        if entercount==1:
          strRow2+="p"
        if entercount==2:
          strRow3+="p"
        if entercount==3:
          strRow4+="p"
        if entercount==4:
          strRow5+="p"
        if entercount==5:
          strRow6+="p"
        sleep(3)

    # q
    if MyText == 'letter q':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[1]/div[1]') \
            .click()
        if entercount==0:
          strRow1+="q"
        if entercount==1:
          strRow2+="q"
        if entercount==2:
          strRow3+="q"
        if entercount==3:
          strRow4+="q"
        if entercount==4:
          strRow5+="q"
        if entercount==5:
          strRow6+="q"
        sleep(3)

    # r
    if MyText == 'letter r':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[1]/div[4]') \
            .click() 
        if entercount==0:
          strRow1+="r"
        if entercount==1:
          strRow2+="r"
        if entercount==2:
          strRow3+="r"
        if entercount==3:
          strRow4+="r"
        if entercount==4:
          strRow5+="r"
        if entercount==5:
          strRow6+="r"
        sleep(3)

    # s
    if MyText == 'letter s':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[2]/div[2]') \
            .click()
        if entercount==0:
          strRow1+="s"
        if entercount==1:
          strRow2+="s"
        if entercount==2:
          strRow3+="s"
        if entercount==3:
          strRow4+="s"
        if entercount==4:
          strRow5+="s"
        if entercount==5:
          strRow6+="s"
        sleep(3)

    # t
    if MyText == 'letter t':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[1]/div[5]') \
            .click()
        if entercount==0:
          strRow1+="t"
        if entercount==1:
          strRow2+="t"
        if entercount==2:
          strRow3+="t"
        if entercount==3:
          strRow4+="t"
        if entercount==4:
          strRow5+="t"
        if entercount==5:
          strRow6+="t"
        sleep(3)

    # u
    if MyText == 'letter u':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[1]/div[7]') \
            .click() 
        if entercount==0:
          strRow1+="u"
        if entercount==1:
          strRow2+="u"
        if entercount==2:
          strRow3+="u"
        if entercount==3:
          strRow4+="u"
        if entercount==4:
          strRow5+="u"
        if entercount==5:
          strRow6+="u"
        sleep(3)

    # v
    if MyText == 'letter v':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[3]/div[5]') \
            .click()
        if entercount==0:
          strRow1+="v"
        if entercount==1:
          strRow2+="v"
        if entercount==2:
          strRow3+="v"
        if entercount==3:
          strRow4+="v"
        if entercount==4:
          strRow5+="v"
        if entercount==5:
          strRow6+="v"
        sleep(3)

    # w
    if MyText == 'letter w':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[1]/div[2]') \
            .click()
        if entercount==0:
          strRow1+="w"
        if entercount==1:
          strRow2+="w"
        if entercount==2:
          strRow3+="w"
        if entercount==3:
          strRow4+="w"
        if entercount==4:
          strRow5+="w"
        if entercount==5:
          strRow6+="w"
        sleep(3)

    # x
    if MyText == 'letter x':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[3]/div[3]') \
            .click()  
        if entercount==0:
          strRow1+="x"
        if entercount==1:
          strRow2+="x"
        if entercount==2:
          strRow3+="x"
        if entercount==3:
          strRow4+="x"
        if entercount==4:
          strRow5+="x"
        if entercount==5:
          strRow6+="x"
        sleep(3)

    # y
    if MyText == 'letter y':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[1]/div[6]') \
            .click()  
        if entercount==0:
          strRow1+="y"
        if entercount==1:
          strRow2+="y"
        if entercount==2:
          strRow3+="y"
        if entercount==3:
          strRow4+="y"
        if entercount==4:
          strRow5+="y"
        if entercount==5:
          strRow6+="y"
        sleep(3)

    # z
    if MyText == 'letter z':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[3]/div[2]') \
            .click() 
        if entercount==0:
          strRow1+="z"
        if entercount==1:
          strRow2+="z"
        if entercount==2:
          strRow3+="z"
        if entercount==3:
          strRow4+="z"
        if entercount==4:
          strRow5+="z"
        if entercount==5:
          strRow6+="z"
        sleep(3)

    # backspace
    if MyText == 'delete the letter':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[3]/div[1]') \
            .click()
        if entercount==0:
          strRow1[:-1]
        if entercount==1:
          strRow2[:-1]
        if entercount==2:
          strRow3[:-1]
        if entercount==3:
          strRow4[:-1]
        if entercount==4:
          strRow5[:-1]
        if entercount==5:
          strRow6[:-1]
        sleep(3)


    #checks if the hexcode of the guess is yellow, green, or grey (for misplaced, correct, and wrong letters) and Speaks the text accordingly
    # enter
    if MyText == 'enter the word':
        driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[6]/div[3]/div[9]') \
            .click()
        sleep(3)
        rgb1 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[1]/div[1]').value_of_css_property('background-color')
        hex1 = Color.from_string(rgb1).hex
        if hex1 == ("#79b851"):
          SpeakText(strCorrect)
          recall1="Correct"
        if hex1 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall1="Elsewhere"
        if hex1 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall1="Incorrect"
          
        rgb2 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[1]/div[2]').value_of_css_property('background-color')
        hex2 = Color.from_string(rgb2).hex
        if hex2 == ("#79b851"):
          SpeakText(strCorrect)
          recall2="Correct"
        if hex2 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall2="Elsewhere"
        if hex2 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall2="Incorrect"
        
        rgb3 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[1]/div[3]').value_of_css_property('background-color')
        hex3 = Color.from_string(rgb3).hex
        if hex3 == ("#79b851"):
          SpeakText(strCorrect)
          recall3="Correct"
        if hex3 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall3="Elsewhere"
        if hex3 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall3="Incorrect"
          
        rgb4 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[1]/div[4]').value_of_css_property('background-color')
        hex4 = Color.from_string(rgb4).hex
        if hex4 == ("#79b851"):
          SpeakText(strCorrect)
          recall4="Correct"
        if hex4 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall4="Elsewhere"
        if hex4 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall4="Incorrect"
        
        rgb5 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[1]/div[5]').value_of_css_property('background-color')
        hex5 = Color.from_string(rgb5).hex
        if hex5 == ("#79b851"):
          SpeakText(strCorrect)
          recall5="Correct"
        if hex5 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall5="Elsewhere"
        if hex5 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall5="Incorrect"
        
        rgb6 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[2]/div[1]').value_of_css_property('background-color')
        hex6 = Color.from_string(rgb6).hex
        if hex6 == ("#79b851"):
          SpeakText(strCorrect)
          recall6="Correct"
        if hex6 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall6="Elsewhere"
        if hex6 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall6="Incorrect"
        
        rgb7 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[2]/div[2]').value_of_css_property('background-color')
        hex7 = Color.from_string(rgb7).hex
        if hex7 == ("#79b851"):
          SpeakText(strCorrect)
          recall7="Correct"
        if hex7 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall7="Elsewhere"
        if hex7 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall7="Incorrect"
          
        rgb8 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[2]/div[3]').value_of_css_property('background-color')
        hex8 = Color.from_string(rgb8).hex
        if hex8 == ("#79b851"):
          SpeakText(strCorrect)
          recall8="Correct"
        if hex8 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall8="Elsewhere"
        if hex8 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall8="Incorrect"
        
        rgb9 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[2]/div[4]').value_of_css_property('background-color')
        hex9 = Color.from_string(rgb9).hex
        if hex9 == ("#79b851"):
          SpeakText(strCorrect)
          recall9="Correct"
        if hex9 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall9="Elsewhere"
        if hex9 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall9="Incorrect"
        
        rgb10 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[2]/div[5]').value_of_css_property('background-color')
        hex10 = Color.from_string(rgb10).hex
        if hex10 == ("#79b851"):
          SpeakText(strCorrect)
          recall10="Correct"
        if hex10 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall10="Elsewhere"
        if hex10 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall10="Incorrect"
        
        rgb11 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[3]/div[1]').value_of_css_property('background-color')
        hex11 = Color.from_string(rgb11).hex
        if hex11 == ("#79b851"):
          SpeakText(strCorrect)
          recall11="Correct"
        if hex11 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall11="Elsewhere"
        if hex11 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall11="Incorrect"
        
        rgb12 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[3]/div[2]').value_of_css_property('background-color')
        hex12 = Color.from_string(rgb12).hex
        if hex12 == ("#79b851"):
          SpeakText(strCorrect)
          recall12="Correct"
        if hex12 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall12="Elsewhere"
        if hex12 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall12="Incorrect"
          
        rgb13 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[3]/div[3]').value_of_css_property('background-color')
        hex13 = Color.from_string(rgb13).hex
        if hex13 == ("#79b851"):
          SpeakText(strCorrect)
          recall13="Correct"
        if hex13 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall13="Elsewhere"
        if hex13 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall13="Incorrect"
          
        rgb14 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[3]/div[4]').value_of_css_property('background-color')
        hex14 = Color.from_string(rgb14).hex
        if hex14 == ("#79b851"):
          SpeakText(strCorrect)
          recall14="Correct"
        if hex14 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall14="Elsewhere"
        if hex14 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall14="Incorrect"
          
        rgb15 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[3]/div[5]').value_of_css_property('background-color')
        hex15 = Color.from_string(rgb15).hex
        if hex15 == ("#79b851"):
          SpeakText(strCorrect)
          recall15="Correct"
        if hex15 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall15="Elsewhere"
        if hex15 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall15="Incorrect"
        
        rgb16 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[4]/div[1]').value_of_css_property('background-color')
        hex16 = Color.from_string(rgb16).hex
        if hex16 == ("#79b851"):
          SpeakText(strCorrect)
          recall16="Correct"
        if hex16 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall16="Elsewhere"
        if hex16 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall16="Incorrect"
          
        rgb17 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[4]/div[2]').value_of_css_property('background-color')
        hex17 = Color.from_string(rgb17).hex
        if hex17 == ("#79b851"):
          SpeakText(strCorrect)
          recall17="Correct"
        if hex17 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall17="Elsewhere"
        if hex17 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall17="Incorrect"
        
        rgb18 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[4]/div[3]').value_of_css_property('background-color')
        hex18 = Color.from_string(rgb18).hex
        if hex18 == ("#79b851"):
          SpeakText(strCorrect)
          recall18="Correct"
        if hex18 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall18="Elsewhere"
        if hex18 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall18="Incorrect"
        
        rgb19 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[4]/div[4]').value_of_css_property('background-color')
        hex19 = Color.from_string(rgb19).hex
        if hex19 == ("#79b851"):
          SpeakText(strCorrect)
          recall19="Correct"
        if hex19 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall19="Elsewhere"
        if hex19 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall19="Incorrect"
        
        rgb20 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[4]/div[5]').value_of_css_property('background-color')
        hex20 = Color.from_string(rgb20).hex
        if hex20 == ("#79b851"):
          SpeakText(strCorrect)
          recall20="Correct"
        if hex20 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall20="Elsewhere"
        if hex20 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall20="Incorrect"
        
        rgb21 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[5]/div[1]').value_of_css_property('background-color')
        hex21 = Color.from_string(rgb21).hex
        if hex21 == ("#79b851"):
          SpeakText(strCorrect)
          recall21="Correct"
        if hex21 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall21="Elswhere"
        if hex21 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall21="Incorrect"
        
        rgb22 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[5]/div[2]').value_of_css_property('background-color')
        hex22 = Color.from_string(rgb22).hex
        if hex22 == ("#79b851"):
          SpeakText(strCorrect)
          recall22="Correct"
        if hex22 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall22="Elswhere"
        if hex22 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall22="Incorrect"
        
        rgb23 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[5]/div[3]').value_of_css_property('background-color')
        hex23 = Color.from_string(rgb23).hex
        if hex23 == ("#79b851"):
          SpeakText(strCorrect)
          recall23="Correct"
        if hex23 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall23="Elswhere"
        if hex23 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall23="Incorrect"
        
        rgb24 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[5]/div[4]').value_of_css_property('background-color')
        hex24 = Color.from_string(rgb24).hex
        if hex24 == ("#79b851"):
          SpeakText(strCorrect)
          recall24="Correct"
        if hex24 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall24="Elswhere"
        if hex24 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall24="Incorrect"
        
        rgb25 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[5]/div[5]').value_of_css_property('background-color')
        hex25 = Color.from_string(rgb25).hex
        if hex25 == ("#79b851"):
          SpeakText(strCorrect)
          recall25="Correct"
        if hex25 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall25="Elswhere"
        if hex25 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall25="Incorrect"
        
        rgb26 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[6]/div[1]').value_of_css_property('background-color')
        hex26 = Color.from_string(rgb26).hex
        if hex26 == ("#79b851"):
          SpeakText(strCorrect)
          recall26="Correct"
        if hex26 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall26="Elswhere"
        if hex26 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall26="Incorrect"
        
        rgb27 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[6]/div[2]').value_of_css_property('background-color')
        hex27 = Color.from_string(rgb27).hex
        if hex27 == ("#79b851"):
          SpeakText(strCorrect)
          recall27="Correct"
        if hex27 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall27="Elswhere"
        if hex27 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall27="Incorrect"
        
        rgb28 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[6]/div[3]').value_of_css_property('background-color')
        hex28 = Color.from_string(rgb28).hex
        if hex28 == ("#79b851"):
          SpeakText(strCorrect)
          recall28="Correct"
        if hex28 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall28="Elswhere"
        if hex28 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall28="Incorrect"
        
        rgb29 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[6]/div[4]').value_of_css_property('background-color')
        hex29 = Color.from_string(rgb29).hex
        if hex29 == ("#79b851"):
          SpeakText(strCorrect)
          recall29="Correct"
        if hex29 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall29="Elswhere"
        if hex29 == ("#a4aec4"):
          SpeakText(strIncorrect)
          recall29="Elswhere"
          
        rgb30 = driver.find_element_by_xpath('//*[@id="game-wrapper"]/div[1]/div[6]/div[5]').value_of_css_property('background-color')
        hex30 = Color.from_string(rgb30).hex
        if hex30 == ("#79b851"):
          SpeakText(strCorrect)
          recall30="Correct"
        if hex30 == ("#f3c237"):
          SpeakText(strElseWhere)
          recall30="Elswhere"
        if hex30 == ("#a4aec4"):
          SpeakText(strIncorrect) 
          recall30="Incorrect"
        entercount+=1  
        sleep(3)

     #code for the recall functionality that states the word for a certain row and speaks the correct-status of the guess   
    if MyText=="recall line number 1" or MyText=="recall line number one":
      SpeakText(strRow1)
      SpeakText(recall1)
      SpeakText(recall2)
      SpeakText(recall3)
      SpeakText(recall4)
      SpeakText(recall5)

    if MyText=="recall line number 2" or MyText=="recall line number two":
      SpeakText(strRow2)
      SpeakText(recall6)
      SpeakText(recall7)
      SpeakText(recall8)
      SpeakText(recall9)
      SpeakText(recall10)

    if MyText=="recall line number 3" or MyText=="recall line number three":
      SpeakText(strRow3)
      SpeakText(recall11)
      SpeakText(recall12)
      SpeakText(recall13)
      SpeakText(recall14)
      SpeakText(recall15)

    if MyText=="recall line number 4" or MyText=="recall line number four":
      SpeakText(strRow4)
      SpeakText(recall16)
      SpeakText(recall17)
      SpeakText(recall18)
      SpeakText(recall19)
      SpeakText(recall20)

    if MyText=="recall line number 5" or MyText=="recall line number five":
      SpeakText(strRow5)
      SpeakText(recall21)
      SpeakText(recall22)
      SpeakText(recall23)
      SpeakText(recall24)
      SpeakText(recall25)

    if MyText=="recall line number 6" or MyText=="recall line number six":
      SpeakText(strRow6)
      SpeakText(recall26)
      SpeakText(recall27)
      SpeakText(recall28)
      SpeakText(recall29)
      SpeakText(recall30)
