import streamlit as st
import requests
import openai
from openai import OpenAI

# OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["simple"]

def fetch_github_file(repo, path, branch='main'):
    url = f"https://raw.githubusercontent.com/{repo}/{branch}/{path}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

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

# Interfaz de Streamlit
st.title("English Proficiency Evaluation from GitHub File")

repo = st.text_input("GitHub Repository (e.g., 'username/repo'):")
file_path = st.text_input("File Path (e.g., 'path/to/file.py'):")
branch = st.text_input("Branch (default is 'main'):", "main")

if st.button("Fetch and Evaluate"):
    if repo and file_path:
        file_content = fetch_github_file(repo, file_path, branch)
        if file_content:
            st.code(file_content, language='python')
            result = openq(file_content)
            st.write("Proficiency Level:", result)
        else:
            st.write("Failed to fetch the file from GitHub. Please check the repository and file path.")
    else:
        st.write("Please enter the GitHub repository and file path.")
