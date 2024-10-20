import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
genai.configure(api_key=os.environ["API_KEY"])

def LLM(message):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(message)
    print(response.text)
    return response.text

EXS = [
    {
        'agent': 'ManagerAgent (agent1qfn5swgk6w03f0junfx3r6239ulk0rz7pl08cya7cx7tzf794cl8urqsmdk)',
        'message': '''The Los Angeles region is unfortunately prone to a variety of natural disasters. Here's a breakdown of what you should be aware of when buying a home: 
        Routing to the appropriate agents...
        '''
    },
    
    {
        'agent': 'FireRiskAgent (agent1qtnl85m5xtg78cn9svgp0vdl7gtfh6n8mapspwzvtz7rl8gkut92w290hjq)',
        'message': '''**Wildfires:** Los Angeles faces high wildfire risk due to its dry climate, frequent droughts, and strong Santa Ana winds that rapidly spread fires. The city's urban expansion into wildland areas, coupled with highly flammable vegetation like chaparral and steep, fire-prone terrain, increases the danger. Human activities, such as accidental ignitions and power line issues, further contribute to the frequency and intensity of wildfires in the region.
        Querying manager for data...
        '''
    },

    {
        'agent':'FireRiskAgent (agent1qtnl85m5xtg78cn9svgp0vdl7gtfh6n8mapspwzvtz7rl8gkut92w290hjq)', 
        'message':'''According to data, LA has a risk factor of 7.38, with significant temperature flux and wind speed contributing to wildfire in the northern regions. 
        Expected property loss at (34.0522° N, 118.2437° W): $14,300
        '''
    },
    
    {
        'agent':'FloodRiskAgent (agent1qv49ej57qjzkc4ewhjh74v2eputmqa0h3j0hwc5k7ja3swmhe2fa6m7mwj3)', 
        'message':'''**Floods:** Although Los Angeles is often perceived as dry, certain areas are vulnerable to flooding due to heavy winter rains, especially in low-lying regions. The risk is increased by aging infrastructure and inadequate stormwater systems, particularly in floodplain zones. Flash floods and mudslides often accompany intense rainfall events.
        Querying manager for data...
        '''
    },
    
    {
        'agent':'FloodRiskAgent (agent1qv49ej57qjzkc4ewhjh74v2eputmqa0h3j0hwc5k7ja3swmhe2fa6m7mwj3)',
        'message':'''According to data, flood risk in LA is moderate, particularly in the downtown basin. There’s a risk factor of 4.67, with expected property damage at (34.0522° N, 118.2437° W): $8,500
        '''
    },
    
    {
        'EarthquakeAgent (agent1qf972ckn3x7lkt324ycz8ehryg7gcwtqf25dfl423fkjpvj43hp2c8mq8ft)': 
        '''**Earthquakes:** Los Angeles sits along the Pacific Ring of Fire, making it one of the most seismically active regions in the world. Major fault lines, including the San Andreas Fault, pose a constant threat of large, destructive earthquakes. The region has a long history of seismic activity, and modern structures must comply with earthquake-resistant building codes.
        Querying manager for data...
        '''
    },
    
    {
        'EarthquakeAgent (agent1qf972ckn3x7lkt324ycz8ehryg7gcwtqf25dfl423fkjpvj43hp2c8mq8ft)': 
        '''Data shows that LA has a high earthquake risk, with a magnitude 7.8 event expected within the next 30 years. Risk factor: 9.15. Expected property loss at (34.0522° N, 118.2437° W): $35,000
        '''
    },
    
    {
        'ManagerAgent (agent1qfn5swgk6w03f0junfx3r6239ulk0rz7pl08cya7cx7tzf794cl8urqsmdk)': 
        '''Conclusion: According to the data provided by the various agents, Los Angeles presents significant risks across multiple natural disaster categories.
        
        - **Wildfire risk** is high, with a risk factor of 7.38 due to dry climate and wind patterns. Estimated property loss in wildfire-prone areas is $14,300.
        - **Flood risk** is moderate, especially during winter rains in low-lying areas, with a risk factor of 4.67. Estimated property loss due to flooding is $8,500.
        - **Earthquake risk** is extremely high, with a risk factor of 9.15, driven by proximity to major fault lines. Expected property loss in the event of a significant earthquake is $35,000.
        
        Overall, prospective homeowners should carefully evaluate these risks and consider adequate insurance and safety measures before purchasing property in this region.
        '''
    }
]

def example():
    user_msg = input()
    
    for ex in EXS:
        for agent, response in ex.items():
            print(f"{agent}: {response}")
    return EXS


if __name__ == '__main__':
    example()
    
    # LLM("If I'm buying a home in the LA region, what natural disasters should I watch out for?")
