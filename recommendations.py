import ollama

def get_recommendations(prompt):
    response = ollama.generate(model="llama3", prompt=prompt)
    
    # Extract the text from the 'response' key
    response_text = response['response']
    print(response_text)
    # Split the text into lines and filter to capture the recommendations
    lines = response_text.split("\n")
    recommendations = [line for line in lines if line.startswith("1.") or line.startswith("2.") or line.startswith("3.")]
    
    return recommendations
