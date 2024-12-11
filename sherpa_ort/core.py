import time
import os
import io

import sherpa_onnx
import wave
from .utils import get_current_dir

def generate_audio(text):
    """
    Generate audio for a given text using the Sherpa-ONNX Offline TTS engine.

    Args:
    - text (str): The input text to convert to speech.

    Returns:
    - bytes: The generated audio in WAV format as an in-memory binary file.
    """
    current_dir = get_current_dir()
    args = {
        "vits_model": str(os.path.join(current_dir, 'assets', 'en_US-libritts_r-medium.ort')),
        "vits_lexicon": "",
        "vits_tokens": str(os.path.join(current_dir, 'assets', 'tokens.txt')),
        "vits_data_dir": str(os.path.join(current_dir, 'assets', 'espeak-ng-data')),
        "vits_dict_dir": "",
        "tts_rule_fsts": "",
        "max_num_sentences": 100,
        "sid": 0,
        "debug": False,
        "provider": "cuda",
        "num_threads": 4,
        "speed": 1.0,
    }

    # Configure the TTS engine
    tts_config = sherpa_onnx.OfflineTtsConfig(
        model=sherpa_onnx.OfflineTtsModelConfig(
            vits=sherpa_onnx.OfflineTtsVitsModelConfig(
                model=args["vits_model"],
                lexicon=args["vits_lexicon"],
                data_dir=args["vits_data_dir"],
                dict_dir=args["vits_dict_dir"],
                tokens=args["vits_tokens"],
            ),
            provider=args["provider"],
            debug=args["debug"],
            num_threads=args["num_threads"],
        ),
        rule_fsts=args["tts_rule_fsts"],
        max_num_sentences=args["max_num_sentences"],
    )

    # Validate configuration
    if not tts_config.validate():
        raise ValueError("Invalid TTS configuration. Please check your config.")

    # Initialize the TTS engine
    tts = sherpa_onnx.OfflineTts(tts_config)

    # Generate audio
    start = time.time()
    audio = tts.generate(
        text,
        sid=args["sid"],
        speed=args["speed"],
    )
    end = time.time()

    # Check if audio was generated successfully
    if len(audio.samples) == 0:
        raise RuntimeError("Error in generating audio. Please check your configuration.")

    # Calculate elapsed time and log details (optional)
    elapsed_seconds = end - start
    audio_duration = len(audio.samples) / audio.sample_rate
    real_time_factor = elapsed_seconds / audio_duration

    # Return the in-memory WAV file as bytes
    return [audio, elapsed_seconds, audio_duration, real_time_factor]


# print(f"Loading Model Elapsed seconds: {total_elapsed_seconds:.3f}")
# print(f"Total Elapsed seconds: {(time.time() - start_total):.3f}")
# # Example usage
# timestamps = get_word_timestamps(f"{args['output_filename']}", text)

# print(timestamps)
# # Print the results
# # for entry in timestamps:
# #     print(entry)

# # start = time.time()
# # convert_wav_to_mp3(f"{args['output_filename']}", "./generated.mp3")
# # print(f"Total Time to Convert seconds: {(time.time() - start):.3f}")