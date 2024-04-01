from imports import *

class StoryGenerator:
    def __init__(self, model_name_or_path):
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name_or_path)
        self.model = GPT2LMHeadModel.from_pretrained(model_name_or_path)

    def generate_story(self, theme, num_sentences):
        input_ids = self.tokenizer.encode(theme, return_tensors='pt')
        max_length = num_sentences * 50  # Adjust the length based on the desired number of sentences

        # Generate text
        output = self.model.generate(input_ids, max_length=max_length, num_return_sequences=1, temperature=0.7)

        # Decode and format generated text
        generated_text = self.tokenizer.decode(output[0], skip_special_tokens=True)
        sentences = nltk.sent_tokenize(generated_text)
        sentences = sentences[:num_sentences]  # Ensure exactly num_sentences are returned
        story = ' '.join(sentences)

        return story
