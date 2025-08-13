export PROJECT_ID="PLACEHOLDER - REPLACE WITH YOUR GOOGLE CLOUD PROJECT ID" # String 
export PROJECT_NUMBER="PLACEHOLDER - REPLACE WITH YOUR GOOGLE CLOUD PROJECT NUMBER" # String 

export REASONING_ENGINE_ID="PLACEHOLDER - REPLACE WITH YOUR AGENT ENGINE ID" # String - Normally a 18-digit number
export REASONING_ENGINE_LOCATION="PLACEHOLDER - REPLACE WITH YOUR AGENT ENGINE LOCATION" # String - e.g. us-central1
export REASONING_ENGINE="projects/${PROJECT_ID}/locations/${REASONING_ENGINE_LOCATION}/reasoningEngines/${REASONING_ENGINE_ID}"


export AS_APP="PLACEHOLDER - REPLACE WITH YOUR AGENT SPACE APPLICATION ID" # String - Find it in Google Cloud AI Applications
export AS_LOCATION="PLACEHOLDER - REPLACE WITH YOUR AGENT SPACE APPLICATION LOCATION" # String - e.g. global, eu, us

export AGENT_DISPLAY_NAME="teaching-assistant-agent" # String - this will appear as the name of the agent into your AgentSpace
AGENT_DESCRIPTION=$(cat <<EOF
This agent acts as a friendly teaching assistant, checking the grammar of kids\' questions, performing math calculations using corrected or original text (if grammatically correct), and providing results or grammar feedback in a friendly tone.
EOF
)
export AGENT_DESCRIPTION

DISCOVERY_ENGINE_PROD_API_ENDPOINT="https://discoveryengine.googleapis.com"


deploy_agent_to_agentspace() {
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -H "x-goog-user-project: ${PROJECT_ID}" \
        ${DISCOVERY_ENGINE_PROD_API_ENDPOINT}/v1alpha/projects/${PROJECT_NUMBER}/locations/${AS_LOCATION}/collections/default_collection/engines/${AS_APP}/assistants/default_assistant/agents \
        -d '{
      "name": "projects/${PROJECT_NUMBER}/locations/${AS_LOCATION}/collections/default_collection/engines/${AS_APP}/assistants/default_assistant",
      "displayName": "'"${AGENT_DISPLAY_NAME}"'",
      "description": "'"${AGENT_DESCRIPTION}"'",
      "icon": {
        "uri": "https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/corporate_fare/default/24px.svg"
      },
      "adk_agent_definition": {
        "tool_settings": {
          "toolDescription": "'"${AGENT_DESCRIPTION}"'",
        },
        "provisioned_reasoning_engine": {
          "reasoningEngine": "'"${REASONING_ENGINE}"'"
        },
      }
    }'
}

deploy_agent_to_agentspace
