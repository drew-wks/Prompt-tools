import streamlit as st
import openai

openai.api_key = "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"  # sets my api key

def main():

    # get_completion is a helper function. It takes in a prompt and return a completion for that prompt
    def get_completion(prompt, model="gpt-3.5-turbo"):
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0,  # this is the degree of randomness of the model's output
        )
        return response.choices[0].message["content"]
        
    st.title ("Prompt POC")
    
     # Create a form
    with st.form("my_form"):
        text_input = st.text_input("Enter your prompt here:")
        submit_button = st.form_submit_button("Submit")
    
    # When the submit button is clicked
    if submit_button:
             # Run your Python script with the submitted text
            result = run_python_script(text_input)
            st.write(f"Result: {result}")
    

if __name__ == '__main__':
    main()
