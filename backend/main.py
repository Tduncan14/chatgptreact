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
@app.get("/post-audio-get/")
async def get_audio():
    # get saved audio
    audio_input = open("voice.mp3" ,'rb')

    #decode audio
    message_decoded = convert_audio_to_text(audio_input)

    #store messages


    print(message_decoded)

    #Guard" Ensure message decoded

    if not message_decoded:
       return HTTPException(status_code=400,detail="failed to decode audio")
    
    #Get chatpt response
    chat_reponse = get_chat_response(message_decoded)

    #store messages

    store_messages(message_decoded,chat_reponse)


    print(chat_reponse)
       
    
    return "done"

# @app.post("/post-audio/")
# async def post_audio(file:UploadFile = File(...)):
#  print('hello')




# @app.get('/wealthy')
# async def check_wealthy():
#      return{"message":"wealthy"}


