def construct_prompt(preferences, query):
    preferences_summary = ', '.join(preferences)
    prompt = f"User prefers {preferences_summary}. Current query: {query}. Recommend the top 3 food choices."
    return prompt
