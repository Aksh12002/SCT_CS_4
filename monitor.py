from datetime import datetime

LOG_FILE = "keystrokes.log"
current_line = ""


def start_session():
    global current_line
    current_line = ""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write("\n--- Session Started ---\n")
        f.write(f"Time: {datetime.now()}\n")


def log_key(event):
    global current_line

    # ENTER → write full line
    if event.keysym == "Return":
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(current_line + "\n")
        current_line = ""

    # BACKSPACE → record + modify buffer
    elif event.keysym == "BackSpace":
        current_line += "<BACKSPACE>"
        # Also remove last normal character if exists
        # (optional, keeps buffer realistic)
        # You can comment this out if you want pure key logging
        # current_line = current_line[:-1]

    # DELETE key
    elif event.keysym == "Delete":
        current_line += "<DELETE>"

    # TAB key
    elif event.keysym == "Tab":
        current_line += "<TAB>"

    # SPACE
    elif event.keysym == "space":
        current_line += " "

    # NORMAL printable characters
    elif len(event.char) == 1 and event.char.isprintable():
        current_line += event.char

    # OTHER special keys (arrows, shift, ctrl, etc.)
    else:
        # Log other keys symbolically
        current_line += f"<{event.keysym}>"
        
def stop_session():
    global current_line

    if current_line:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(current_line + "\n")
        current_line = ""

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write("--- Session Ended ---\n")
