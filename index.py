import openai
import streamlit as st
from trubrics.integrations.streamlit import FeedbackCollector

openai.api_key = st.secrets["OPENAI_API_KEY"]  # sets my api key by pulling it from the streamlit secrets file

st.session_state['previous_response'] = 0


def main():
    # get_completion is a helper function. It takes in a prompt and return a completion for that prompt
    def get_completion(prompt):
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,  # this is the degree of randomness of the model's output
        )
        return response.choices[0].message["content"]

    
    st.title ("AI Prompt Tool")
    st.write ("We developed this proof of concept for situations where you would like Chat GPT to perform a task upon text supplied by you. By separating the text from the instruction, you can get better results.")
    st.write ("Go ahead, give it a try!")
    
    with st.form("round1"):
        # Input widgets
        model = st.selectbox("Select a model:", ("gpt-3.5-turbo", "text-davinci-003")) # this works it's just not needed right now
        instruction = st.text_area("Place instructions here:")    
        text = st.text_area("Place optional text here:") 
        submit_button1 = st.form_submit_button("Submit")
    
    prompt = f"""
        {instruction}```{text}```
        """
     
    # When the submit button is clicked
    if submit_button1:
             # Run your Python script with the submitted text
            response = get_completion(prompt)
            st.session_state['previous_response'] = f"{response}"
            st.write(f"**Response:** {response}") # this works. I just prefer the st.code model with copy 2 clipboard
            # st.code(response, language="asciidoc", line_numbers=False) #has copy function but no word wrap! 

            st.write ("Session State value is",  st.session_state['previous_response'])

            collector = FeedbackCollector(
                component_name="default",
                email=st.secrets["TRUBRICS_EMAIL"], # Retreives my Trubrics credentials from secrets file
                password=st.secrets["TRUBRICS_PASSWORD"], # https://blog.streamlit.io/secrets-in-sharing-apps/
            )

            st.markdown("""---""")
            st.write ("How well did the model do?")
            st.write (f"{model}")

            collector.st_feedback(feedback_type="thumbs",
                model=model,
                open_feedback_label="[Optional] How did the model do?",
            )
#round two       

    with st.form("round2"):
        # Input widgets
        instruction = st.text_area("Place instructions here:")    
        submit_button2 = st.form_submit_button("Submit")

                   
    prompt = f"""
        {instruction}```{st.session_state['previous_response']}```
        """
    
    # When the submit button is clicked
    if submit_button2:
             # Run your Python script with the submitted text

            
            response = get_completion(prompt)
            st.write(f"**Response:** {response}") 

            st.write ("Session State value is",  st.session_state['previous_response'])
            
if __name__ == '__main__':
    main()
