import os
from pydantic import BaseModel
from bark import SAMPLE_RATE, generate_audio, preload_models
import logging

os.environ["SUNO_OFFLOAD_CPU"] = "True"
os.environ["SUNO_USE_SMALL_MODELS"] = "True"
# download and load all models
preload_models()




class Prompt(BaseModel):

    prompt:str




async def process_prompt(prompt:str):
    """
    Process the given prompt and generate audio output.

    Args:
        prompt (str): The prompt string.

    Returns:
        str: The generated audio output.

    """
    assert prompt is not None
    output = generate_audio(prompt)

    return output


