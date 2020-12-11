import dialogflow_v2 as dialogflow
import requests
import os
from dotenv import load_dotenv
import json
load_dotenv()
GOOGLE_APPLICATION_CREDENTIALS=os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
PROJECT_ID=os.getenv('PROJECT_ID')
url = 'https://dvmn.org/media/filer_public/a7/db/a7db66c0-1259-4dac-9726-2d1fa9c44f20/questions.json'


def creating_intent(url):
    #Creating list of intents in requiring format
    data = requests.get(url).json()
    intents = []
    for k,v in data.items():
        intents.append({
        "display_name":k,
        "messages":[{"text":{"text":[v["answer"]]}}],
        "training_phrases":[{"parts":[{"text":value}]} for value in v["questions"]]
        })
    return intents
    
def make_intent(project_id):
    #send formating intent to dialogflow
    client = dialogflow.IntentsClient()
    parent = client.project_agent_path(project_id)
    intents = creating_intent(url)
    for intent in intents:
        response = client.create_intent(parent,intent)
    

def train_agent(project_id):
    client = dialogflow.AgentsClient()
    parent = parent = client.project_path(project_id)
    response = client.train_agent(parent)
    def callback(operation_future):
        result = operation_future.result()
    response.add_done_callback(callback)
    metadata = response.metadata()
if __name__ == "__main__":
    make_intent(PROJECT_ID)
    #train_agent(PROJECT_ID)
    
