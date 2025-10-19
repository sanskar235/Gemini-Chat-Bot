import google.generativeai as genai

#API Connection
genai.configure(api_key="AIzaSyAubv_vCnUG7XBDWAYeGiohsfIw1rQ86Fs")
model = genai.GenerativeModel("gemini-2.5-flash")

#Persona Setup
print("Let's create your chatbot's personality!\n")
print("We are creating a bot specially designed for you. Everyone is unique, so your bot will be too.\n")

persona = {}
persona["name"] = input("Enter chatbot name: ").strip() or "Nova"
persona["tone"] = input("Enter chatbot tone (e.g., friendly, to-the-point, sarcastic, roaster mode): ").strip()
persona["backstory"] = input("Enter about yourself: ").strip()
persona["goal"] = input("Enter chatbot goal (main area for the bot to focus on): ").strip()

print(f"\n✅ Chatbot '{persona['name']}' created successfully!\n")

#Conversation History
conversation_history = []

def GenaiChat(user_input):
    """Generate chatbot reply using Gemini API with persona and memory."""
    context = f"""
You are {persona['name']}, a chatbot with the personality: {persona['tone']}.
Backstory: {persona['backstory']}
Goal: {persona['goal']}

Conversation so far:
{''.join(conversation_history)}

User: {user_input}
{persona['name']}: 
"""
    response = model.generate_content(context)
    reply = response.text.strip()

    # Save messages for context
    conversation_history.append(f"User: {user_input}\n")
    conversation_history.append(f"{persona['name']}: {reply}\n")

    return reply

#Chat Loop
print(f"{persona['name']}: Hey there! Type 'exit' anytime to end the chat.\n")
while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ["exit", "quit"]:
        print(f"{persona['name']}: Fine, leaving already. Goodbye.")
        break
    print(f"{persona['name']}: {GenaiChat(user_input)}\n")
