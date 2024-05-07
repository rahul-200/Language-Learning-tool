import boto3

def convert_text_to_speech(text, language_code='en-US', voice_id='Joanna'):
    """
    Convert input text to speech using Amazon Polly.
    
    Parameters:
    text (str): The text to be converted to speech.
    language_code (str): The language code (e.g., '[ar-AE, en-US, en-IN, es-MX, en-ZA, tr-TR, ru-RU, ro-RO, pt-PT, pl-PL, nl-NL, it-IT, is-IS, fr-FR, fi-FI, es-ES, de-DE, yue-CN, ko-KR, en-NZ, en-GB-WLS, hi-IN, arb, cy-GB, cmn-CN, da-DK, en-AU, pt-BR, nb-NO, sv-SE, ja-JP, es-US, ca-ES, fr-CA, en-GB, de-AT').
    voice_id (str): The voice ID (e.g., 'Joanna', 'Matthew', 'Celine').

    Returns:
    bytes: The audio stream in binary format.
    """
    try:
        # Initialize the Amazon Polly client with AWS credentials
        polly_client = boto3.client('polly', region_name='us-east-1')  # Replace 'us-east-1' with your AWS region

        # Request speech synthesis
        response = polly_client.synthesize_speech(Text=text,
                                                  OutputFormat='mp3',
                                                  VoiceId=voice_id,
                                                  LanguageCode=language_code)
        audio_stream = response['AudioStream'].read()
        return audio_stream
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def save_audio_to_file(audio_stream, output_file):
    """
    Save the audio stream to a file.
    
    Parameters:
    audio_stream (bytes): The audio stream in binary format.
    output_file (str): The path to save the audio file.
    """
    with open(output_file, 'wb') as f:
        f.write(audio_stream)

if _name_ == "_main_":
    text_to_convert = input("Enter text to convert to speech: ")
    language_code = input("Enter language code (e.g., en-US): ")
    voice_id = input("Enter voice ID (e.g., Joanna): ")

    audio_stream = convert_text_to_speech(text_to_convert,
                                          language_code=language_code,
                                          voice_id=voice_id)

    if audio_stream:
        output_file = "output.mp3"
        save_audio_to_file(audio_stream, output_file)
        print(f"Audio file saved as: {output_file}")
    else:
        print("Failed to convert text to speech.")
