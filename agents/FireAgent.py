from uagents import Agent, Context, Model
from chatbot import LLM  

class Message(Model):
    message: str

# Manager agent address (as a string, not a list)
manager_agent = 'agent1qfn5swgk6w03f0junfx3r6239ulk0rz7pl08cya7cx7tzf794cl8urqsmdk'

FireAgent = Agent(
    name="WildFireRiskAgent",
    port=8001,
    seed="Fire agent",
    endpoint=["http://127.0.0.1:8001/submit"],
)

print("Fire agent address:", FireAgent.address)

# No need for global variables; use context storage instead

@FireAgent.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    # Initialize context storage for 'history' and 'task' if not already set
    if 'history' not in ctx.storage:
        ctx.storage['history'] = []
    if 'task' not in ctx.storage:
        ctx.storage['task'] = ''

    # If this is the first message, set the task
    if len(ctx.storage['history']) == 0:
        ctx.storage['task'] = msg.message

    ctx.storage['history'].append(msg.message)

    query = f'''
You are {FireAgent.name}. 

The following is your task: 

{ctx.storage['task']}

You may query the manager if you need additional information to answer this task. Otherwise, provide your answer.

For example, if you are trying to find if there is a wildfire in a certain location, you might start off by querying the manager for the wildfire risk in that region.

If you would like to query the manager, start your message with "Query: ...".

Otherwise, start your message with "Answer: ...".
'''

    # Call the LLM to generate a response
    response = LLM(query)

    # Ensure the response is in the expected format
    if ':' in response:
        prefix, content = response.split(':', 1)
        prefix = prefix.strip()
        content = content.strip()

        if prefix == 'Query':
            # Send the query to the manager agent
            await ctx.send(manager_agent, Message(message=content))
        elif prefix == 'Answer':
            # Send the answer to the manager agent and stop the agent
            await ctx.send(manager_agent, Message(message=content))
            await FireAgent.stop()  # Stop the agent after completing the task
        else:
            # Handle unexpected prefixes
            ctx.logger.warning("Unexpected response format from LLM.")
    else:
        ctx.logger.warning("Invalid response format from LLM.")

if __name__ == "__main__":
    FireAgent.run()
