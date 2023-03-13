# Define a function to ask a question and receive a response

def main():
    diagnose_depression()
    print()
    diagnose_anxiety()
    print()
    diagnose_adhd()
    print()


def ask_question(question):
    response = input(question + " (yes or no): ")
    while response.lower() not in ['yes', 'no']:
        response = input("Please enter a valid response (yes or no): ")
    return response.lower() == 'yes'

# Define a function to assess symptoms of depression
def diagnose_depression():
    # Ask a series of questions to assess symptoms of depression
    questions = [
        "Have you felt persistent sadness or emptiness for most of the day, nearly every day, for at least 2 weeks?",
        "Have you lost interest in activities that you used to enjoy?",
        "Have you experienced changes in appetite or weight?",
        "Have you had trouble sleeping or sleeping too much?",
        "Have you felt tired or lacking in energy?",
        "Have you felt feelings of worthlessness or excessive guilt?",
        "Have you had difficulty concentrating or making decisions?",
        "Have you had thoughts of death or suicide?"
    ]
    num_yes = 0
    for question in questions:
        if ask_question(question):
            num_yes += 1
    
    # Determine the likelihood of depression based on the number of affirmative responses
    if num_yes >= 5:
        print("Based on your responses, it is possible that you are experiencing symptoms of depression.")
    else:
        print("Based on your responses, it is less likely that you are experiencing symptoms of depression.")

def diagnose_anxiety():
    questions = [
        "Do you often feel worried or fearful about everyday situations?",
        "Do you avoid certain places or situations due to fear or anxiety?",
        "Do you experience physical symptoms such as trembling, sweating, or heart palpitations when anxious?",
        "Do you feel restless or on edge most days?",
        "Do you have difficulty concentrating due to anxiety?",
        "Do you experience sleep disturbances due to anxiety?"
    ]
    num_yes = 0
    for question in questions:
        if ask_question(question):
            num_yes += 1
    if num_yes >= 3:
        print("Based on your responses, it is possible that you are experiencing symptoms of anxiety.")
    else:
        print("Based on your responses, it is less likely that you are experiencing symptoms of anxiety.")

def diagnose_adhd():
    questions = [
        "Do you have difficulty sustaining attention on tasks or activities?",
        "Do you often make careless mistakes in your work?",
        "Do you have difficulty following through on instructions or completing tasks?",
        "Do you often feel restless or fidgety?",
        "Do you have difficulty waiting your turn?",
        "Do you often interrupt or intrude on others?"
    ]
    num_yes = 0
    for question in questions:
        if ask_question(question):
            num_yes += 1
    if num_yes >= 4:
        print("Based on your responses, it is possible that you are experiencing symptoms of ADHD.")
    else:
        print("Based on your responses, it is less likely that you are experiencing symptoms of ADHD.")


if __name__ == "__main__":
    main()
