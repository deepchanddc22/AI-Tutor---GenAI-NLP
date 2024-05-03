import streamlit as st
import subprocess


def run_streamlit_app():
    subprocess.Popen(["streamlit", "run", "main.py"])

def run_data_extraction():
    subprocess.Popen(["streamlit", "run", "dataextracter.py"])

def main():
    st.title("AI Tutor 🤖")

    option = st.radio("Choose an option", ("Upload Document", "Start Test"))

    if option == "Upload Document":
        run_data_extraction()

    elif option == "Start Test":
        st.write("Click the button below to start the test")
        if st.button("Start Test"):
            run_streamlit_app()  # Run the Streamlit app

if __name__ == "__main__":
    main()
