import streamlit as st
import openai

# Your OpenAI API Key
openai.api_key = "YOUR_OPENAI_API_KEY"

st.title("Chatbot Table Interface")

# Initialize session state for table
if "prompts" not in st.session_state:
    st.session_state.prompts = [""] * 3
if "responses" not in st.session_state:
    st.session_state.responses = [""] * 3

# Table layout
st.write("Enter your questions/prompts below:")

for i in range(3):
    cols = st.columns([1, 2])
    with cols[0]:
        st.session_state.prompts[i] = st.text_input(f"Prompt {i+1}", st.session_state.prompts[i], key=f"prompt_{i}")
    with cols[1]:
        if st.session_state.responses[i]:
            st.text_area(f"Answer {i+1}", st.session_state.responses[i], key=f"answer_{i}", height=100)

# Submit button to query chatbot
if st.button("Get Answers"):
    for i, prompt in enumerate(st.session_state.prompts):
        if prompt.strip():
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            st.session_state.responses[i] = response.choices[0].message.content