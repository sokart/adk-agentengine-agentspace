from google.adk.agents import SequentialAgent

from agent_maths.agent import agent_math
from agent_grammar.agent import agent_grammar
from agent_summary.agent import agent_summary

root_agent = SequentialAgent(
        name="agent_teaching_assistant",
        description="This agent acts as a friendly teaching assistant, checking the grammar of kids' questions, performing math calculations using corrected or original text (if grammatically correct), and providing results or grammar feedback in a friendly tone.",
        sub_agents=[agent_grammar, agent_math, agent_summary],
    )

    