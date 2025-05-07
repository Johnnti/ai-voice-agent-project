import os
import json
import openai 
from dotenv import load_dotenv
from deepgram import DeepgramClient, PrerecordedOptions, SpeakOptions

load_dotenv()

DG_API_KEY = os.getenv('DEEPGRAM_VOICE_AGENT_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_LLM_KEY')

if not DG_API_KEY or not OPENAI_API_KEY:
    raise ValueError("Please set the DG_API_KEY and/or OPEN_API_KEY environment variable.")

#initialize the clients

deepgram = DeepgramClient(DG_API_KEY)
openai_client = openai.OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY')
)


#Define the system prompt for OpenAI
system_prompt = """
You are a helpful and friendly customer service assistant for a cell phone provider.
Your goal is to help customers with issues like:
-Billing questions
-Troubleshooting their mobile devices
-Activating or deactivating services
-Transferring them to appropriate departments for further assistance

Maintain a polite and professional tone in yuor responses. Always make the customer feel valued and heard.
"""
#set speech to text options
text_options = PrerecordedOptions(
    model = "nova-2",
    language="en",
    summarize="v2",#generate a short summary
    topics=True,#identify topics discussed
    intents=True,#detect the user's intent
    smart_format=True,#enable smart formatting for punctuation and capitalization
    sentiment=True,#analyze the sentiment of the speaker
)

#set text-to-speech options
speak_options = SpeakOptions(
    model="aura-asteria-en",
    encoding="linear16",#audio encoding
    container="wav" #audio container
)


#query Chatgpt
def ask_openai(prompt):
    """
    Send OpenAI API a prompt, returns a response back.
    """
    try:
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role":"system", "content": system_prompt},
                {"role":"user", "content": prompt}
            ],
            temperature=0.7#controls the randomness of the response
        )
        return response.choices[0].message.content
    except openai.error.OpenAIError as e:
        return f"An error occurred: {e}"
    
