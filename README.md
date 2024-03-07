# Speech Recognition Project

This project utilizes the `speech_recognition` library to convert speech from audio files into text. It's designed to process `.wav` audio files, extracting the spoken content and exporting the transcribed text to an Excel file.

## Prerequisites

Before you run this project, ensure you have the following installed:
- Python 3.x
- pandas: `pip install pandas`
- speech_recognition: `pip install SpeechRecognition`
- PyAudio: `pip install PyAudio` (you might need this for `speech_recognition` to work properly)


## Running the Script

To run the script, you need to have `.wav` audio files in the same directory as your script. 

1. Place your `.wav` audio files into the `./` directory (or modify the `directory` variable in the script to point to your audio files location).
2. Run the script using:

## Output

The script will create a DataFrame with the filenames and their corresponding transcribed text. If an audio file cannot be transcribed, an error message will be printed to the console.

An Excel file named `output_voice_to_text.xlsx` will be generated in the root directory, containing the results of the transcription.

## Troubleshooting

- If the audio cannot be recognized, ensure the `.wav` file is not corrupted and the speech is clear.
- In case of any `RequestError`, check your internet connection or try increasing the timeout for the recognition service.

## Contributions

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## Contact

If you have any questions or feedback, please reach out to me.
