নিশ্চয়ই\! আপনার চাওয়া অনুযায়ী `README.md` ফাইলটি Markdown ফরম্যাটে নিচে দেওয়া হলো।

-----

````markdown:project ReadMe:README.md
# 📚 Student Eligibility System
_A simple Python program to check if a student is eligible for an exam._

---

## 🎯 Project Goal

This is a beginner-friendly project that helps new programmers understand how to use **conditional logic** (`if` and `else`) to make decisions based on specific criteria. The program determines if a student can sit for an exam by checking their attendance and assignment submission status.

---

## ✨ Key Features

* **Input Validation:** Takes a student's attendance percentage and assignment submission status as input.
* **Rule-Based Logic:** Applies two strict rules to decide eligibility.
* **Clear Decision:** Provides a clear "Allowed" or "Not Allowed" output.

---

## 📜 Eligibility Rules

To be eligible for the exam, a student must meet **both** of the following criteria:

* **Attendance:** Attendance must be **75% or higher**.
* **Assignment:** The assignment must be **submitted**.

If either of these conditions is not met, the student is not allowed to take the exam.

---

## 🚀 How to Run

1.  Save the code as a Python file (e.g., `student_eligibility.py`).
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the program using the following command:
    ```bash
    python student_eligibility.py
    ```

---

## 📝 Example Usage

* **Allowed:**
    * **Input:** Attendance `80`, Assignment `yes`
    * **Output:** `Allowed to take exam`

* **Not Allowed (Low Attendance):**
    * **Input:** Attendance `70`, Assignment `yes`
    * **Output:** `Not allowed`

* **Not Allowed (Missing Assignment):**
    * **Input:** Attendance `90`, Assignment `no`
    * **Output:** `Not allowed`

