# app.py
import streamlit as st

# Set the title of the web page
st.title("CLI to Streamlit Host Example")

# --- REPLACING input("Enter your name") ---
# Use st.text_input for user input.
# The user's input is stored in the 'name' variable in real-time.
name = st.text_input("Enter your name")

# --- REPLACING print(f"Hello!, {name}") ---

# We only want to display the greeting if the user has actually entered something.
if name:
    # Use st.write, st.header, or st.success to display the output.
    # We use an f-string, just like your original code, to format the output.
    st.header(f"Hello!, {name}") 
else:
    # A friendly prompt when the input field is empty
    st.info("Please enter your name above to see the greeting.")
