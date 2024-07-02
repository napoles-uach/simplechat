import streamlit as st
from openai import OpenAI

# OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["gpt_key"]

def openq(prompt_script):
    client = OpenAI(api_key=st.secrets["simple"])
    completion = client.chat_completions.create(
        # model = "gpt-3.5-turbo-0125",
        # model="gpt-4-turbo-2024-04-09",
        model="gpt-4o",
        # model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Evaluate the following answers to determine the English proficiency level (Beginner, Intermediate, Advanced):\n{prompt_script}\nProvide the overall proficiency level:"}
        ],
        max_tokens=1000
    )
    return completion.choices[0].message.content

# Ejemplo de uso en Streamlit
st.title("English Proficiency Evaluation")
prompt_script = st.text_area("Enter the answers to evaluate:")
if st.button("Evaluate"):
    if prompt_script:
        result = openq(prompt_script)
        st.write("Proficiency Level:", result)
    else:
        st.write("Please enter the answers to evaluate.")

