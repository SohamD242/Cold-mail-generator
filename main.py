import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    st.set_page_config(
        layout="wide", 
        page_title="Cold Email Generator", 
        page_icon="📧"
    )
    with st.sidebar:
        st.title("Cold Mail Generator 📧")
        st.markdown(
            """
            This app generates tailored cold emails for job applications from scraped career page data.
            Just enter a URL of a career page, and the app will generate an email tailored to the job roles.

            **How to Use**:
            - Input the URL of the career page in the input box below.
            - Click on 'Generate Email'.
            - The email will be generated and displayed for you to copy or send!
            """
        )

    st.title("📧 Cold Mail Generator")
    st.subheader("Enter the URL of a career page and get a tailored cold email")

    url_input = st.text_input(
        "Career Page URL:", 
        value="", 
        placeholder="https://example.com/careers"
    )

    # Submit button to generate email
    submit_button = st.button("Generate Email", use_container_width=True)

    if submit_button:
        if not url_input:
            st.error("Please enter a valid URL to generate the cold email.")
        else:
            with st.spinner("Processing... Please wait."):
                try:
                    
                    loader = WebBaseLoader([url_input])
                    data = clean_text(loader.load().pop().page_content)
                    portfolio.load_portfolio()
                    jobs = llm.extract_jobs(data)

                    if jobs:
                        job = jobs[0]
                        skills = job.get('skills', [])
                        links = portfolio.query_links(skills)
                        email = llm.write_mail(job, links)

                        st.subheader("Generated Cold Email:")
                        st.markdown("### 📧 Your Cold Email:")
                        st.code(email, language='markdown')
                    else:
                        st.warning("No job listings found in the URL provided.")
                except Exception as e:
                    st.error(f"An error occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    create_streamlit_app(chain, portfolio, clean_text)
