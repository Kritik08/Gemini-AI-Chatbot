
import os
import sys
import subprocess

# Install the library if it is missing
try:
    from google import genai
except ImportError:
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "--upgrade", "google-genai"
    ])
    from google import genai


# Read API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: Gemini API key not found.")
    print('Run in CMD: setx GEMINI_API_KEY "YOUR_API_KEY"')
    raise SystemExit


# Connect to Gemini
client = genai.Client(api_key=api_key)

# Create chatbot with conversation history
chat = client.chats.create(
    model="gemini-3.8-flash"
)

print("\n================================")
print("       GEMINI AI CHATBOT")
print("================================")
print("Ask me anything!")
print("Type 'exit' to close the chatbot.\n")


while True:

    user_input = input("You: ").strip()

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break

    if not user_input:
        continue

    try:
        print("Chatbot: ", end="", flush=True)

        # Stream the response
        for chunk in chat.send_message_stream(user_input):
            if chunk.text:
                print(chunk.text, end="", flush=True)

        print("\n")

    except Exception as e:
        print("\nGemini API Error:", str(e))
        print("Please check your API key, model access and internet connection.\n")


client.close()
