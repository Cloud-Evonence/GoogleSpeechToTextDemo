# Import speech module from google cloud package
from google.cloud import speech 


def transcribe_file(speech_file):


# Instantiate the SpeechClient class with default config and pass it to a variable client
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
    language_code="en-US",
    # Language code is an important input to reduce errors, eg: en-US, en-UK and en-IN
)


# Perform speech recognition on the audio file using the recognize() method of SpeechClass
response = client.recognize(config=config, audio=audio)


for result in response.results:
    # Print the transcription by selecting the first alternative result by index value [0]
    print("Transcript: {}".format(result.alternatives[0].transcript))
    # Confidence denotes API’s level of confidence that the transcribed text is accurate
    print("Confidence: {}".format(result.alternatives[0].confidence))
