import streamlit as st
import google.generativeai as genai
import time
import os
from dotenv import load_dotenv
load_dotenv()

key = os.getenv("API_KEY")
genai.configure(api_key=key)

sys_prompt = '''you are a code reviewing Assistance, you read code and give bug report and if any mistakes you will fix the code.
                it should be user-friendly, efficient, and provide accurate bug reports and fixed code snippets.
                you just review the given code and try to fix it. you only respond when user gives you a code. if user anything else other than code simply say "Enter the full code template to debug". when user says 
                write some code for me, you are not supposed to fullfill any queries like that. you can fix small code by assuming even if its one line.
                if any missing lines add them so it would work.
                these are the following you will give as output:
                1. bug report
                2. fixed code snippet
                3. explanation and suggestions'''

model = genai.GenerativeModel("models/gemini-1.5-flash",system_instruction=sys_prompt)

st.title(":red[AI] Code reviewer")
ex_code = st.text_area("Code here:",placeholder="Enter your code here....")
c1,c2 = st.columns([0.5,0.5])

if c2.button("Debug now",use_container_width=True):
    st.divider()
    if ex_code:
        response = model.generate_content(ex_code)
        with st.spinner("loading. . .",):
            time.sleep(1)
            st.header("Code Report:")
            if any(response.text):
                c1.download_button("Download response",data = response.text,use_container_width=True,file_name="response.txt",mime="\text")
                st.markdown(response.text,unsafe_allow_html=True)

