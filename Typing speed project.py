import streamlit as st
import time

st.title("TYPE SPEED TEST")

def calculate_speed(text, typed_text, time_taken):
    words_typed = len(typed_text.split())
    cpm = (len(typed_text) / time_taken) * 60
    wpm = (words_typed / time_taken) * 60
    errors = sum(1 for i, j in zip(text, typed_text) if i != j)
    accuracy = ((words_typed - errors) / words_typed) * 100 if words_typed != 0 else 0
    return cpm, wpm, accuracy, errors

# Initialize session state variables
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'text' not in st.session_state:
    st.session_state.text = None

def choice1():
    st.markdown("Type a passage we suggest")
    st.session_state.text = "Touch typing allows for faster, more accurate typing by training your fingers to press the correct keys without looking at the keyboard."
    st.write("Type the following text:")
    st.write(st.session_state.text)
    
    if st.button("Start"):
        st.session_state.start_time = time.time()
    
    typed_text = st.text_input("Type Here")
    
    if st.button("Stop"):
        if st.session_state.start_time is not None:
            end_time = time.time()
            time_taken = end_time - st.session_state.start_time
            cpm, wpm, accuracy, errors = calculate_speed(st.session_state.text, typed_text, time_taken)
            st.write(f"CPM: {cpm:.2f}")
            st.write(f"WPM: {wpm:.2f}")
            st.write(f"Accuracy: {accuracy:.2f}%")
            st.write(f"Errors: {errors}")
            st.write(f"Time taken: {time_taken}")
        else:
            st.write("Please click 'Start' before stopping the test.")

def choice2():
    st.markdown("Give a passage and type the passage you gave once the time starts")
    st.session_state.text = st.text_area("Enter the passage:")
    st.write("Type the following text:")
    st.write(st.session_state.text)
    
    if st.button("Start"):
        st.session_state.start_time = time.time()
    
    typed_text = st.text_input("Type Here")
    
    if st.button("Stop"):
        if st.session_state.start_time is not None:
            end_time = time.time()
            time_taken = end_time - st.session_state.start_time
            cpm, wpm, accuracy, errors = calculate_speed(st.session_state.text, typed_text, time_taken)
            st.write(f"CPM: {cpm:.2f}")
            st.write(f"WPM: {wpm:.2f}")
            st.write(f"Accuracy: {accuracy:.2f}%")
            st.write(f"Errors: {errors}")
            st.write(f"Time taken: {time_taken}")
        else:
            st.write("Please click 'Start' before stopping the test.")

def choice3():
    st.markdown("Type whatever as a passage Your choice")
    st.session_state.text = ""
    
    if st.button("Start"):
        st.session_state.start_time = time.time()
    
    typed_text = st.text_input("Type Here")
    
    if st.button("Stop"):
        if st.session_state.start_time is not None:
            end_time = time.time()
            time_taken = end_time - st.session_state.start_time
            cpm, wpm, accuracy, errors = calculate_speed(st.session_state.text, typed_text, time_taken)
            st.write(f"CPM: {cpm:.2f}")
            st.write(f"WPM: {wpm:.2f}")
            st.write(f"Accuracy: {accuracy:.2f}%")
            st.write(f"Errors: {errors}")
            st.write(f"Time taken: {time_taken}")
        else:
            st.write("Please click 'Start' before stopping the test.")

selected_page = st.sidebar.selectbox('User choice', ['Type a passage we suggest', 'Give a passage and type the passage you gave once the time starts', 'Type whatever as a passage'])

if selected_page == "Type a passage we suggest":
    choice1()
elif selected_page == "Give a passage and type the passage you gave once the time starts":
    choice2()
elif selected_page == "Type whatever as a passage":
    choice3()
