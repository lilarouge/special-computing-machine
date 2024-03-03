from tkinter import S
import assemblyai as aai
import translators as ts

#Using Assemblyai to transcribe to txt and store it in a file 
aai.settings.api_key = "6b24538f918e45d7a4564f6413fbc3ee"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("/home/lilarouge/Documents/Atera translate/Atera's_Advanced_Reports_Demo.mp4")

#loop to make it more readable
with open('Atera_video.txt', 'w') as f:
    letters = []
    for letter in transcript.text:
        letters.append(letter)
        if letter == '.':
            letters.append('\n')
    f.write(''.join(letters))

# Translate to french
with open('Atera_video.txt', 'r') as data_file:
     
    with open('fr_Atera_video.txt', 'a') as output_file:
        go_to_line_fr=[] 

        for line_fr in data_file:
            go_to_line_fr.append(line_fr)
            if line_fr == '.':
                go_to_line_fr.append('\n')

            output_file.write(ts.translate_text(line_fr, to_language='fr'))

#translate to German
with open('Atera_video.txt', 'r') as data_file_de:    
    with open('de_Atera_video.txt', 'a') as output_file_de:
        go_to_line_de=[] 

        for line_de in data_file_de:
            go_to_line_de.append(line_de)
            if line_de == '.':
                go_to_line_de.append('\n')

            output_file_de.write(ts.translate_text(line_de, to_language='de'))
