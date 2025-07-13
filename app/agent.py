import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from app.github_search import search_github_issues
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.2,
        google_api_key=os.getenv("GEMINI_API_KEY"),
        model_kwargs={"stream": False}
    )

def process_error(error, stack, lang):
    prompt = ChatPromptTemplate.from_template("""
You are an AI programming assistant. 
Classify the cause, component, and severity of the following error.
Return response as a JSON with keys: cause, component, severity.

Error Message:
{error}

Stack Trace:
{stack}
""")
    classification_chain = prompt | get_llm()
    classification = classification_chain.invoke({"error": error, "stack": stack})

    fix_prompt = ChatPromptTemplate.from_template("""
You are an expert software engineer.

Explain and fix the following error and stack trace in {lang}. 
Return response as a JSON with keys: explanation, fix, code.

Error Message:
{error}

Stack Trace:
{stack}
""")
    fix_chain = fix_prompt | get_llm()
    fix_suggestion = fix_chain.invoke({"error": error, "stack": stack, "lang": lang})

    github_results = search_github_issues(error)

    return {
        "classification": classification,
        "fix_suggestion": fix_suggestion,
        "github_issues": github_results
    }