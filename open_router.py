import os 
import sys 
from dotenv import load_dotenv
from openai import OpenAI
import re


def cleaned_content(content):    
    bold_start = r"\*\*"
    bold_end = r"\*\*"
    regex = f"{bold_start}(.*?){bold_end}"
    return re.sub(regex, r"\1", content)

def open_router():
    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY")
    base_url = os.getenv("OPENROUTER_BASE_URL")

    client = OpenAI(api_key=api_key, base_url=base_url)

    if len(sys.argv) < 2:
        print("Please provide a prompt")
        sys.exit(1)
    verbose_flag = False
    if len(sys.argv) > 2 and sys.argv[2] == "-v":
        verbose_flag = True
    
    prompt = sys.argv[1]

    messages = [
        {"role": "system", "content": "kamu adalah seorang asisten bantuan yang membantu pengguna dengan membantu pengguna untuk memecahkan masalah."},
        {"role": "user", "content": prompt}
    ]

    response = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3.1:free",
            messages=messages
    )

    clean_content = cleaned_content(response.choices[0].message.content)
    print(clean_content)

    if verbose_flag:
        print("Response: ", clean_content)
        print("prompt tokens: ", response.usage.prompt_tokens)
        print("Response tokens: ", response.usage.completion_tokens)


if __name__ == "__main__":
    open_router()