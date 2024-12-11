import wave
import lameenc
import os

def get_current_dir() -> str:
    return os.path.dirname(__file__)
    
def get_word_timestamps(audio_file, text):
    # Open the audio file and get its duration
    with wave.open(audio_file, "rb") as audio:
        frame_rate = audio.getframerate()
        n_frames = audio.getnframes()
        audio_duration = n_frames / float(frame_rate)

    # Split the text into words
    words = text.split()
    total_words = len(words)

    # Calculate the delay (duration) per word
    if total_words > 0:
        word_duration = audio_duration / total_words
    else:
        word_duration = 0

    # Create the array to store word data
    word_timestamps = []
    current_time = 0.0

    for index, word in enumerate(words):
        start_time = current_time
        end_time = current_time + word_duration
        word_timestamps.append({
            "word": word,
            "start": round(start_time, 3),  # Start time in seconds
            "end": round(end_time, 3),      # End time in seconds
            "score": 1.0,                   # Default confidence score
            "text_offset": index            # Word position in text
        })
        current_time = end_time

    return word_timestamps


def convert_wav_to_mp3(wav_file, mp3_file):
    # Open the WAV file
    with wave.open(wav_file, 'rb') as wav:
        # Get audio parameters
        nchannels = wav.getnchannels()
        sampwidth = wav.getsampwidth()
        framerate = wav.getframerate()
        nframes = wav.getnframes()

        # Read audio data
        audio_data = wav.readframes(nframes)

    # Initialize LAME encoder
    encoder = lameenc.Encoder()
    encoder.set_bit_rate(128)
    encoder.set_in_sample_rate(framerate)
    encoder.set_channels(nchannels)
    encoder.set_quality(2)  # 2 = High quality, slow speed

    # Encode to MP3
    mp3_data = encoder.encode(audio_data)
    mp3_data += encoder.flush()

    # Save the MP3 file
    with open(mp3_file, 'wb') as mp3:
        mp3.write(mp3_data)

    print(f"Conversion successful: {mp3_file}")
