from setuptools import setup, find_packages

setup(
    name='sherpa_ort',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,  # Include non-code files
    package_data={
        'sherpa_ort': [
            'assets/**/*',
            # 'assets/model_file.bin',
        ],  # Include assets folder
    },
    install_requires=[
        'wave',
        'lameenc',
        'sherpa_onnx',
    ],
    description='A demo library that loads a model and uses the soundfile library.',
    author='Your Name',
    author_email='your_email@example.com',
)

