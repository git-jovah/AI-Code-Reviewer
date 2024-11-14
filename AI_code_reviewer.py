import streamlit as st
import google.generativeai as genai
import time

genai.configure(api_key="AIzaSyAPPjQz0sJ800CX6hFdllcRxNUaldL4HIQ")

sys_prompt = '''you are a code review Assistance, you read code and give bug report and if any mistakes you will fix the code.
                it should be user-friendly, efficient, and provide accurate bug reports and fixed code snippets.
                you just review the given code and try to fix it. you only respond when user gives you a code. if user anything else other than code simply say sorry. when user says 
                write some code for me, you are not supposed to fullfill any queries like that. you can fix small code by assuming sometimes.
                if any missing lines add them so it would work.
                these are the following you will give as output:
                1. bug report
                2. fixed code snippet
                3. explanation and suggestions'''

model = genai.GenerativeModel("models/gemini-1.5-flash",system_instruction=sys_prompt)

st.header(":red[AI] Code reviewer",divider=True)
ex_code = st.text_area("Code here:",placeholder="Enter your code here....")

if st.button("Generate"):
    st.divider()
    if ex_code:
        response = model.generate_content(ex_code)
        with st.spinner("loading. . .",):
            time.sleep(1)
            st.header("Code Report:")
            st.markdown(response.text,unsafe_allow_html=True)

