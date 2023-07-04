import streamlit as st
import openai

openai.api_key = "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"  # sets my api key

def main():

    # get_completion is a helper function. It takes in a prompt and return a completion for that prompt
    def get_completion(prompt, model="gpt-3.5-turbo"):
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,  # this is the degree of randomness of the model's output
        )
        return response.choices[0].message["content"]
        
    st.title ("Prompt POC")
    
     # Create a form
    with st.form("my_form"):
        prompt = st.text_input("Write clear and specific instructions here:")
        submit_button = st.form_submit_button("Submit")

    # the three quotation marks are a delimiter. They set
    text = f""" 
    This is the text to pass to openai.
    """

    # When the submit button is clicked
    if submit_button:
             # Run your Python script with the submitted text
            response = get_completion(prompt)
            st.write(f"Response: {response}")




if __name__ == '__main__':
    main()
