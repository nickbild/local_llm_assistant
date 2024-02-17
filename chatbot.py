###
# Nick Bild
# February 2024
#
# Be sure to start the LLM before running this script, e.g.:
# ./TinyLlama-1.1B-Chat-v1.0.Q5_K_M.llamafile
###

import os
from openai import OpenAI


client = OpenAI(
    base_url="http://127.0.0.1:8080/v1",
    api_key = "sk-no-key-required"
)

###
# Get the request.
###

request = "say the word 'hi'"

###
# Query the LLM.
###

completion = client.chat.completions.create(
    model="LLaMA_CPP",
    messages=[
        {"role": "system", "content": "You are an AI assistant. Your priority is helping users with their requests."},
        {"role": "user", "content": request}
    ]
)

###
# Speak the result.
###

print(completion.choices[0].message)
os.system('espeak "{0}" 2>/dev/null'.format(completion.choices[0].message.content))

