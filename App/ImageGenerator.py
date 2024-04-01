from imports import *

class ImageGenerator:
    def __init__(self, apikey):
        self.client = OpenAI(api_key=apikey)
        self.single_img = {
            "title": "",
            "text": "",
            "interval": None,
            "img": ""
        }

    # Generate images
    def generate_images(self, story):
        sentences = sent_tokenize(story)
        images = []
        counter = 1

        for sentence in sentences:
            img_response = self.client.images.generate(
                model="dall-e-3",
                prompt=sentence,
                size="1024x1024",
                quality="standard",
                n=1 
            )

            img_url = img_response.data[0].url
            new_img = self.single_img.copy()
            new_img["title"] = f"Image {counter}" 
            new_img["text"] = sentence
            new_img["img"] = img_url
            images.append(new_img)
            counter += 1

        return images