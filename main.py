import tkinter as tk
from monitor import start_session, log_key, stop_session
from defensive import generate_defensive_report

monitoring = False


def on_key(event):
    if monitoring:
        log_key(event)


def start_monitoring():
    global monitoring
    if monitoring:
        return  # Prevent double start

    monitoring = True
    start_session()
    status_label.config(text="● MONITORING ACTIVE", fg="#00ff99")
    root.title("Ethical Keystroke Monitor - ACTIVE")


def stop_monitoring():
    global monitoring
    if not monitoring:
        return

    monitoring = False
    stop_session()
    status_label.config(text="● MONITORING STOPPED", fg="#ff6666")
    root.title("Ethical Keystroke Monitor - STOPPED")


def minimize_app():
    root.iconify()


def generate_report():
    path = generate_defensive_report()
    report_label.config(text=f"Security report generated:\n{path}")


# ================= UI SETUP =================

root = tk.Tk()
root.title("Ethical Keystroke Monitor")
root.geometry("520x420")
root.configure(bg="#1e1e1e")

FONT_TITLE = ("Segoe UI", 16, "bold")
FONT_BTN = ("Segoe UI", 11, "bold")
FONT_TEXT = ("Segoe UI", 10)

# Header
tk.Label(
    root,
    text="Ethical Keystroke Monitor",
    font=FONT_TITLE,
    fg="#00ccff",
    bg="#1e1e1e"
).pack(pady=10)

# Status
status_label = tk.Label(
    root,
    text="● MONITORING STOPPED",
    font=("Segoe UI", 12, "bold"),
    fg="#ff6666",
    bg="#1e1e1e"
)
status_label.pack(pady=5)

# Typing Area (Required for Focus)
tk.Label(
    root,
    text="Type here to simulate keystrokes (required for logging):",
    font=("Segoe UI", 9),
    fg="#aaaaaa",
    bg="#1e1e1e"
).pack(pady=(5, 2))

typing_box = tk.Text(
    root,
    height=4,
    width=60,
    font=("Consolas", 10),
    bg="#111111",
    fg="#00ffcc",
    insertbackground="#00ffcc"
)
typing_box.pack(pady=5)

# Control Frame
control_frame = tk.Frame(root, bg="#2b2b2b", bd=2, relief="groove")
control_frame.pack(padx=15, pady=10, fill="x")

tk.Label(
    control_frame,
    text="Monitoring Controls",
    font=("Segoe UI", 12, "bold"),
    fg="#ffffff",
    bg="#2b2b2b"
).pack(pady=5)

tk.Button(
    control_frame,
    text="▶ Start Monitoring (Consent)",
    font=FONT_BTN,
    bg="#00aa88",
    fg="white",
    command=start_monitoring,
    width=32
).pack(pady=5)

tk.Button(
    control_frame,
    text="■ Stop Monitoring",
    font=FONT_BTN,
    bg="#cc4444",
    fg="white",
    command=stop_monitoring,
    width=32
).pack(pady=5)

tk.Button(
    control_frame,
    text="— Minimize (Run in Background)",
    font=FONT_BTN,
    bg="#444444",
    fg="white",
    command=minimize_app,
    width=32
).pack(pady=5)

# Defensive Section
defensive_frame = tk.Frame(root, bg="#2b2b2b", bd=2, relief="groove")
defensive_frame.pack(padx=15, pady=10, fill="x")

tk.Label(
    defensive_frame,
    text="Defensive Security Simulator",
    font=("Segoe UI", 12, "bold"),
    fg="#ffffff",
    bg="#2b2b2b"
).pack(pady=5)

tk.Button(
    defensive_frame,
    text="🛡 Generate Security Awareness Report",
    font=FONT_BTN,
    bg="#0066cc",
    fg="white",
    command=generate_report,
    width=36
).pack(pady=5)

report_label = tk.Label(
    defensive_frame,
    text="",
    font=FONT_TEXT,
    fg="#cccccc",
    bg="#2b2b2b",
    wraplength=480,
    justify="center"
)
report_label.pack(pady=5)

# Footer
tk.Label(
    root,
    text="Status is always visible. Logging is consent-based & ethical.",
    font=("Segoe UI", 9),
    fg="#888888",
    bg="#1e1e1e"
).pack(pady=8)

# Bind keys ONLY to typing box
typing_box.bind("<Key>", on_key)
typing_box.focus_set()

root.mainloop()
