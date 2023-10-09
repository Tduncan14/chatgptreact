import json
import random

#Get recent messages

def get_recent_messages():

    #define the file name
    file_name = "stored_data.json"
    learn_instruction ={
        "role":"system",
        "content":"You are interviewing me for a job as a retail assitant, Ask short questions for the position. Your name is John. Keep your answers under 30 seconds"
    }
    
    #initialize messages


    messages = []

    #Add a random element
    x = random.uniform(0,1)
    if x < 0.5:
        learn_instruction["content"] = learn_instruction["content"] + "Your response will include some dry humor."
    else: 
        learn_instruction["content"] = learn_instruction["content"] + "Your response will include a rather challenging question"

    # append instruction to messages
    messages.append(learn_instruction)


    # Get last messages

    try:
        with open(file_name) as user_file:
            data = json.load(user_file)

            # Appended the last 5 items of data
             
            if data:
                if len(data) < 5:
                  for item in data:
                    messages.append(item)
                else:
                    for item in data[-5:]:
                        messages.append(item)


    except Exception as e:
            print(e)
            pass
    

    #Return messages
    return messages


