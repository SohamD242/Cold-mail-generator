# Cold Mail Generator  

An AI-powered tool designed to craft **personalized job application emails** by analyzing career portal job links. Built using **Llama-3.1 (70B Versatile)**, **Chromadb**, **Langchain**, and **Streamlit**, this project helps job seekers streamline their communication with HR managers, ensuring tailored and professional outreach.

---

## Features  

- **Job-Link Analysis**: Extracts key job details from career portal links for personalized email creation.  
- **AI-Powered Content Generation**: Utilizes Llama-3.1 to generate emails specific to the job description and requirements.  
- **Vector Database Integration**: Employs Chromadb to store and retrieve job-specific information for enhanced personalization.  
- **User-Friendly Interface**: Built with Streamlit, making it easy for anyone to generate customized emails.  

---

## Example  

### Input  
Career portal link: `https://example.com/jobs/software-engineer-role`  

### Output  

**Subject**: Application for Software Engineer Role  

**Email**:  
Dear [HR Name],  

I hope this email finds you well. I came across the Software Engineer position listed on your career portal and was thrilled to see how closely it aligns with my skills and career aspirations.  

With a strong background in [specific skills matching the job], I am confident in my ability to contribute effectively to [Company Name]. My recent experience includes [brief relevant experience or achievement].  

I would love the opportunity to discuss how my skills and experience align with the goals of your team. Please let me know a convenient time for a conversation.  

Looking forward to hearing from you!  

Warm regards,  
[Your Name]  

---

## How It Works  

1. **Input Job Link**: Paste the career portal link into the application.  
2. **AI Processing**: The tool retrieves job details and analyzes the description using Llama-3.1 via Groq API and Langchain.  
3. **Personalization**: Chromadb ensures the email aligns perfectly with the job description.  
4. **Email Output**: A customized job application email is generated for HR outreach.  

---

## Installation  

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/SohamD242/Cold-Mail-Generator.git

## Installation  

1. Clone the repository:  
   ```bash  
   https://github.com/SohamD242/Cold-mail-generator.git

## Setup Instructions  

2. **Navigate to the project directory:**  
   ```bash
   cd Cold-mail-generator/app

3. **Run the application:**
   ```bash
     python main.py
![Screenshot](./Screenshot%202024-12-10%20163410.png)


