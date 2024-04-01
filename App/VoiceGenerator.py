from elevenlabs.client import ElevenLabs
from elevenlabs import play

class VoiceGenerator:
    def __init__(self, apikey):
        self.client = ElevenLabs(api_key=apikey)  

    # Generate voice
    def generate_voice(self, text, voice_name, model_name):
        audio = self.client.generate(
            text=text,
            voice=voice_name,
            model=model_name
        )
        return audio