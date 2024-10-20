from uagents import Agent, Context, Model


class Message(Model):
    message: str

managed_agents = {
    'WildFireRiskAgent': 'agent1qtnl85m5xtg78cn9svgp0vdl7gtfh6n8mapspwzvtz7rl8gkut92w290hjq',
    'FloodRiskAgent': 'agent1floodriskaddress',
    'EarthquakeAgent': 'agent1earthquakeaddress',
    'HurricaneAgent': 'agent1hurricaneaddress',
}

start_message = {
    "WildFireRiskAgent": "You are responsible for wildfire prediction",
    "FloodRiskAgent": "You are responsible for flood prediction",
    "EarthquakeAgent": "You are responsible for earthquake prediction",
    "HurricaneAgent": "You are responsible for hurricane prediction",
}

ManagerAgent = Agent(
    name="ManagerAgent",
    port=8000,
    seed="ManagerAgent secret phrase",
    endpoint=["http://127.0.0.1:8000/submit"],
)

print("Manager agent", ManagerAgent.address)

# Assume Query_Data is given
def Query_Data(feature, lon, lat, datetime):
    # Simulate data retrieval
    return f"Data for {feature} at ({lon}, {lat}) on {datetime}"

async def classify_agent(msg):
    response = LLM(f"Determine the appropriate agent for the following task: {msg}. Available agents: WildFireRiskAgent, FloodRiskAgent, EarthquakeAgent, HurricaneAgent.")
    agent_name = response.strip()
    return agent_name

@ManagerAgent.on_message(model=Message)
async def handle_agent_message(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
    if msg.message.lower() == "done":
        ctx.logger.info("Agent has completed its task.")
        # Optionally stop the manager agent or perform cleanup
        # await ManagerAgent.stop()
        return



    llm_response = LLM(f"Extract 'feature', 'lon', 'lat', and 'datetime' from the following request: {msg.message}. Example response: feature: temperature, lon: -122.4194, lat: 37.7749, datetime: 2023-10-20")
    # Example response: "feature: temperature, lon: -122.4194, lat: 37.7749, datetime: 2023-10-20"
    
    # Parse the response
    parameters = {}
    for item in llm_response.split(','):
        key, value = item.strip().split(':')
        parameters[key.strip()] = value.strip()

    feature = parameters.get('feature')
    lon = parameters.get('lon')
    lat = parameters.get('lat')
    datetime_value = parameters.get('datetime')

    data = Query_Data(feature, lon, lat, datetime_value)
    await ctx.send(sender, Message(message=data))

async def main():
    await ManagerAgent.start()

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Exiting...")
            await ManagerAgent.stop()
            break

        agent_name = await classify_agent(user_input)
        if agent_name not in managed_agents:
            print("No suitable agent found for the message.")
            continue

        agent_address = managed_agents[agent_name]
        await ManagerAgent.send(agent_address, Message(message=start_message[agent_name]))
        await ManagerAgent.send(agent_address, Message(message=user_input))

if __name__ == '__main__':
    import asyncio
    from chatbot import LLM
    asyncio.run(main())