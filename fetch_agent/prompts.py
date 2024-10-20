from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_messages([
    ChatPromptTemplate.Message(type="System", text="The user wants to assess the true cost of a property considering the natural disaster risk of {disaster_type}. Can you analyze factors like insurance and other fees?"),
    ChatPromptTemplate.Message(type="Human", text="{additional_info}"),  # Optional: User can provide additional details
])
