import tkinter as tk
import random


# -------------------------------
# Game Settings
# -------------------------------

MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_ATTEMPTS = 10

secret_number = 0
attempts = 0
game_over = False


# -------------------------------
# Game Functions
# -------------------------------

def start_new_game():
    """Start a new game and reset all values."""

    global secret_number, attempts, game_over

    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts = 0
    game_over = False

    guess_entry.config(state="normal")
    guess_entry.delete(0, tk.END)

    guess_button.config(state="normal")

    message_label.config(
        text="یک عدد بین ۱ تا ۱۰۰ حدس بزن!",
        fg="#A1A1AA"
    )

    result_label.config(
        text="",
        fg="#FFFFFF"
    )

    update_attempts()


def update_attempts():
    """Update the remaining attempts counter."""

    remaining = MAX_ATTEMPTS - attempts

    attempts_label.config(
        text=f"تلاش باقی‌مانده: {remaining} از {MAX_ATTEMPTS}"
    )


def check_guess(event=None):
    """Check the user's guessed number."""

    global attempts, game_over

    if game_over:
        return

    user_input = guess_entry.get().strip()

    # Validate the input
    if not user_input.isdigit():
        message_label.config(
            text="لطفاً فقط یک عدد وارد کنید!",
            fg="#F87171"
        )
        return

    guess = int(user_input)

    if guess < MIN_NUMBER or guess > MAX_NUMBER:
        message_label.config(
            text="عدد باید بین ۱ تا ۱۰۰ باشد!",
            fg="#F87171"
        )
        return

    # Increase the attempt counter
    attempts += 1

    # Check the guessed number
    if guess == secret_number:

        game_over = True

        result_label.config(
            text="🎉 تبریک! شما برنده شدید!",
            fg="#4ADE80"
        )

        message_label.config(
            text=f"عدد صحیح {secret_number} بود.",
            fg="#4ADE80"
        )

        end_game()

    elif attempts == MAX_ATTEMPTS:

        game_over = True

        result_label.config(
            text="متأسفانه شما بازنده شدید!",
            fg="#F87171"
        )

        message_label.config(
            text=f"عدد صحیح {secret_number} بود.",
            fg="#F87171"
        )

        end_game()

    elif guess < secret_number:

        message_label.config(
            text="عدد بزرگ‌تری حدس بزنید ↑",
            fg="#FBBF24"
        )

    else:

        message_label.config(
            text="عدد کوچک‌تری حدس بزنید ↓",
            fg="#FBBF24"
        )

    update_attempts()

    # Clear the input field
    guess_entry.delete(0, tk.END)


def end_game():
    """Disable the game input after finishing."""

    guess_entry.config(state="disabled")
    guess_button.config(state="disabled")


# -------------------------------
# GUI Functions
# -------------------------------

def create_window():
    """Create the main application window."""

    window = tk.Tk()

    window.title("Number Guessing Game")
    window.geometry("500x530")
    window.resizable(False, False)

    window.configure(bg="#18181B")

    return window


def create_widgets(window):
    """Create and arrange all GUI components."""

    global guess_entry
    global guess_button
    global message_label
    global attempts_label
    global result_label

    # Main container
    main_frame = tk.Frame(
        window,
        bg="#27272A",
        padx=30,
        pady=30
    )

    main_frame.pack(
        padx=30,
        pady=30,
        fill="both",
        expand=True
    )

    # Game title
    title_label = tk.Label(
        main_frame,
        text="NUMBER GUESSING",
        font=("Segoe UI", 21, "bold"),
        bg="#27272A",
        fg="#A78BFA"
    )

    title_label.pack(pady=(10, 5))

    # Subtitle
    subtitle_label = tk.Label(
        main_frame,
        text="بازی حدس عدد",
        font=("Segoe UI", 14),
        bg="#27272A",
        fg="#FFFFFF"
    )

    subtitle_label.pack(pady=(0, 20))

    # Game instructions
    instruction_label = tk.Label(
        main_frame,
        text="یک عدد بین ۱ تا ۱۰۰ انتخاب شده است.",
        font=("Segoe UI", 11),
        bg="#27272A",
        fg="#A1A1AA"
    )

    instruction_label.pack(pady=5)

    # Attempts counter
    attempts_label = tk.Label(
        main_frame,
        text="",
        font=("Segoe UI", 11, "bold"),
        bg="#27272A",
        fg="#A78BFA"
    )

    attempts_label.pack(pady=15)

    # Input field
    guess_entry = tk.Entry(
        main_frame,
        font=("Segoe UI", 18),
        justify="center",
        width=15,
        bg="#3F3F46",
        fg="#FFFFFF",
        insertbackground="#FFFFFF",
        relief="flat"
    )

    guess_entry.pack(ipady=10, pady=10)

    # Guess button
    guess_button = tk.Button(
        main_frame,
        text="بررسی حدس",
        font=("Segoe UI", 12, "bold"),
        bg="#7C3AED",
        fg="#FFFFFF",
        activebackground="#6D28D9",
        activeforeground="#FFFFFF",
        relief="flat",
        cursor="hand2",
        command=check_guess
    )

    guess_button.pack(fill="x", ipady=8, pady=10)

    # Feedback message
    message_label = tk.Label(
        main_frame,
        text="یک عدد حدس بزن!",
        font=("Segoe UI", 12),
        bg="#27272A",
        fg="#A1A1AA"
    )

    message_label.pack(pady=15)

    # Game result
    result_label = tk.Label(
        main_frame,
        text="",
        font=("Segoe UI", 14, "bold"),
        bg="#27272A"
    )

    result_label.pack(pady=5)

    # Restart button
    restart_button = tk.Button(
        main_frame,
        text="شروع مجدد بازی",
        font=("Segoe UI", 11, "bold"),
        bg="#3F3F46",
        fg="#FFFFFF",
        activebackground="#52525B",
        activeforeground="#FFFFFF",
        relief="flat",
        cursor="hand2",
        command=start_new_game
    )

    restart_button.pack(fill="x", ipady=8, pady=(20, 5))

    # Press Enter to submit the guess
    guess_entry.bind("<Return>", check_guess)


# -------------------------------
# Main Function
# -------------------------------

def main():

    window = create_window()

    create_widgets(window)

    start_new_game()

    guess_entry.focus()

    window.mainloop()


# Run the program
if __name__ == "__main__":
    main()
