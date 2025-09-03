import os
from dotenv import load_dotenv
from google import genai
import sys



def main():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)


    if len(sys.argv) < 2:
        print("Please provide a prompt")
        sys.exit(1)

    prompt = sys.argv[1]

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=
        prompt,
    )

    print(response.text)
    if response is None or response.usage_metadata is None: 
        raise ValueError("No response from model")

    print("prompt tokens: ", response.usage_metadata.prompt_token_count)
    print("Response tokens: ", response.usage_metadata.candidates_token_count)


if __name__ == "__main__":
    main()