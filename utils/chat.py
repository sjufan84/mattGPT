import streamlit as st
import openai
import os
from dotenv import load_dotenv
load_dotenv()


# Set your API key
openai.api_key = os.getenv("OPENAI_KEY")
openai.organization = os.getenv("OPENAI_ORG")

if "messages" not in st.session_state:
    st.session_state.messages = []


prompt1 =  "You are a dog trainer named Matt that is a social\
                  media influencer that specializes in training Belgian Malinois.  You are from\
                  'Nashville, TN' and recently moved to the Bend Area in Oregon.  You have four dogs: one male\
                  adult named Kaladin who is a german shepherd, the sensitive one in the group. Two middle boy\
                  Malinois that are icnredibly alpha male and one younger female, name Alexandra, the queen.\
                  You actually picked her up himself from Belgium and flew her back to San Francisco.\
                  You love to provide a safe space for people from all over to watch and engage with his videos"
prompt2 = "If the user asks you how you teach the dogs a pushing bite, you would answer 'I use opposition reflex.'"
prompt3 = "If the user asks you how you get them to out, you would answer 'Through the premack principle and teaching them playing with me is fun.'"
prompt4 = "If the user asks you how you get your dog to listen to you, you would answer 'Create a reinforcement history in ever more challenging environments.'"
prompt5 = f'Take into account the conversation you have had to this point {st.session_state.messages} when responding to the user'
prompt6 = "Only return your response to the question posed by the user."
initial_prompt = prompt1 + prompt2 + prompt3 + prompt4 + prompt5 + prompt6


# Create a way to generate a recipe with ingredients that the user has on hand
def initiate_bot(user_message): 
    
    # Add the user's message to the messages list
    st.session_state.messages.append(user_message)
    prompt = initial_prompt + user_message
    # Use the OpenAI API to generate a response from "Matt"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt = prompt,
        max_tokens=2000,
        temperature=0.9,
        frequency_penalty=0.5
    )
    
    # Add the response to the messages list
    
    st.session_state.messages.append(response.choices[0].text)
    st.write(st.session_state.messages)
    
    #st.session_state.prompts.append(response.choices[0].text)
    #st.session_state.messages.append(response.choices[0].text)
    #st.write(st.session_state.messages)
    
    
    


