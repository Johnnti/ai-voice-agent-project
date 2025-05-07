import os
import json
import openai 
from dotenv import load_dotenv
from deepgram import DeepgramClient, PrerecordedOptions, SpeakOptions

load_dotenv()

DP_API_KEY = os.getenv('DEEPGRAM_VOICE_AGENT_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_LLM_KEY')