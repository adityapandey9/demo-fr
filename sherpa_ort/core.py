# import time
# import sherpa_onnx
# import soundfile as sf

# start_total = time.time()

# args = {
#     "vits_model": "./model.onnx",
#     "vits_lexicon": "",
#     "vits_tokens": "./tokens.txt",
#     "vits_data_dir": "./espeak-ng-data",
#     "vits_dict_dir": "",
#     "tts_rule_fsts": "",
#     "max_num_sentences": 100,
#     "output_filename": "./generated.wav",
#     "sid": 0,
#     "debug": False,
#     "provider": "cuda",
#     "num_threads": 4,
#     "speed": 1.0,
# }

# text = """
# Welcome to Bytesflow, your reliable Text-to-Speech SaaS application. Powered by state-of-the-art technology, we aim to convert your text into high-quality, realistic audio seamlessly. Our service prioritizes speed, accuracy, and privacy, ensuring your data is handled securely in compliance with Indian laws.
# """

# tts_config = sherpa_onnx.OfflineTtsConfig(
#     model=sherpa_onnx.OfflineTtsModelConfig(
#         vits=sherpa_onnx.OfflineTtsVitsModelConfig(
#             model=args["vits_model"],
#             lexicon=args["vits_lexicon"],
#             data_dir=args["vits_data_dir"],
#             dict_dir=args["vits_dict_dir"],
#             tokens=args["vits_tokens"],
#         ),
#         provider=args["provider"],
#         debug=args["debug"],
#         num_threads=args["num_threads"],
#     ),
#     rule_fsts=args["tts_rule_fsts"],
#     max_num_sentences=args["max_num_sentences"],
# )
# if not tts_config.validate():
#     raise ValueError("Please check your config")

# tts = sherpa_onnx.OfflineTts(tts_config)

# end_total = time.time()
# total_elapsed_seconds = end_total - start_total

# start = time.time()
# audio = tts.generate(
#     text,
#     sid=args["sid"],
#     speed=args["speed"],
# )
# end = time.time()

# if len(audio.samples) == 0:
#     print("Error in generating audios. Please read previous error messages.")
# else:
#     elapsed_seconds = end - start
#     audio_duration = len(audio.samples) / audio.sample_rate
#     real_time_factor = elapsed_seconds / audio_duration

#     sf.write(
#         args["output_filename"],
#         audio.samples,
#         samplerate=audio.sample_rate,
#         subtype="PCM_16",
#     )
#     print(f"Text size: {len(text)}")
#     print(f"Saved to {args['output_filename']}")
#     print(f"Elapsed seconds: {elapsed_seconds:.3f}")
#     print(f"Audio duration in seconds: {audio_duration:.3f}")
#     print(f"RTF: {elapsed_seconds:.3f}/{audio_duration:.3f} = {real_time_factor:.3f}")
#     # play_audio(f"{args['output_filename']}")


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

from .utils import get_current_dir
import os

def load_model():
    """
    Load the model file from the assets directory.
    """
    current_dir = get_current_dir()
    asset_path = os.path.join(current_dir, 'assets', 'model_file.bin')
    print(f"Loading model from: {asset_path}")
    if not os.path.exists(asset_path):
        raise FileNotFoundError(f"Model file not found at {asset_path}")
    with open(asset_path, 'rb') as f:
        model_data = f.read()
    return model_data

def does_file_exist(file_name: str):
    """
    Check the file if exists from the assets directory.
    """
    current_dir = get_current_dir()
    asset_path = os.path.join(current_dir, 'assets', file_name)
    print(f"Loading model from: {asset_path}")
    if not os.path.exists(asset_path):
        raise FileNotFoundError(f"Model file not found at {asset_path}")
    return True

def print_assets_structure():
    """
    Print the structure of the assets folder with absolute paths and check if files exist.    
    """
    current_dir = get_current_dir()
    asset_path = os.path.join(current_dir, 'assets')
    paths = []
    for root, dirs, files in os.walk(asset_path):
        print(f"Directory: {os.path.abspath(root)}")
        
        # Check subdirectories
        for d in dirs:
            dir_path = os.path.join(root, d)
            exists = os.path.exists(dir_path)
            paths.append(f"  Subdirectory: {os.path.abspath(dir_path)} - {'Exists' if exists else 'Missing'}")
        
        # Check files
        for f in files:
            file_path = os.path.join(root, f)
            exists = os.path.exists(file_path)
            paths.append(f"  File: {os.path.abspath(file_path)} - {'Exists' if exists else 'Missing'}")
    return paths
