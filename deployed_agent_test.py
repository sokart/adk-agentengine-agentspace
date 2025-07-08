import os
import vertexai
from vertexai import agent_engines

from dotenv import load_dotenv
load_dotenv()

def parse_event_content(event: dict) -> list:
    """
    Parses the 'content' section of an event dictionary to extract text,
    function calls, or function responses from the 'parts' list.

    Args:
        event: The event dictionary to parse.

    Returns:
        A list of tuples. Each tuple contains (events type, content)
        Returns an empty list if the structure is invalid or no 
        relevant parts are found.
    """
    results = []
    
    # Use .get() for safer access in case keys are missing
    content = event.get('content')
    if not isinstance(content, dict):
        # print("Warning: 'content' key missing or not a dictionary in event.")
        return results # Return empty list if content is missing/wrong type

    parts = content.get('parts')
    if not isinstance(parts, list):
        # print("Warning: 'parts' key missing or not a list in event['content'].")
        return results # Return empty list if parts is missing/wrong type

    # Iterate through each dictionary in the 'parts' list
    for part in parts:
        if not isinstance(part, dict):
            # print(f"Warning: Item in 'parts' is not a dictionary: {part}")
            results.append(('unknown', part)) # Handle non-dict items if necessary
            continue # Skip to the next item

        if 'text' in part:
            print("-----------------------------")
            print('>>> Inside final response <<<')
            print("-----------------------------")
            print(part['text'])
            results.append(('text', part['text']))
        elif 'function_call' in part:
            print("-----------------------------")
            print('+++ Inside function call +++')
            print("-----------------------------")
            print(f"Call Function: {part['function_call']['name']}")
            print(f"Argument: {part['function_call']['args']}")
            # Found a function call part
            results.append(('function_call', part['function_call']))
        elif 'function_response' in part:
            print("------------------------------")
            print('-- Inside function response --')
            print("------------------------------")
            print(f"Function Response: {part['function_response']['name']}")
            print(f"Response: {part['function_response']['response']}")
            results.append(('function_response', part['function_response']))
        else:
            # The part dictionary doesn't contain any of the expected keys
            # print(f"Warning: Unknown structure in part: {part}")
            print(f'Unknown part: {part}')
            results.append(('unknown', part))

    return results

if __name__ == '__main__':
    GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT")
    GOOGLE_CLOUD_LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION")

    AGENT_ENGINE_ID = 'PLACEHOLDER - REPLACE WITH YOUR AGENT ENGINE ID' # Normally a 18-digit number - it is a number not a string 
    
    vertexai.init(
        project=GOOGLE_CLOUD_PROJECT,
        location=GOOGLE_CLOUD_LOCATION,
    )

    
    print("--------------------------")
    print("---- Get Agent Engine ----")
    print("--------------------------")
    agent = agent_engines.get(f"projects/{GOOGLE_CLOUD_PROJECT}/locations/{GOOGLE_CLOUD_LOCATION}/reasoningEngines/{AGENT_ENGINE_ID}")
    print(f"Agent Retrieved: {agent.display_name}")

    print("\n-------------------------")
    print("---- Send User Query ----")
    print("-------------------------")
    user_query = "Hi teacher. Could she help me to multiply all the numbers between 1 and 10 and then add 5?"
    
    print(f"User query: {user_query}")

    for event in agent.stream_query(user_id="user", message=user_query):
        parse_event_content(event)