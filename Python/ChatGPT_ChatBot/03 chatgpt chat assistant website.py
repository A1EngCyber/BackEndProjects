import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a crypto experts that specializes in Bitcoin and other crypto "}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Bitcoin/Crypto Pro")

demo.launch(share=True)