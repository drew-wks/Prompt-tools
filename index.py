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
     # Create a prompt form 
    
    with st.form("my_form"):
        # Input widgets
        instruction = st.text_input("Place instructions here:")    
        text = st.text_area("Place optional text here:") 
        submit_button = st.form_submit_button("Submit")

       
    prompt = f"""
        {instruction}```{text}```
        """
    
    # When the submit button is clicked
    if submit_button:
             # Run your Python script with the submitted text
            response = get_completion(prompt)

            '''
            ChatGPT response
            '''
        
            st.text_area(label ="",value=response, height =100)
           # st.write(f"GPT 3.5 turbo Response: {response}")
            


if __name__ == '__main__':
    main()
