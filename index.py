import streamlit as st
import openai

openai.api_key = "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"  # sets my api key

st.title ("Prompt POC")
def main():

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
