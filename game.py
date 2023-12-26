import tkinter as tk
import random
import time

word_list = [
    "the", "be", "of", "and", "a", "to", "in", "he", "have", "it", "that", "for",
    "they", "with", "as", "not", "on", "she", "at", "by", "this", "we", "you",
    "do", "but", "from", "or", "which", "one", "would", "all", "will", "there",
    "say", "who", "make", "when", "can", "more", "if", "no", "man", "out", "other",
    "so", "what", "time", "up", "go", "about", "than", "into", "could", "state",
    "only", "new", "year", "some", "take", "come", "these", "know", "see", "use",
    "get", "like", "then", "first", "any", "work", "now", "may", "such", "give",
    "over", "think", "most", "even", "find", "day", "also", "after", "way", "many",
    "must", "look", "before", "great", "back", "through", "long", "where", "much",
    "should", "well", "people", "down", "own", "just", "because", "good", "each",
    "those", "feel", "seem", "how", "high", "too", "place", "little", "world",
    "very", "still", "nation", "hand", "old", "life", "tell", "write", "become",
    "under", "last", "nation", "consider", "though", "live", "thought", "fast"
]
def start_typing_test():
    def update_wpm():
        nonlocal words_typed, start_time, wpm_started
        elapsed_time = time.time() - start_time
        if wpm_started and elapsed_time > 0:
            words_per_minute = int((words_typed / elapsed_time) * 60)
            wpm_label.config(text=f"WPM: {words_per_minute}")
        if elapsed_time < 30:
            root.after(1000, update_wpm)
        else:
            wpm_label.config(text=f"You wrote {words_per_minute} words per minute!")

    def start_countdown():
        nonlocal timer_seconds, start_time, wpm_started
        wpm_started = True
        start_time = time.time()
        timer_seconds = 30
        update_words_display()
        update_wpm()
        countdown()

    def countdown():
        nonlocal timer_seconds
        if timer_seconds > 0:
            timer_label.config(text=f"Time left: {timer_seconds} s")
            timer_seconds -= 1
            root.after(1000, countdown)
        else:
            input_entry.config(state="disabled")

    def check_input(event):
        nonlocal words_typed, current_word_index
        typed_word = input_entry.get().strip()
        if current_word_index < len(word_list) and typed_word == word_list[current_word_index]:
            words_typed += 1
            current_word_index += 1
            input_entry.delete(0, tk.END)
            update_words_display()

    def update_words_display():
        nonlocal current_word_index
        words_to_display = word_list[current_word_index:current_word_index + 60]
        formatted_words = []

        # Rearranging words in a 4x15 grid
        for i in range(0, len(words_to_display), 15):
            line = words_to_display[i:i + 15]
            formatted_line = " ".join(line)

            # Tagging the first word as 'cursive'
            if i == 0:
                formatted_line = f"*{line[0]}* " + " ".join(line[1:])

            formatted_words.append(formatted_line)

        words_label.config(text='\n'.join(formatted_words), justify='left')

    def restart_test():
        nonlocal words_typed, timer_seconds, current_word_index, wpm_started
        words_typed = 0
        timer_seconds = 0
        current_word_index = 0
        wpm_started = False
        words_label.config(text="")
        input_entry.delete(0, tk.END)  # Clearing the input field
        input_entry.config(state="normal")
        start_countdown()

    root = tk.Tk()
    root.geometry("800x400")  # Larger window size
    root.title("Typing Test - by Jens B.")

    random.shuffle(word_list)

    current_word_index = 0

    words_label = tk.Label(root, text="", font=("Arial", 16))  # Increased font size
    words_label.pack()

    input_entry = tk.Entry(root)
    input_entry.pack()
    input_entry.focus_set()
    input_entry.bind('<Key>', check_input)  # Check input on key press

    words_typed = 0
    wpm_label = tk.Label(root, text="WPM: 0")
    wpm_label.pack()

    timer_seconds = 30
    timer_label = tk.Label(root, text="", font=("Arial", 12))
    timer_label.pack()

    start_time = 0
    wpm_started = False

    start_button = tk.Button(root, text="Start", command=start_countdown)
    start_button.pack()

    restart_button = tk.Button(root, text="Restart", command=restart_test)
    restart_button.pack()

    root.mainloop()

start_typing_test()