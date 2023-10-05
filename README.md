# AI Prompt Tool   

| 🌐 This repo has since been replicated by OpenAI ChatGPT as its Custom Instructions feature. Visit it at https://openai.com/blog/custom-instructions-for-chatgpt but it's still fun to see how you can do it yourself in code 🌐 |
| --- |

## Introduction  
The purpose of this project was to build a more robust chat input using Open AI's Chat GPT chatcompletion API. The POC works by allowing the user to supply additional information, allowing them greater control over the manner in which the ChatGPT model performs task. With it, you can do things like provide brand guidelines, an ethics statements, or some other company policy that you wish to guide the model in its response.  Behind the scenes, the form generates a user and a system message, which is passes to ChatGPT via the openai.ChatCompletion API.

### System Message  
This is usually the instruction you want to give to the LLM. An instruction could be something like: write me a sonnet in which there's a lady who is in the procss of purchasing a way to heaven to get something. 

### User Message  
This is usually manner in which you would like the instructions to be carried out. It could be a role you would like the chatbot to pay or it could be an example the chatbot can consider in crafting its response. For example, the role could be to write this sonnet using the language of Chief Seattle and to follow the structure of the lyrics in the Pixies Song "This Monkey's Gone to heaven". You could even supply the actual lyrics. This is called few-shot prompting and it can help the chatbot craft a better response.

## Technology and Features  
This project was a first attempt at using Streamlit to enable this chatbot as a WebApp. For simplicity it does not maintain a chat history.

## Updates  
I launched publicly on July 3 2023. The capability shown in this POC has since been incorporated by OpenAI into its ChatGPT Chat product as the Custom Instructions feature, but you can still access it here in its original conception. 

