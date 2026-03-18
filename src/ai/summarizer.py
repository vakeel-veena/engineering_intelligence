import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_summary(metrics):
    prompt = f"""
You are an engineering analyst.

Metrics:
{metrics}

Generate:
- summary
- highlights
- risks
- leadership note
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content