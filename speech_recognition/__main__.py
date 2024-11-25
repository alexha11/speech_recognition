import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

# Store the play list song in a list of string

fin_song = ""

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something Duong!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

            # if the user said "exit", break out of the loop


            
              # this version of Python uses unicode for strings (Python 3+)
            if "play" in value :
                    fin = value.replace("play","",1)
                    fin = fin.replace(" ","",1)
                    fin_song = fin
            if value == "exit":
                    break
            print("You said {}".format(value))
            print("Song list: ", fin) 
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
