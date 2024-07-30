import time

def calculate_speed(text, typed_text, time_taken):
    words_typed = len(typed_text.split())
    cpm = (len(typed_text) / time_taken) * 60
    wpm = (words_typed / time_taken) * 60
    errors = sum(1 for i, j in zip(text, typed_text) if i != j)
    accuracy = ((words_typed - errors) / words_typed) * 100 if words_typed != 0 else 0
    return cpm, wpm, accuracy, errors

def main():
    user_choice = int(input('''Enter your choice:
1. Type a passage we suggest
2. Give a passage and type the passage you gave once the time starts
3. Type whatever as a passage
Your choice: '''))

    if user_choice == 1:
        text = "sample text for testing your typing speed"
        print("Type the following text:")
        print(text)
        input("Press Enter when ready...")
        
    elif user_choice == 2:
        text = input("Enter the passage: \n")
        print("Type the following text:")
        print(text)
        input("Press Enter when ready...")
        
    elif user_choice == 3:
        text = ""
        input("Press Enter when ready...")
        
    else:
        print("Invalid choice")
        return
    start_time = time.time()
    
    if user_choice == 3:
        typed_text = input("Start typing whatever comes in your mind: ")
    else:
        typed_text = input("Type the above text: ")
    
    end_time = time.time()
    time_taken = end_time - start_time
    cpm, wpm, accuracy, errors = calculate_speed(text, typed_text, time_taken)



    print(f"CPM: {cpm:.2f}")
    print(f"WPM: {wpm:.2f}")
    if user_choice != 3:
        print(f"Accuracy: {accuracy:.2f}%")
        print(f"Errors: {errors}")
    print(f"Time taken: {time_taken:.2f} seconds")

if __name__ == "__main__":
    main()
