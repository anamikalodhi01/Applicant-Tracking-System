import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv


load_dotenv()  # load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(input_text):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_text)
    return response.text


def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += str(page.extract_text())
    return text


# Updated Prompt Template
input_prompt = """
You are a skilled ATS (Applicant Tracking System) with deep knowledge in tech fields including software engineering, data science, data analysis, and big data engineering. Evaluate the resume based on the provided job description. Given the competitive job market, provide the following:
1. CV Score: A percentage representing how well the resume matches the job description.
2. Things that can be improved in CV: A list of improvements that can be made to the resume.
3. Skills Improvement Suggestions: Suggestions for skills that should be added or improved in the resume.
4. Missing Keywords: A list of important keywords that are missing in the resume.
5. Profile Summary: A brief summary of the candidate’s profile.

resume: {text}
description: {jd}

Format the response as follows:
CV Score: <percentage>
Things that can be improved in CV:
- <improvement1>
- <improvement2>
Skills Improvement Suggestions:
- <suggestion1>
- <suggestion2>
Missing Keywords:
- <keyword1>
- <keyword2>
Profile Summary:
<summary>
"""


# Streamlit app
st.title("💻 Smart Applicant Tracking System 📈 ")
st.markdown("---")
jd = st.text_area("Enter the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")
st.markdown("---")
submit = st.button("Analyze Resume")


if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt.format(text=text, jd=jd))
        
        # Process the plain text response
        lines = response.split('\n')
        cv_score = "Not available"
        improvements = []
        suggestions = []
        missing_keywords = []
        profile_summary = "Not available"
        
        current_section = None
        
        for line in lines:
            if line.startswith("CV Score:"):
                cv_score = line.replace("CV Score:", "").strip()
            elif line.startswith("Things that can be improved in CV:"):
                current_section = "improvements"
            elif line.startswith("Skills Improvement Suggestions:"):
                current_section = "suggestions"
            elif line.startswith("Missing Keywords:"):
                current_section = "missing_keywords"
            elif line.startswith("Profile Summary:"):
                current_section = "profile_summary"
            elif current_section == "improvements" and line.startswith('-'):
                improvements.append(line.strip('- ').strip())
            elif current_section == "suggestions" and line.startswith('-'):
                suggestions.append(line.strip('- ').strip())
            elif current_section == "missing_keywords" and line.startswith('-'):
                missing_keywords.append(line.strip('- ').strip())
            elif current_section == "profile_summary":
                profile_summary = line.strip()
        
        
        # Display results
        st.subheader("CV Score")
        st.write(cv_score)
        
        
        st.subheader("Profile Summary")
        st.write(profile_summary)
        
        
        st.subheader("Missing Keywords")
        if missing_keywords:
            for item in missing_keywords:
                st.write(f"- {item}")
        else:
            st.write("No missing keywords identified.")
        
        
        st.subheader("Things that can be improved in CV")
        if improvements:
            for item in improvements:
                st.write(f"- {item}")
        else:
            st.write("No suggestions available.")
        
        
        st.subheader("Skills Improvement Suggestions")
        if suggestions:
            for item in suggestions:
                st.write(f"- {item}")
        else:
            st.write("No suggestions available.")
        
       