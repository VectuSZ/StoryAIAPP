from imports import *

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Image-Generator",
        page_icon=":camera",
        layout="wide",
    )

    model_name_or_path="C:/Users/mateu/gpt2"

    # Create ImageGenerator, StoryGenerator and VoiceGenerator instance
    image_generator = ImageGenerator(apikey=openai_apikey)
    story_generator = StoryGenerator(model_name_or_path=model_name_or_path)
    voice_generator = VoiceGenerator(apikey=elevenlabs_apikey)

    # Set title``
    st.markdown('<h1 class="title">Create your story!</h1>', unsafe_allow_html=True)

     # Load CSS file
    with open("Style/styles.css", "r") as file:
        css_code = file.read()

    # Apply CSS styles
    st.markdown(
        f'<style>{css_code}</style>',
        unsafe_allow_html=True
    )

    # User inputs
    user_input = st.text_input("Enter a description and app will create a story based on it")
    theme = "Tell an interesing and short (maximum 5 sentences) story about " + user_input
    num_of_sentences = st.number_input("Select number of images for your story", min_value=1, max_value=5, value=1)

    # Button to generate images
    if st.button("Generate Images and Voice"):
        # Generate story
        story = story_generator.generate_story(theme, num_of_sentences)
        audio = voice_generator.generate_voice(story, "Domi", "eleven_monolingual_v1")

        # Generate and display images
        generated_images = image_generator.generate_images(story)
        carousel(items=generated_images, width=1)
        # Play audio
        play(audio)
        # Print a story
        print(story)

if __name__ == "__main__":
    main()