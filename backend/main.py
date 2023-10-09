#uvicorin main:app
#uvicorn main:app --reload

from fastapi import FastAPI, File,UploadFile,HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai


#custrom Functions import
#....
from functions.database import store_messages,reset_messages
from functions.openai_requests import convert_audio_to_text,get_chat_response
from functions.text_to_speech import convert_text_to_speech


openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")



#Initiate App



app = FastAPI()



#Cors -origin


origins = [
    "http://localhost:5173"
    "http://localhost:5174"
    "http://localhost:4173"
    "http://localhost:4174"
    "http://localhost:3000"
]


# corss middle ware {
# }

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# check healthy
@app.get("/")
async def check_health():
    print('this is treek')
    return {"message": "healthy"}



#reset messages
@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"message": "conversation reset"}



# post reponse
# Not playing in browser when using post request return audio


#Get audio
@app.post("/post-audio-get/")
async def post_audio(file:UploadFile=File(...)):

    # Convert audio to text - production
    # Save the file temporarily

    # audio_input = open("voice.mp3", "rb")

    #save file from frontend
    with open(file.filename,"wb") as buffer:
        buffer.write(file.file.read())
    audio_input = open(file.filename,"rb")

    # Decode audio
    message_decoded = convert_audio_to_text(audio_input)

    # Guard: Ensure output
    if not message_decoded:
        raise HTTPException(status_code=400, detail="Failed to decode audio")

    # Get chat response
    chat_response = get_chat_response(message_decoded)

    # Store messages
    store_messages(message_decoded, chat_response)

    # Guard: Ensure output
    if not chat_response:
        raise HTTPException(status_code=400, detail="Failed chat response")

    # Convert chat response to audio
    audio_output = convert_text_to_speech(chat_response)

    # Guard: Ensure output
    if not audio_output:
        raise HTTPException(status_code=400, detail="Failed audio output")

    # Create a generator that yields chunks of data
    def iterfile():
        yield audio_output

    # Use for Post: Return output audio
    return StreamingResponse(iterfile(), media_type="application/octet-stream")