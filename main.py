import streamlit as st
from user_auth import create_user, login_user, load_user_preferences
from recommendations import get_recommendations
from preferences import update_preferences
from database import create_tables

# Define the construct_prompt function directly in main.py
def construct_prompt(preferences, query):
    preferences_summary = ', '.join(preferences)
    prompt = (
        f"Considering the user's preferences ({preferences_summary}) and the current query: '{query}', "
        "please recommend three specific dishes from well-known restaurants in the area. "
        "Each recommendation should include the restaurant's name and the specific dish."
    )
    return prompt

def main():
    create_tables()
    
    st.title("AI-Powered Food Recommendation App")

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if not st.session_state['logged_in']:
        user_id = st.text_input("User ID")
        password = st.text_input("Password", type="password")

        if st.button("Create Account"):
            create_user(user_id, password)
            st.success("Account created! Please log in.")
        
        if st.button("Login"):
            if login_user(user_id, password):
                st.session_state['logged_in'] = True
                st.session_state['user_id'] = user_id
                st.session_state['user_preferences'] = load_user_preferences(user_id)
                st.success("Login successful!")
            else:
                st.error("Login failed. Please check your User ID and Password.")
    else:
        st.write(f"Logged in as {st.session_state['user_id']}")
        st.write("Your Preferences:", st.session_state['user_preferences'])

        current_query = st.text_input("What's your food query today?")

        if st.button("Get Recommendations"):
            prompt = construct_prompt(st.session_state['user_preferences'], current_query)
            recommendations = get_recommendations(prompt)
            st.write("Top 3 Recommendations:", recommendations)

        new_preference = st.text_input("Add new preference based on your choices:")
        if st.button("Update Preferences"):
            updated_preferences = update_preferences(st.session_state['user_id'], new_preference)
            st.write("Updated Preferences:", updated_preferences)

if __name__ == "__main__":
    main()
