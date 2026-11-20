
import tkinter as tk
from tkinter import ttk
from collections import Counter
import re


# --------------------------------
# Application Settings
# --------------------------------

BG_COLOR = "#18181B"
FRAME_COLOR = "#27272A"
INPUT_COLOR = "#3F3F46"
ACCENT_COLOR = "#7C3AED"
TEXT_COLOR = "#FFFFFF"
SECONDARY_COLOR = "#A1A1AA"
SUCCESS_COLOR = "#4ADE80"

window = None
text_input = None
result_box = None


# --------------------------------
# Text Analysis Functions
# --------------------------------

def analyze_text(text):
    """Analyze the input text and return statistics."""

    # Check if the input is empty
    if not text.strip():
        return None

    # Extract words (Persian and English)
    words = re.findall(r"\w+", text.casefold())

    # Count words and characters
    word_count = Counter(words)
    char_count = Counter(
        char for char in text if not char.isspace()
    )

    # Calculate statistics
    total_chars = len(text)
    chars_without_spaces = sum(
        1 for char in text if not char.isspace()
    )

    total_words = len(words)
    unique_words = len(word_count)

    letters = sum(1 for char in text if char.isalpha())
    digits = sum(1 for char in text if char.isdigit())
    spaces = sum(1 for char in text if char.isspace())

    # Most frequent word
    most_common_word = word_count.most_common(1)

    # Most frequent character
    most_common_char = char_count.most_common(1)

    # Average word length
    average_length = (
        sum(len(word) for word in words) / total_words
        if total_words > 0 else 0
    )

    return {
        "total_chars": total_chars,
        "chars_without_spaces": chars_without_spaces,
        "total_words": total_words,
        "unique_words": unique_words,
        "letters": letters,
        "digits": digits,
        "spaces": spaces,
        "average_length": average_length,
        "most_common_word": most_common_word,
        "most_common_char": most_common_char,
        "word_count": word_count,
        "char_count": char_count
    }


# --------------------------------
# Display Results
# --------------------------------

def display_results(data):
    """Display text analysis results in the GUI."""

    result_box.config(state="normal")
    result_box.delete("1.0", tk.END)

    if data is None:
        result_box.insert(
            tk.END,
            "لطفاً ابتدا یک متن وارد کنید."
        )
        result_box.config(state="disabled")
        return

    result = []

    result.append("📊 نتایج تحلیل متن")
    result.append("=" * 35)

    result.append("\nآمار کلی:")
    result.append(f"تعداد کل کاراکترها: {data['total_chars']}")
    result.append(
        f"کاراکترها بدون فاصله: {data['chars_without_spaces']}"
    )
    result.append(f"تعداد کلمات: {data['total_words']}")
    result.append(f"تعداد کلمات یکتا: {data['unique_words']}")

    result.append("\nآمار کاراکترها:")
    result.append(f"تعداد حروف: {data['letters']}")
    result.append(f"تعداد اعداد: {data['digits']}")
    result.append(f"تعداد فاصله‌ها: {data['spaces']}")

    result.append("\nپرتکرارترین موارد:")

    if data["most_common_word"]:
        word, count = data["most_common_word"][0]
        result.append(
            f"پرتکرارترین کلمه: {word} ({count} بار)"
        )

    if data["most_common_char"]:
        char, count = data["most_common_char"][0]
        result.append(
            f"پرتکرارترین کاراکتر: {char} ({count} بار)"
        )

    result.append(
        f"میانگین طول کلمات: {data['average_length']:.2f}"
    )

    result.append("\nتکرار هر کلمه:")

    for word, count in data["word_count"].most_common():
        result.append(f"{word} : {count} بار")

    result.append("\nتکرار هر کاراکتر:")

    for char, count in data["char_count"].most_common():
        result.append(f"{char} : {count} بار")

    result_box.insert(tk.END, "\n".join(result))
    result_box.config(state="disabled")


# --------------------------------
# GUI Event Functions
# --------------------------------

def on_analyze():
    """Get input text and analyze it."""

    text = text_input.get("1.0", "end-1c")

    data = analyze_text(text)

    display_results(data)


