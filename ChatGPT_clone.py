import os
import openai
import gradio as gr

#if you have OpenAI API key as an environment variable, use the below statement
#openai.api_key = os.getenv("OPENAI_API_KEY")

#if you have OpenAI API key as a string, then use this
openai.api_key = "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"

start = "\nAI:"
restart = "\nHuman: "
prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "

def create_prompt(prompt):

    result = openai.Completion.create(model="text-davinci-003",prompt=prompt,temperature=0.9,max_tokens=150,top_p=1,frequency_penalty=0,presence_penalty=0.6,stop=[" Human:", " AI:"])
    return result.choices[0].text

def chatgGPT_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = create_prompt(inp)
    history.append((input, output))
    return history, history

block = gr.Blocks()

with block:
    gr.Markdown("""<h1><center>Experience ChatGPT with OpenAI API & Gradio</center></h1>
    """)
    chatbot = gr.Chatbot()
    text_message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    send = gr.Button("SEND")
    send.click(chatgGPT_clone, inputs=[text_message, state], outputs=[chatbot, state])

block.launch(debug = True)