def transcribe_streaming():
 
    # Instantiate a Speech client
    client = speech.SpeechClient()


    # Set the streaming configuration
streaming_config = types.StreamingRecognitionConfig(
        config=types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="en-US",
        ),
        interim_results=True,
    )


    # Create a generator to stream audio from the default microphone
    audio_generator = MicrophoneStream(
        sample_rate=streaming_config.config.sample_rate_hertz, 
        chunk_size=1024
    )


    # Create a generator to stream requests to the API
    requests = (types.StreamingRecognizeRequest(audio_content=content) 
                for content in audio_generator)
    
    # Stream audio to the Speech-to-Text API and process the responses
    responses = client.streaming_recognize(streaming_config=streaming_config, 
                                           requests=requests)


    # Loop through responses received from the server.
    for response in responses:
        if not response.results:
            continue
        result = response.results[0]
        if not result.alternatives:
            continue
        transcript = result.alternatives[0].transcript
        if result.is_final:
            print(f"Final transcript: {transcript}")
        else:
            print(f"Interim transcript: {transcript}")
