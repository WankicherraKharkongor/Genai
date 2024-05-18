import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from langchain import OpenAI

#pip install openai
# Load environment variables
load_dotenv('project1/.env')
key = os.environ.get('api_key')

# Initialize OpenAI language model
llm = OpenAI(temperature=0.7, openai_api_key=key)

# Define function to generate player names participating in the football club
def generate_player_names(team_name):
    # Prompt template for generating player names
    player_names_prompt_template = PromptTemplate(
        
        input_variables=['team_name'],
        template="List the names of players participating in the {team_name} football club."
    )

    # Define LLM chain for player names
    player_names_chain = LLMChain(llm=llm, prompt=player_names_prompt_template, output_key="player_names")

    # Generate response using the chain
    response = player_names_chain({'team_name': team_name})

    return response

if __name__ == "__main__":
    # Test the function with a football club team name
    print(generate_player_names("Manchester City"))


