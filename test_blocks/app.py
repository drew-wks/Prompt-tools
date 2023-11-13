# run as streamlit run /Users/drew_wilkins/Drews_Files/Drew/Python/pythonProject/WebApp/app.py
import streamlit as st

from barfi import st_barfi, barfi_schemas

from test_blocks import process_blocks

st.title ("LLM Logic Builder")
barfi_schema_name = st.selectbox(
    'Select a saved schema to load:', barfi_schemas())


compute_engine = st.checkbox('Activate barfi compute engine', value=True)


barfi_result = st_barfi(
    base_blocks=process_blocks,
    compute_engine=compute_engine,
    load_schema=barfi_schema_name)

if barfi_result:
    st.write(barfi_result['Result Operator-1']['block'].get_interface(name='input'))