def clear_text():
    """Clear input and output fields."""

    text_input.delete("1.0", tk.END)

    result_box.config(state="normal")
    result_box.delete("1.0", tk.END)
    result_box.config(state="disabled")


# --------------------------------
# Window Creation
# --------------------------------

def create_window():
    """Create the main application window."""

    app = tk.Tk()

    app.title("Text Analyzer")
    app.geometry("750x750")
    app.minsize(600, 600)

    app.configure(bg=BG_COLOR)

    return app


# --------------------------------
# GUI Components
# --------------------------------

def create_widgets(app):
    """Create and arrange GUI components."""

    global text_input, result_box

    main_frame = tk.Frame(
        app,
        bg=FRAME_COLOR,
        padx=25,
        pady=20
    )

    main_frame.pack(
        fill="both",
        expand=True,
        padx=25,
        pady=25
    )

    # Application title
    title = tk.Label(
        main_frame,
        text="TEXT ANALYZER",
        font=("Segoe UI", 22, "bold"),
        bg=FRAME_COLOR,
        fg="#A78BFA"
    )

    title.pack(pady=(5, 5))

    # Subtitle
    subtitle = tk.Label(
        main_frame,
        text="تحلیلگر هوشمند متن",
        font=("Tahoma", 13),
        bg=FRAME_COLOR,
        fg=TEXT_COLOR
    )

    subtitle.pack(pady=(0, 15))

    # Input title
    input_label = tk.Label(
        main_frame,
        text="متن مورد نظر خود را وارد کنید:",
        font=("Tahoma", 11, "bold"),
        bg=FRAME_COLOR,
        fg=TEXT_COLOR,
        anchor="e"
    )

    input_label.pack(fill="x", pady=5)

    # Text input field
    text_input = tk.Text(
        main_frame,
        height=6,
        font=("Tahoma", 12),
        bg=INPUT_COLOR,
        fg=TEXT_COLOR,
        insertbackground=TEXT_COLOR,
        relief="flat",
        wrap="word"
    )

    text_input.pack(fill="x", pady=8)

    # Analyze button
    analyze_button = tk.Button(
        main_frame,
        text="تحلیل متن",
        font=("Tahoma", 11, "bold"),
        bg=ACCENT_COLOR,
        fg=TEXT_COLOR,
        activebackground="#6D28D9",
        activeforeground=TEXT_COLOR,
        relief="flat",
        cursor="hand2",
        command=on_analyze
    )

    analyze_button.pack(fill="x", ipady=8, pady=8)

    # Results title
    result_label = tk.Label(
        main_frame,
        text="گزارش تحلیل",
        font=("Tahoma", 12, "bold"),
        bg=FRAME_COLOR,
        fg=SUCCESS_COLOR
    )

    result_label.pack(pady=(12, 5))

    # Results container
    result_frame = tk.Frame(
        main_frame,
        bg=INPUT_COLOR
    )

    result_frame.pack(
        fill="both",
        expand=True,
        pady=5
    )

    # Scrollbar
    scrollbar = tk.Scrollbar(result_frame)

    scrollbar.pack(side="left", fill="y")

    # Results text box
    result_box = tk.Text(
        result_frame,
        font=("Tahoma", 11),
        bg=INPUT_COLOR,
        fg=TEXT_COLOR,
        relief="flat",
        wrap="word",
        padx=12,
        pady=10,
        yscrollcommand=scrollbar.set,
        state="disabled"
    )

    result_box.pack(
        side="right",
        fill="both",
        expand=True
    )

    scrollbar.config(command=result_box.yview)

    # Clear button
    clear_button = tk.Button(
        main_frame,
        text="پاک کردن متن",
        font=("Tahoma", 10, "bold"),
        bg="#3F3F46",
        fg=TEXT_COLOR,
        activebackground="#52525B",
        activeforeground=TEXT_COLOR,
        relief="flat",
        cursor="hand2",
        command=clear_text
    )

    clear_button.pack(fill="x", ipady=7, pady=(10, 0))


# --------------------------------
# Main Function
# --------------------------------

def main():

    global window

    window = create_window()

    create_widgets(window)

    window.mainloop()


# Run Application
if __name__ == "__main__":
    main()
