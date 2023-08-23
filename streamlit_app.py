import streamlit as st
import random

def main():
    st.title("Random Number Generator")
    
    # Generate a random number
    random_number = random.randint(1, 100)
    
    st.write(f"Generated Random Number: {random_number}")
    
    st.write("Welcome to this simple Streamlit app. It generates a random number and displays it.")
    
if __name__ == "__main__":
    main()
