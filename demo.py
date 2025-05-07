import utils 
from deepgram import FileSource

AUDIO_FILE = "sample.mp3"

def main():
    try:
        with open(AUDIO_FILE, "rb") as file:
            buffer_data = file.read()
            
        customer_inquiry = utils.get_transcript(payload)
        
        transcribed_text = customer_inquiry['results']['channels'][0]['alternatives'][0]['transcript']
        agent_answer = utils.ask_openai(transcribed_text)
        
        
        utils.save_speech_summary(agent_answer)
    except Exception as e:
        print(f'Exception: {e}')
        

if __name__ == "__main__":
    main()