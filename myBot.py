import openai
import gradio

openai.api_key = "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";

messages = [{"role": "system", "content": "You are a Programmer"}]

def CustomChatPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = messages["choices"][0]["messages"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return  ChatGPT_reply
demo = gradio.Interface(fn=CustomChatPT, inputs="text", outputs="text", title="DannyApi")

demo.launch(share=True)
