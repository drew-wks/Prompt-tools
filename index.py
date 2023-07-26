import openai
import streamlit as st

openai.api_key = "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"  # sets my api key

# at some point I wil ltransition to this as a more secure way of accessing my openai key. It may require a package called os to be imported first.
# from dotenv import load_dotenv, find_dotenv
# _ = load_dotenv(find_dotenv()) # read a local .env file which contains my secret key

# openai.api_key  = os.environ['OPENAI_API_KEY']


def main():

    # get_completion is a helper function. It takes in a prompt and return a completion for that prompt
    def get_completion(prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,  # this is the degree of randomness of the model's output
        )
        return response.choices[0].message["content"]
        
    st.title ("AI Prompt Tool")
    st.write ("We developed this proof of concept for situations where you would like Chat GPT to perform a task upon text supplied by you. By separating the text from the instruction, you can get better results.")
    st.write ("Go ahead, give it a try!")
    
    with st.form("my_form"):
        # Input widgets
        model = st.selectbox("Select a model:", ("gpt-3.5-turbo", "gpt-4.0")) # this works it's just not needed right now
        instruction = st.text_area("Place instructions here:")    
        text = st.text_area("Place optional text here:") 
        submit_button = st.form_submit_button("Submit")

       
    prompt = f"""
        {instruction}```{text}```
        """
    
    # When the submit button is clicked
    if submit_button:
             # Run your Python script with the submitted text
            response = get_completion(prompt)
        
            st.write(f"**Response:** {response}") # this works. I just prefer the st.code model with copy 2 clipboard
            # st.code(response, language="asciidoc", line_numbers=False) #has copy function but no word wrap!

        from trubrics.integrations.streamlit import FeedbackCollector

        collector = FeedbackCollector()
        collector.st_feedback(feedback_type="issue")
            


if __name__ == '__main__':
    main()
