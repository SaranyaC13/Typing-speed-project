
import time

def calculate_speed(text, time_taken, errors):
    words_typed = len(text.split())
    cpm = (len(text) / time_taken) * 60
    wpm = (words_typed / time_taken) * 60
    accuracy = ((words_typed - errors) / words_typed) * 100
    return cpm, wpm, accuracy

def main():
    text = "Sample text for typing speed test."
    print("Type the following text:")
    print(text)
    input("Press Enter when ready...")
    
    start_time = time.time()
    typed_text = input("Type the above text: ")
    end_time = time.time()
    
    errors = sum(1 for i, j in zip(text, typed_text) if i != j)
    
    cpm, wpm, accuracy = calculate_speed(typed_text, end_time - start_time, errors)
    
    print(f"CPM: {cpm:.2f}")
    print(f"WPM: {wpm:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    main()
