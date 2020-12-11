import dialogflow_v2 as dialogflow
from dotenv import load_dotenv
load_dotenv()
GOOGLE_APPLICATION_CREDENTIALS=os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

def detect_intent_texts(project_id, session_id, text, language_code='ru-RU'):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""
    
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
        session=session,
        query_input=query_input
    )

    return response.query_result.fulfillment_text