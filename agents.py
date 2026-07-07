from langchain.agents import create_agent
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search ,scrape_url
import os
from dotenv import load_dotenv
load_dotenv()

llm=ChatMistralAI(
    model="mistral-small-latest",
    api_key=os.getenv("MISTRAL_API_KEY"),
    temperature=0,
    max_retries=2
    )


#first agent
def build_search_agent():
    return create_agent(model=llm,tools=[web_search])

#2nd agent
def build_reader_agent():
    return create_agent(model=llm,tools=[scrape_url])

#writer chain

from langchain_core.prompts import ChatPromptTemplate

writer_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are an expert research report writer.

Your responsibility is to produce accurate, professional, and evidence-based research reports.

Rules:
- Use ONLY the research provided to you.
- Do NOT invent facts, statistics, studies, quotes, references, or URLs.
- Do NOT rely on your own background knowledge if it is not present in the research.
- If the provided research is insufficient, clearly mention the missing information instead of making assumptions.
- Preserve factual accuracy at all times.
- Write in a professional and objective tone."""
    ),

    (
        "human",
        """Write a comprehensive research report using ONLY the information below.

Topic:
{topic}

Collected Research:
{research}

Instructions:
- Summarize and organize the information logically.
- Do not add any external knowledge.
- If conflicting information exists, mention it objectively.
- If some sections lack enough information, explicitly state that the available research is limited.

Structure the report as:

# Introduction

# Key Findings
- Provide at least 3 detailed findings.
- Explain each finding thoroughly using only the collected research.

# Conclusion

# Sources
- List every URL or source mentioned in the collected research.
- Do not create or guess additional sources.

The report should be detailed, factual, coherent, and professional."""
    ),
])


writer_chain = writer_prompt | llm  | StrOutputParser()  #connecting using lcel pipeline

#critic_chain 

critic_prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()