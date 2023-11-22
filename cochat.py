import cohere
co = cohere.Client('OOiIxmYDAuXPtUjtjTPV9Gd6Spy4HSvyFtZMNb9p')

message = "Hello World"

################### streamlit #################################

#import streamlit as st

########################### Generate the Response #########################################
###########Call the endpoint via the co.chat() method, specifying the message and the model settings ###################

response = co.chat(
	message, 
	model="command", 
	temperature=0.9
)

answer = response.text

############### Use the previous message to continue the conversation #################################

chat_history = [
	{"user_name": "User", "text": "Hey!"},
	{"user_name": "Chatbot", "text": "Hey! How can I help you today?"},
]
message = "Can you tell me about LLMs?"

response = co.chat(
	message=message,
	chat_history=chat_history
)

answer = response.text

############################### Keeping track of responses ############################################

chat_history = []
max_turns = 10

for _ in range(max_turns):
	# get user input
	message = input("Send the model a message: ")
	
	# generate a response with the current chat history
	response = co.chat(
		message,
		temperature=0.8,
		chat_history=chat_history
	)
	answer = response.text
		
	print(answer)

	# add message and answer to the chat history
	user_message = {"user_name": "User", "text": message}
	bot_message = {"user_name": "Chatbot", "text": answer}
	
	chat_history.append(user_message)
	chat_history.append(bot_message)
    
    ################################ Documents Mode #########################################################


################################ example reply ###########################################

{  
    "response_id": "ea9eaeb0-073c-42f4-9251-9ecef5b189ef",  
    "text": "The tallest penguins, Emperor penguins, live in Antarctica.",  
    "generation_id": "1b5565da-733e-4c14-9ff5-88d18a26da96",  
    "token_count": {  
        "prompt_tokens": 445,  
        "response_tokens": 13,  
        "total_tokens": 458,  
        "billed_tokens": 20  
    },  
    "meta": {  
        "api_version": {  
            "version": "2022-12-06"  
        }  
    },  
    "citations": [  
        {  
            "start": 22,  
            "end": 38,  
            "text": "Emperor penguins",  
            "document_ids": [  
                "doc_0"  
            ]  
        },  
        {  
            "start": 48,  
            "end": 59,  
            "text": "Antarctica.",  
            "document_ids": [  
                "doc_1"  
            ]  
        }  
    ],  
    "documents": [  
        {  
            "id": "doc_0",  
            "title": "Tall penguins",  
            "snippet": "Emperor penguins are the tallest.",  
            "url": ""  
        },  
        {  
            "id": "doc_1",  
            "title": "Penguin habitats",  
            "snippet": "Emperor penguins only live in Antarctica.",  
            "url": ""  
        }  
    ],  
    "search_queries": []  
}
