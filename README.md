# ⌨️ Task 04 – Ethical Keystroke Monitor & Defensive Simulator

## 📌 Overview
This project is developed as **Task 04** of the **Cyber Security Internship**.  
It implements a **consent-based, application-scoped keystroke monitoring tool** combined with a **defensive security awareness simulator**.

The project demonstrates how keystroke monitoring works in a **controlled and ethical environment**, while also educating users about how malicious keyloggers operate and how they can be detected.

This tool is designed strictly for **educational and ethical cybersecurity purposes**.

---

## 🎯 Objectives
- Demonstrate how keystroke logging works at the application level
- Simulate background-style monitoring in a visible and ethical way
- Educate users about malicious keylogger behavior
- Promote defensive cybersecurity awareness
- Ensure responsible and consent-based monitoring practices

---

## 🔐 Key Features

### ✅ Consent-Based Keystroke Monitoring
- Logs keystrokes **only inside the application window**
- Requires explicit user action to start monitoring
- Status is always visible (Active / Stopped)
- User can stop monitoring at any time
- Logs are saved locally to a file

---

### 🧠 Keystroke Event Logging
- Records full text lines
- Logs special keys such as:
  - Backspace
  - Delete
  - Tab
  - Arrow keys
- Provides a more realistic keystroke event log
- Buffers input to create readable logs

---

### 🖥 Background-Style Behavior (Ethical)
- Application can be minimized
- Monitoring continues while minimized
- Status remains visible in the window title
- No hidden or stealth execution

---

### 🛡 Defensive Security Simulator
- Generates a security awareness report
- Explains how real malicious keyloggers operate
- Provides guidance on how to detect suspicious software
- Promotes defensive cybersecurity practices

---

## 🧱 Project Structure
```

SCT_CS_4/
│
├── main.py              # GUI application (ethical monitor)
├── monitor.py           # Keystroke logging logic
├── defensive.py         # Defensive security simulator
├── keystrokes.log       # Logged keystroke data
├── security_report.txt  # Generated security awareness report
└── README.md

````

---

## 🛠 Technologies Used
- Python 3
- Tkinter (GUI)
- Standard Python libraries
- File handling for secure local logging

---

## ⚙ How to Run
```bash
python main.py
````

---

## ▶ How It Works

### 🔐 Start Monitoring

1. Launch the application
2. Click **Start Monitoring (Consent)**
3. Type inside the provided typing area
4. Keystrokes are logged to `keystrokes.log`

---

### 🛑 Stop Monitoring

1. Click **Stop Monitoring**
2. Session ends
3. Remaining buffered keystrokes are saved

---

### 🧾 Defensive Simulator

* Click **Generate Security Awareness Report**
* A file named `security_report.txt` is created
* The report explains:

  * How malicious keyloggers work
  * How to detect suspicious behavior
  * Why ethical monitoring is important



