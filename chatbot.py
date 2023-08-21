import csv
import random

qa_pairs = {}

# Read data from the CSV file
with open('qa_pairs.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        question = row[0]
        answers = row[1:]
        qa_pairs[question] = answers

def chatbot_response(user_input):
    if user_input in qa_pairs:
        responses = qa_pairs[user_input]
        return random.choice(responses)
    else:
        return "Sorry! I didn't get your question!"

while True:
    user_input = input("You: ")
    if user_input == "Exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
