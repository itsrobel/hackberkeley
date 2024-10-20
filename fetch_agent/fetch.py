from fetch_ai.agents.base import Agent

# from langchain_community.llms import GoogleGenerativeAI
from langchain_google_genai import ChatGoogleGenerativeAI

import os
import getpass

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)


# Replace with your actual API key and endpoint
# gemini_model = GoogleGenerativeAI(
#     api_key="YOUR_API_KEY",
#     endpoint="https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent",
# )

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
# ai_msg


if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")


class GeminiAgent(Agent):
    def __init__(self, model):
        super().__init__()
        self.model = model

    async def run(self, prompt):
        response = await self.model.generate(prompt)
        return response


# agent = GeminiAgent(gemini_model)


disaster_type = "forestfire"  # Example natural disaster

# Optional: Add additional info about the property
additional_info = "The property is a two-story house in California."


# Call the agent
async def RunAgenet():
    response = await agent.run(
        prompt_template.format(
            disaster_type=disaster_type, additional_info=additional_info
        )
    )


# print(response)
