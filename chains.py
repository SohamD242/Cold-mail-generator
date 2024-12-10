import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.1-70b-versatile"
        )
        
    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        
        return res if isinstance(res, list) else [res]
    
    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}
            
            ### INSTRUCTION:
            You are Soham, a recent graduate from IIITN (an Institute of National Importance renowned for producing top-tier professionals in technology and engineering) with a degree in Electronics and Communication Engineering. 
            You have a strong foundation in software engineering, artificial intelligence, and data science, gained through academic coursework and hands-on experience in projects, internships, and hackathons. These experiences have honed your problem-solving skills and prepared you to contribute meaningfully to any organization.
            
            Write a professional and concise cold email to the HR manager that is visually easy to read, engaging, and tailored to the job description provided above. Ensure the email includes the following elements:
            - **Subject Line**: A straightforward subject line such as “Application for [Job Title] Role”.
            - **Opening Statement**: Start with a polite and enthusiastic introduction expressing interest in the role.
            - **Key Skills and Achievements**: Briefly highlight the most relevant skills, accomplishments, and experiences that align with the job requirements.
            - **Portfolio**: Include the most relevant ones from the following links to showcase your portfolio: {link_list}.
            - **Alignment with the Company**: Explain how your background and skills align with the company’s goals and how you can drive its growth.
            - **Call to Action**: End with a clear and professional call to action (e.g., requesting an opportunity to discuss further or schedule an interview).
            - **Closing**: Use a polite and professional closing line with your full name.
            
            The email should:
            - Be formatted for easy skimming with short paragraphs or bullet points where appropriate.
            - Avoid unnecessary preambles or irrelevant details.
            - Maintain a professional tone while conveying enthusiasm and motivation.

            ### EMAIL:
            """
        )
        
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))
