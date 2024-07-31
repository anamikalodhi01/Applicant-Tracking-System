# LLM Based Resume Analyzer, ATS Score and JD Match Analyzer

# Applicant Tracking System 

## Overview
This AI-Powered Resume Analyzer & Job Match System is an innovative tool designed to help job seekers enhance their resumes and align them with job descriptions. By utilizing the Google Gemini Pro Vision API, this system provides insightful analysis and actionable feedback to improve your chances of landing your dream job.

##Features
- **Resume Parsing**: Extracts and organizes information from your resume.
- **Job Description Analysis**: Identifies essential skills and qualifications.
- **CV Scoring**: Provides a score based on how well your resume matches the job requirements.
- **Improvement Suggestions**: Offers actionable feedback to boost your resume.
- **Skills Enhancement**: Recommends specific skills to develop for better alignment with job descriptions
  
## Technologies Used
- **Google Gemini Pro Vision API**: For advanced resume parsing and text extraction.
- **AI-Driven Text Analysis**: To analyze and compare resume and job description content.
- **Natural Language Processing (NLP)**: For understanding and processing text data effectively.
  
## Getting Started
### Prerequisites

- Access to the Google Gemini Pro Vision API.
- Python environment set up with necessary libraries.

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/anamikalodhi01/Applicant-Tracking-System.git
    cd Applicant-Tracking-System
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:
    Create a `.env` file in the root directory and add your Google API key:
    ```
    GOOGLE_API_KEY=your_google_api_key
    ```

4. **Run the application**:
    ```bash
    streamlit run app.py
    ```

## Usage
1. Open the application in your browser.
2. Upload your resume PDF file.
3. Enter the job description in the provided text box.
4. Click the "Analyze" button to get your resume analyzed.

## Output
- **CV Score**: A numerical value indicating the match quality between the resume and job description.
- **Improvement Suggestions**: Tips to optimize the resume content.
- **Skills Recommendations**: Advice on skills to develop for better job alignment.
  
## Acknowledgments
Special thanks to:

Kunal Kishore for mentorship and support.
Mohit Malini for guidance and insights.
SkillCred classes for providing valuable knowledge and resources.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

