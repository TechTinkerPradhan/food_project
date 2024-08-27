from user_auth import save_user_preferences, load_user_preferences

def update_preferences(user_id, new_preference):
    preferences = load_user_preferences(user_id)
    preferences.append(new_preference)
    save_user_preferences(user_id, preferences)
    return preferences
