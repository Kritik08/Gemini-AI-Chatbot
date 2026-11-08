# 🤖 Gemini AI Chatbot

## 📌 Project Overview

Gemini AI Chatbot is a Python-based conversational application powered by Google's Gemini API. It allows users to ask different types of questions and receive AI-generated responses.

The chatbot uses streaming to display responses gradually and maintains conversation history during the session.

## ✨ Features

- **AI-Powered Responses:** Generates answers using Google's Gemini AI.
- **Dynamic Questions:** Users can ask different types of questions.
- **Conversation History:** Remembers previous messages during the session.
- **Streaming Responses:** Displays answers gradually as they are generated.
- **Exit Option:** Allows users to close the chatbot by typing `exit`, `quit` or `bye`.
- **Error Handling:** Displays an error message if an API request fails.
- **Simple Interface:** Easy-to-use command-line interface.

## ⏳ Response Time

- The chatbot may take a few seconds to generate responses.
- Response time depends on internet connectivity, API processing time and server load.
- Streaming is enabled, so generated text appears gradually rather than waiting for the complete response.

## 🛠️ Technologies Used

- Python
- Google Gemini API
- Google GenAI Python SDK

## 📋 Requirements

- Python 3 installed on your computer.
- Active internet connection.
- Google Gemini API key.

## ⚙️ Installation

Install the required Google GenAI library using CMD:

```bash
pip install google-genai
```

## 🔑 API Key Setup

The chatbot uses an environment variable to access the Gemini API key.

For Windows CMD, run:

```cmd
setx GEMINI_API_KEY "YOUR_API_KEY"
```

Replace `YOUR_API_KEY` with your actual Gemini API key.

**Important:** Restart CMD or Python IDLE after setting the environment variable.

Never share your API key or upload it to GitHub.

## ▶️ How to Run

1. Download or clone this repository.
2. Open CMD in the project folder.
3. Run the following command:

```bash
python chatbot.py
```

4. Start asking questions.
5. Type `exit` to close the chatbot.

## 💬 Sample Output

```text
================================
       GEMINI AI CHATBOT
================================
Ask me anything!
Type 'exit' to close the chatbot.

You: What is Artificial Intelligence?

Chatbot: Artificial Intelligence is the ability
of computers to perform tasks that normally
require human intelligence.

You: Give me an example.

Chatbot: A virtual assistant that understands
questions and provides answers is an example
of Artificial Intelligence.

You: exit

Chatbot: Goodbye!
```

## 🎯 Learning Objectives

- Understanding Python programming.
- Learning how to integrate an AI API.
- Understanding chatbot conversation history.
- Handling API responses and errors.
- Implementing streaming responses.
- Working with external Python libraries.

## 🚀 Future Improvements

- Develop a graphical user interface.
- Add voice-based interaction.
- Improve chatbot response speed.
- Add more interactive features.
- Improve the overall user experience.

## 👨‍💻 Author

**Kritik Shetty**

TYBSc Information Technology

## 📄 Project Purpose

This project was developed as a practical learning experience to understand Python programming and integration of Generative AI using Google's Gemini API.
