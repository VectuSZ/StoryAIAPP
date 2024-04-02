# Story AI App

## Overview
Story AI App is a Python program that runs on Streamlit. It lets you type in any topic, sentence, or word you want. Then, it creates a story using up to five pictures, you choose how many pictures you want to display. Plus, it reads the story out loud with a computer voice. It's like having your own personal storyteller!

## Features
- **Easy Input**: Input any theme, sentence, or word effortlessly to prompt the generation of a unique story.

- **Image-Based Narratives**: Create stories composed of up to five images selected by the user, adding visual depth to the narrative.

- **Immersive Experience**: Experience the story as it unfolds visually while an AI voice narrates the tale in the background, enhancing engagement.

- **Customization**: Tailor your storytelling experience by selecting the number and content of images used in your story.

- **Seamless Integration**: Utilizes Streamlit for a smooth and user-friendly interface, making the storytelling process intuitive and accessible.

- **Versatile Usage**: Ideal for inspiration, entertainment, or exploring the capabilities of AI-driven storytelling.

- **Creative Exploration**: Unleash your creativity and embark on imaginative journeys through dynamically generated narratives.

- **Accessible to All**: Designed to be inclusive and easy-to-use, regardless of technical expertise.

## Installation
To install the required dependencies for this project, run the following command in your terminal or command prompt:

1. Clone the repository to your local machine:
    ```
    git clone https://github.com/VectuSZ/StoryAIApp
    ```

2. Navigate to the project directory:
    ```
    cd StoryAIApp
    ```

3. You can do this by simply typing this command into your terminal:
    ```
    pip install -r requirements.txt
    ```

4. Before running an app you have to add apikey for two AI service:
 

 Firstly go to https://platform.openai.com/api-keys and create new secret key, or you the one you already used. Then go to apikey.py and paste this apikey to openai_apikey variable.

 Secondly go to https://elevenlabs.io/, go to profile + apikey and copy provided apikey to elevenlabs_apikey variable.

 For both apikey, you need to have account.


5. For proper usage of AI Voice Generation, you need to have installed ffmpeg on you computer and add this to your PATH variable. You can do this by following this tutorial: https://www.editframe.com/guides/how-to-install-and-start-using-ffmpeg-in-under-10-minutes

6. If everything is installed properly, you need to open terminal and put this command:
    ```
    streamlit run App/main.py
    ```

## Usage
1. When streamlit app is opened in your brower (usually on localhost:8501) it is ready to work.

2. Enter a word/sentence/theme to the first text field. Based on this app will generate a story and images.

3. Enter number of images you want to display (This many images your story will have) (Maximum number of images is 5 due to DallE limit)

4. Press "Generate images and voice" and wait a second until your story will be displayed in the bottom of the page and until you hear your story in a background.

   NOTE: If you are not using gpt2 model locally then you have to change model_name_or_path variable in main.py to "gpt2"
