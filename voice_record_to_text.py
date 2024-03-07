import os
import pandas as pd
import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Specify the directory where your files are located
directory = "./"  # Adjust this path to the directory containing your .wav files

# Prepare a list to store the filenames and recognized text
data = []

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".wav"):
        try:
            # Use the audio file as the source
            with sr.AudioFile(os.path.join(directory, filename)) as source:
                # Listen for the data (load audio to memory)
                audio_data = recognizer.record(source)
                # Recognize (convert from speech to text)
                text = recognizer.recognize_google(audio_data, language='ar-AR')
                # Append filename and text to the list
                data.append({"Filename": filename, "Text": text})
        except sr.UnknownValueError:
            print(f"Could not understand audio for file {filename}")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

# Convert the list to a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Optional: Save the DataFrame to an Excel file
df.to_excel("output_voice_to_text46.xlsx", index=False)
