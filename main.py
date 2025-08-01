import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)



def main():
    print("Hello from ai-agent!")

user_prompt = sys.argv[1]
print(sys.argv)

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

try:
    sys.argv[1]
except Exception as e:
    print(f'Prompt has error: {e}')
    sys.exit(1)


response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=messages,
)

print(response.text)
if "--verbose" in sys.argv:
    print(f'User prompt: {user_prompt}')
    print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
    print(f'Response tokens: {response.usage_metadata.candidates_token_count}')

if __name__ == "__main__":
    main()
