import subprocess
import pyjokes

jokes=pyjokes.get_joke()
print("welcome to robospeaker:")
while(True):
    x=input("Enter what you want me to say:")
    if x=="Tell me a joke":
        command3=f'Add-Type -AssemblyName System.speech;$synthesizer = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer;$synthesizer.SelectVoice("Microsoft Zira Desktop");$synthesizer.Speak("{jokes}")'
        subprocess.run(["powershell", "-Command", command3], shell=True)
    elif x==";":
        command2='Add-Type -AssemblyName System.speech;$synthesizer = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer;$synthesizer.SelectVoice("Microsoft Zira Desktop");$synthesizer.Speak("Bye Bye Sir")'
        subprocess.run(["powershell", "-Command",command2 ], shell=True)
        break
    else:
        command=f'Add-Type -AssemblyName System.speech;$synthesizer = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer;$synthesizer.SelectVoice("Microsoft Zira Desktop");$synthesizer.Speak("{x}")'
        subprocess.run(["powershell", "-Command", command], shell=True)


# import subprocess
# import pyjokes

# jokes = pyjokes.get_joke()
# print("Welcome to Robospeaker:")

# while True:
#     x = input("Enter what you want me to say:")
#     if x.lower() == "tell me a joke":
#         command3 = f'Add-Type -AssemblyName System.speech;$synthesizer = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer;$synthesizer.SelectVoice("Microsoft Zira Desktop");$synthesizer.Speak("{jokes}")'
#         subprocess.run(["powershell", "-Command", command3])
#     elif x == ";":
#         command2 = 'Add-Type -AssemblyName System.speech;$synthesizer = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer;$synthesizer.SelectVoice("Microsoft Zira Desktop");$synthesizer.Speak("Bye Bye Sir")'
#         subprocess.run(["powershell", "-Command", command2])
#         break
#     else:
#         command = f'Add-Type -AssemblyName System.speech;$synthesizer = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer;$synthesizer.SelectVoice("Microsoft Zira Desktop");$synthesizer.Speak("{x}")'
#         subprocess.run(["powershell", "-Command", command])
