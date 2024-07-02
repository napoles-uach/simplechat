import streamlit as st
import openai

# OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["simple"]

def openq(prompt_script):
    completion = openai.ChatCompletion.create(
        model="gpt-4",  # Usa el modelo correcto según tu suscripción y disponibilidad
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Evaluate the following answers to determine the English proficiency level (Beginner, Intermediate, Advanced):\n{prompt_script}\nProvide the overall proficiency level:"}
        ],
        max_tokens=1000
    )
    return completion.choices[0].message["content"]

# Ejemplo de uso en Streamlit
st.title("English Proficiency Evaluation")
prompt_script = st.text_area("Enter the answers to evaluate:")
if st.button("Evaluate"):
    if prompt_script:
        result = openq(prompt_script)
        st.write("Proficiency Level:", result)
    else:
        st.write("Please enter the answers to evaluate.")

