import streamlit as st
import pandas as pd
import openai

# Initialize OpenAI client
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

st.title("Chatbot Table Interface")

# Initialize or load DataFrame
if "chat_df" not in st.session_state:
    st.session_state.chat_df = pd.DataFrame({
        "Question": ["", "", ""],
        "Answer": ["", "", ""]
    })

# Editable table for questions
edited_df = st.data_editor(
    st.session_state.chat_df,
    column_config={
        "Question": "Your Prompt",
        "Answer": "Chatbot Response"
    },
    use_container_width=True,
    num_rows="fixed",
    disabled=["Answer"]  # Only allow editing "Question"
)

# Update session state
st.session_state.chat_df["Question"] = edited_df["Question"]

if st.button("Get Answers"):
    for i, row in st.session_state.chat_df.iterrows():
        prompt = row["Question"]
        if prompt.strip():
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            st.session_state.chat_df.at[i, "Answer"] = response.choices[0].message.content

    # Re-render table with new answers
    st.experimental_rerun()