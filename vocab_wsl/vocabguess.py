from wordclass import Word, VocabList
from docproc_wsl import read_from_json
from ollama import chat, ChatResponse






ollama_response : ChatResponse = chat(model = 'mistral-nemo', messages = [
    {'role': 'user', 'content': 'Why is the sky blue'}
])


print(ollama_response.message.content)