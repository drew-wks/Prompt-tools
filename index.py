import streamlit as st
import openai

openai.api_key = "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"  # sets my api key

st.title ("Python WebApp")
def main():
    st.title("This is where the prompt will go")

    # Create a form
    with st.form("my_form"):
        text_input = st.text_input("Enter Text:")
        submit_button = st.form_submit_button("Submit")

        # When the submit button is clicked
        if submit_button:
            # Run your Python script with the submitted text
            result = run_python_script(text_input)
            st.write(f"Result: {result}")

def run_python_script(text):
    # Your Python script logic here
    # Perform any desired operations with the submitted text
    return text()

if __name__ == '__main__':
    main()
