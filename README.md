# Google ADK Multi-Agent Demo: Teaching Assistant

This repository contains a demonstration of a multi-agent system built using the **Google Agent Development Kit (ADK)**. The project showcases the end-to-end lifecycle of an AI agent: development, local testing, deployment to **Vertex AI Agent Engine**, and exposure in **Google AgentSpace**.

The example implements a "Teaching Assistant" agent designed to help children by correcting their grammar and solving math problems.

<!-- **Watch the full video demo:**
[![Demo Video](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=VIDEO_ID)
*(Replace `VIDEO_ID` with the actual YouTube video ID)* -->

---

## 🚀 Overview

The goal of this project is to demonstrate how to build, orchestrate, and deploy a sophisticated multi-agent system using Google's latest generative AI tools. The core of the project is a `teaching-assistant-agent` that leverages several specialized sub-agents to handle a user's query.

### Key Features

- **Multi-Agent Architecture:** Composed of distinct agents, each with a specific responsibility (grammar, math, summarization).
- **Full Development Lifecycle:** Provides a complete example from local code to AgentEngine and a production-ready agent in AgentSpace.
- **Powerful Debugging:** Utilizes the ADK Web UI for local testing and tracing, providing clear visibility into agent interactions.

---

## 🏛️ Architecture

The system is orchestrated by the `agent_teaching_assistant`, which is a **Sequential Agent**. It processes a user's query by passing it through a chain of sub-agents.

**Flow:**
`User Prompt` -> `agent_teaching_assistant` (Root Agent)
1.  **`agent_grammar`**: Receives the initial prompt, checks for grammatical errors, and returns a corrected version of the text.
2.  **`agent_maths`**: Receives the corrected text, identifies any mathematical operations, and uses its tools (e.g., `multiply`, `add`) to calculate the result.
3.  **`agent_summary`**: Receives the outputs from the grammar and math agents and synthesizes a friendly, coherent, and helpful response for the user.


---

## 🛠️ Technology Stack

- **Framework:** [Google Agent Development Kit (ADK)](https://cloud.google.com/vertex-ai/docs/agent-builder/agents/adk/overview)
- **Language:** Python
- **AI/LLM:** Google Gemini Models (Gemini 2.5 Flash, Gemini 2.0 Flash)
- **Deployment & Hosting:** [Vertex AI Agent Engine](https://cloud.google.com/vertex-ai/docs/agent-builder/agent-engine/overview)
- **User-Facing Application:** [Google AgentSpace](https://blog.google/technology/ai/google-io-2024-gemini-agent-ai-assistant/)
- **Cloud Platform:** Google Cloud Platform (GCP)

---

## ⚙️ Getting Started

### Prerequisites

1.  Python 3.10+
2.  A Google Cloud Project with the Vertex AI API enabled.
3.  [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) installed and authenticated (`gcloud auth application-default login`).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/sokart/adk-agentengine-agentspace.git
    cd adk-agentengine-agentspace
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .adk_venv
    source .adk_venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install google-adk
    ```

4.  **Configure your environment:**
    Create a `.env` file and populate it with your GCP project details. You can use the provided `.env.example` as a template.
    ```env
    # Choose Model Backend: 0 -> ML Dev, 1 -> Vertex AI
    GOOGLE_GENAI_USE_VERTEXAI=1

    # Vertex AI backend config, uncomment and use
    GOOGLE_CLOUD_PROJECT="your-gcp-project-id"
    GOOGLE_CLOUD_LOCATION="us-central1"

    MODEL="gemini-2.5-flash"
    ```

---

## 🏃‍♀️ How to Run the Demo

This demo follows a three-step process, moving from local development to a fully deployed agent.

### Step 1: Local Development & Testing

The ADK provides a web-based interface for rapid testing and debugging.

1.  **Start the ADK Web server:**
    ```bash
    adk web
    ```
    This will start the server and provide a local URL, typically `http://127.0.0.1:8000`.

2.  **Test the agent:**
    - Open the URL in your browser.
    - From the "Select an agent" dropdown, choose `agent_teaching_assistant`.
    - Enter a prompt with a math question and some grammar mistakes, like:
      > Could you multiply for me all th enumbers between 1 and 10?
    - Observe the agent's step-by-step reasoning and final response. Use the **Trace** view to see the graph of agent interactions.


### Step 2: Deploy to Agent Engine

Once you are satisfied with the agent's local performance, you can deploy it to a scalable, managed environment on Vertex AI.

1.  **Run the deployment script:**
    The `deploy_agent_to_agentengine.py` script handles packaging the agent and deploying it.
    ```bash
    python deploy_agent_to_agentengine.py
    ```
    This process will take approximately 5-7 minutes. It packages the agent code, uploads it to a GCS bucket, and creates an Agent Engine instance.

2.  **Verify in Google Cloud Console:**
    - Navigate to **Vertex AI -> Agent Builder -> Agent Engine**.
    - You will see your `teaching-assistant-agent` listed. You can click on it to view metrics, deployment details, and API URLs.


### Step 3: Expose to AgentSpace

The final step is to make your deployed agent available in a user-facing application like AgentSpace.

1.  **Get the Reasoning Engine ID:**
    The ID is printed in the console at the end of the Step 2 deployment script, or you can find it in the Agent Engine dashboard URL.

2.  **Update and run the expose script:**
    - Open `expose_to_agentspace.sh` and ensure the `REASONING_ENGINE_ID` and other variables are set correctly.
    - Execute the script:
      ```bash
      source expose_to_agentspace.sh
      ```
    This script makes an API call to AgentSpace, registering your Agent Engine instance as a new custom agent.

3.  **Use the agent in AgentSpace:**
    - Go to your Google AgentSpace application.
    - Click on the "Agents" tab.
    - Your `teaching-assistant-agent` will now be available under the "From your organization" section.
    - Click on it to start a new conversation and interact with your fully deployed, end-to-end agent!

---

## 📂 Code Structure

```
.
├── agent_grammar/            # Agent for grammar checks
│   └── agent.py
├── agent_maths/              # Agent for math calculations
│   └── agent.py
├── agent_summary/            # Agent for summarizing results
│   └── agent.py
├── agent_teaching_assistant/ # The root orchestrator agent
│   └── agent.py
├── .env                      # Environment configuration file
├── deploy_agent_to_agentengine.py # Script to deploy to Agent Engine
├── expose_to_agentspace.sh   # Script to expose the agent in AgentSpace
└── README.md                 # This file
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).