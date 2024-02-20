import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
st.set_page_config(page_title="Smart Application Tracking System 📝", page_icon=":bar_chart:", layout="wide")

def get_gemini_repsonse(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text


input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
Provide suggestions or recommendations for skills that might improve the applicant's match percentage based on the job description. This can help applicants tailor their resumes more effectively.
Give personalized feedback to applicants, highlighting specific areas for improvement in their resumes. This could include suggestions for rephrasing certain sections or emphasizing particular experiences.
also provide personalized job recommendations based on the user's skills, experience, and preferences. This can enhance the user experience by helping them discover relevant job opportunities.
Provide insights into the skills users have versus the skills typically required for their target roles. Suggest relevant training or learning opportunities to bridge any gaps.

I want the response having the structure:
{{
"JD Match:",
"Missing Keywords":
"Profile Summary:",
"Skills:",
"Feedback:",
"Skills Gap Analysis:":,
"Customized Job Recommendations:"
}}"""


st.title("Smart Application Tracking System 📝")
st.text("Improve Your Resume and get a high paying job.")
jd=st.text_area("Paste your job description here")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please upload the pdf file")

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        with st.spinner("Analysing your resume, Please wait ⌛..."):
            text=input_pdf_text(uploaded_file)
            response=get_gemini_repsonse(input_prompt)
            st.subheader(response)