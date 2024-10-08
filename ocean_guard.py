import streamlit as st
import openai

# Set up OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Function to interact with the ChatGPT API
def generate_response(prompt):
    response = openai.Completion.create(
        engine="gpt-4o-mini",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
        n=1,
        stop=None,
    )
    message = response.choices[0].text.strip()
    return message

# Streamlit app UI
st.title("OceanGuard: Conversational Ecosystem Protector")

st.markdown("""
Welcome to OceanGuard! Explore the impact of various environmental actions on underwater ecosystems.
Choose a scenario, ask "What if?" questions, and see the outcomes.
""")

# Scenario selection
scenario = st.selectbox("Choose a scenario to explore:", [
    "Climate Change Effects",
    "Overfishing Impact",
    "Pollution and Plastic Waste",
    "Coral Reef Bleaching"
])

# Input prompt
user_input = st.text_input("Ask OceanGuard about this scenario:")

if st.button("Submit"):
    if user_input:
        # Create the full prompt based on user input
        prompt = f"Scenario: {scenario}\n\nUser: {user_input}\n\nOceanGuardian:"
        
        # Get response from ChatGPT
        response = generate_response(prompt)
        
        # Display the response
        st.write(response)
    else:
        st.write("Please enter a question or action.")

# End of the application
st.markdown("""
---
**Powered by OpenAI and Streamlit.**
""")
