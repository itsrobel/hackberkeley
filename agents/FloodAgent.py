from uagents import Agent, Context, Model
from chatbot import LLM  

class Message(Model):
    message: str

manager_agent_address = 'agent1qfn5swgk6w03f0junfx3r6239ulk0rz7pl08cya7cx7tzf794cl8urqsmdk'

FloodRiskAgent = Agent(
    name="FloodRiskAgent",
    port=8002,
    seed="Flood agent secret phrase",
    endpoint=["http://127.0.0.1:8002/submit"],
)
  
print("Flood agent", FloodRiskAgent.address)

history = []
task = ''

@FloodRiskAgent.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    global task  # Declare that we will modify the global variable 'task'
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
    if not history:
        task = msg.message
        history.append(task)
    else:
        history.append(msg.message)
    
    query = f'''
You are a {FloodRiskAgent.name}. 

The following is your task: 

{task}

You may query the manager if you need additional information to answer this task. Otherwise, provide your answer.

For example, if you are trying to assess flood risk in a certain location, you might start by querying the manager for recent rainfall data or river levels in that region.

If you would like to query the manager, start your message with "Query: ....".

Otherwise, start your message with "Answer: ..."
'''

    res = LLM(query).strip()
    
    if res.startswith('Query:'):
        query_message = res[len('Query:'):].strip()
        await ctx.send(manager_agent_address, Message(message=query_message))
    elif res.startswith('Answer:'):
        answer_message = res[len('Answer:'):].strip()
        # Send the answer back to the manager agent
        await ctx.send(manager_agent_address, Message(message=answer_message))
        await ctx.stop()
    else:
        # Handle unexpected LLM output
        ctx.logger.error("Unexpected LLM output format.")
        await ctx.send(manager_agent_address, Message(message="Error: Unexpected LLM output format."))
        await ctx.stop()

if __name__ == "__main__":
    FloodRiskAgent.run()
