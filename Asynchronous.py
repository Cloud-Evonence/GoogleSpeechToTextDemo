# Import speech module from google cloud package
from google.cloud import speech 


def transcribe_file(speech_file):
    # Instantiate the SpeechClient class with default config and pass it to a variable
    client = speech.SpeechClient()
    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()


    # Utilize the RecognitionAudio class to create an object audio
    audio = speech.RecognitionAudio(content=content)


    # Create a config object using the RecognitionConfig class of speech
    config = speech.RecognitionConfig(
    # Set audio encoding to LINEAR16 pcm type, audio sample captured per second to 16000
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
    # Language code is an important input to reduce errors, eg: en-US, en-UK and en-IN
        language_code="en-US",
    )
    # As stated above asynchronous transcription uses Long running operation
    operation = client.long_running_recognize(config=config, audio=audio)
    print("Waiting for operation to complete...")
    response = operation.result(timeout=90)
    for result in response.results:
        # Print the transcription and select the first alternative by index value [0]
        print("Transcript: {}".format(result.alternatives[0].transcript))
        # Based on your inputs you can have maximum 30 alternative transcription for an audio file
        print("Confidence: {}".format(result.alternatives[0].confidence))
