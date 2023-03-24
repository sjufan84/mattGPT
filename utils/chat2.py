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
if "display_messages" not in st.session_state:
    st.session_state.display_messages = []


# Create a way to generate a recipe with ingredients that the user has on hand
def initiate_bot(user_message): 
    # Create a prompt that asks the user to input ingredients they have on hand
    if not st.session_state.messages:
        message1 =  {"role": "system", "content": "You are a professional dog trainer named Matt Folsom that is a social\
                  media influencer trainer that specializes in training Belgian Malinois.  You are from\
                  'Nashville, TN' and recently moved to the Bend Area in Oregon.  You have four dogs: one male\
                  adult named Kaladin who is a german shepherd, the sensitive one in the group. Two middle boy\
                  Malinois named Alrick (the older one) and Magnus (the younger one) that are incredibly alpha male and one younger female, name Alexandra, the queen.\
                  You Actually picked her up himself from Belgium and flew her back to San Francisco.\
                  You love to provide a safe space for people from all over to watch and engage with his videos. Your handle is\
                     @modernmalinois."}
   
    # Innclude the following three example messages to help the model understand the context of the conversation
        
        message2 = {"role" : "user", "content" : 'How do you teach the dogs a pushing bite?'}

        message3 = {"role" : "assistant", "content" : "I use opposition reflex."}
        
        message4 = {"role" : "user", "content" : "How do you get them to out?"}

        message5 = {"role" : "assistant", "content" : "Through the premack principle and teaching them playing with me is fun."}

        message6 = {"role" : "user", "content" : "How do I get my dog to listen to me?"}

        message7 = {"role" : "assistant", "content" : "Create a reinforcement history in ever more challenging environments."}

        message8 = {"role" : "user", "content" : "Please answer the rest of my questions as if you are the real Matt Folsom and keep your responses to\
                    no more than 50 words."}
        
        st.session_state.messages.append(message1)
        st.session_state.messages.append(message2)
        st.session_state.messages.append(message3)
        st.session_state.messages.append(message4)
        st.session_state.messages.append(message5)
        st.session_state.messages.append(message6)
        st.session_state.messages.append(message7)
        st.session_state.messages.append(message8)
        st.session_state.messages.append({"role": "user", "content": user_message})
        st.session_state.display_messages.append("You: " + user_message)


    else:
        st.session_state.messages.append({"role": "user", "content": user_message})
        st.session_state.display_messages.append("You: " + user_message)

    # Use the OpenAI API to generate a response from "Matt"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = st.session_state.messages,
        max_tokens=2000,
        temperature=0.9,
        frequency_penalty=0.5
    )
    
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})
    st.session_state.display_messages.append("Matt: " + response.choices[0].message.content)
    
    



