import os
import logging

from deepgram.utils import verboselogs

from deepgram import(
    DeepgramClient,
    SpeakOptions,
)
SPEAK_TEXT = {"text": "Hi, I’m reaching out because I noticed some unexpected charges on my phone bill this month, and I need some help figuring it out. My bill is usually pretty consistent, but this time, there’s an extra fee labeled as 'Additional Services' that I don’t recognize. I didn’t sign up for anything new, and I want to make sure I’m not being charged for something by mistake. Can you help me understand what’s going on and how we can fix it? Oh, and by the way, I also noticed that my last payment hasn’t been reflected yet—it looks like there might be a delay or an issue processing it. Could we check on that as well? Thanks for your help!"}

filename = "sample.mp3"

API_KEY = os.getenv("DG_API_KEY")

if not API_KEY:
    raise ValueError("Please set the DG_API_KEY environment variable.")

#create deepgram client 
deepgram = DeepgramClient(API_KEY)

#call save method on speak property
options = SpeakOptions(
    model='aura-asteria-en',
)

response = deepgram.speak.rest.v('1').save(filename, SPEAK_TEXT, options)

print(response.to_json(indent=4))
