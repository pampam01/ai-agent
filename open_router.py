import os 
import sys 
from dotenv import load_dotenv
from openai import OpenAI


def open_router():
    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY")
    base_url = os.getenv("OPENROUTER_BASE_URL")

    client = OpenAI(api_key=api_key, base_url=base_url)

    if len(sys.argv) < 2:
        print("Please provide a prompt")
        sys.exit(1)
    
    prompt = sys.argv[1]

    response = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3.1:free",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    clean_content = response.choices[0].message.content.replace("**", "")
    print(clean_content)
    print("prompt tokens: ", response.usage.prompt_tokens)
    print("Response tokens: ", response.usage.completion_tokens)


if __name__ == "__main__":
    open_router()