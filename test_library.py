from sherpa_ort.core import load_model, print_assets_structure

# Test loading the model
model_data = load_model()
print("Model Data Loaded:", model_data.decode('utf-8'))

print("Struct: ", print_assets_structure())

# Test generating audio info
# audio_info = generate_audio_info("test.wav")  # Replace with an actual .wav file path
# print("Audio Info:", audio_info)
