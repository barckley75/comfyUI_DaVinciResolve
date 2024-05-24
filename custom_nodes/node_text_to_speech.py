import folder_paths
import os
from openai import OpenAI

class TextToSpeech:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text_prompt": ("STRING", {
                    "multiline": True,
                    "default": "Enter your text here"}),
                "voice": (['nova', 'shimmer', 'echo', 'onyx', 'fable', 'alloy'],),
                "filename": ("STRING", {"default": "output"}),
            },
        }

    RETURN_TYPES = ("AUDIO", )
    FUNCTION = "generate_tts"
    OUTPUT_NODE = True
    CATEGORY = "audio"

    def generate_tts(self, text_prompt, voice, filename):
        try:
            os.environ["OPENAI_API_KEY"] = "Your_OpenAI_Key"
            client = OpenAI()
            if text_prompt and filename:
                speech_file_path = os.path.join(self.output_dir, f"{filename}.mp3")
                response = client.audio.speech.create(
                    model="tts-1",
                    voice=voice,
                    input=text_prompt
                )
                response.stream_to_file(speech_file_path)
                print(f'Audio generated and saved to {speech_file_path}')
                return (speech_file_path,)
            else:
                print("Text prompt or filename is missing.")
                return None
        except Exception as e:
            print(f"An error occurred while generating TTS: {e}")
            return None

NODE_CLASS_MAPPINGS = {
    "TextToSpeech": TextToSpeech
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TextToSpeech": "Text to Speech"
}
