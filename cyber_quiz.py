import tkinter as tk
from tkinter import messagebox
import random

# ======================= QUESTION BANK =======================

question_bank = {

    # ======================= UNIT 1 =======================
    1: [
        {"q":"Cyber security focuses on protecting:",
         "o":["Computer systems, networks, and data","Only mobile phones","Only hardware","Only cloud storage"],
         "a":0,"i":"Sony Pictures attack (2014) showed how systems and data must be protected."},

        {"q":"Confidentiality ensures:",
         "o":["Data is kept private","Data is always available","Data loads faster","Data is deleted"],
         "a":0,"i":"Yahoo breach exposed billions of accounts, breaking confidentiality."},

        {"q":"Integrity refers to:",
         "o":["Accuracy of data","Speed of data","Encryption","Backup"],
         "a":0,"i":"Attackers modifying databases damages integrity."},

        {"q":"Availability means:",
         "o":["Data accessible when needed","Data hidden","Data encrypted","Data deleted"],
         "a":0,"i":"DDoS attacks affect availability of services."},

        {"q":"CIA triad stands for:",
         "o":["Confidentiality, Integrity, Availability","Control, Internet, Access","Cyber, Information, Assurance","Confidentiality, Internet, Access"],
         "a":0,"i":"CIA triad is the foundation of cyber security."},

        {"q":"Cybercrime is:",
         "o":["Illegal activity using internet","Online shopping","Video streaming","Email sending"],
         "a":0,"i":"Identity theft cases increased due to cybercrime."},

        {"q":"Phishing is:",
         "o":["Fake attempt to steal information","Encrypting data","Scanning virus","Blocking websites"],
         "a":0,"i":"Twitter Bitcoin scam started with phishing."},

        {"q":"Internet governance deals with:",
         "o":["Rules and policies of internet","Hardware manufacturing","Programming","Web designing"],
         "a":0,"i":"ICANN handles domain management."},

        {"q":"ICANN manages:",
         "o":["Domain names","Internet speed","Cyber laws","Firewalls"],
         "a":0,"i":"ICANN prevents duplicate domain names."},

        {"q":"Cyber threats include:",
         "o":["Virus, ransomware, phishing","Power failure","Slow internet","Low battery"],
         "a":0,"i":"Ransomware attacks increased globally."},

        {"q":"Malware is:",
         "o":["Malicious software","Hardware failure","Firewall","Antivirus"],
         "a":0,"i":"Malware infected systems during WannaCry."},

        {"q":"Data breach means:",
         "o":["Unauthorized access to data","Data backup","Data encryption","Data recovery"],
         "a":0,"i":"Equifax breach leaked millions of records."}
    ],

    # ======================= UNIT 2 =======================
    2: [
        {"q":"A cyber security vulnerability is:",
         "o":["A system weakness","Antivirus","Firewall","Backup"],
         "a":0,"i":"Equifax breach happened due to a vulnerability."},

        {"q":"Weak passwords can cause:",
         "o":["Unauthorized access","Better security","Fast login","More storage"],
         "a":0,"i":"Many social media accounts were hacked due to weak passwords."},

        {"q":"Outdated software is risky because:",
         "o":["Lacks security updates","Runs faster","Consumes less memory","Improves performance"],
         "a":0,"i":"WannaCry exploited outdated Windows systems."},

        {"q":"Human error includes:",
         "o":["Clicking phishing emails","Installing antivirus","Updating OS","Using firewall"],
         "a":0,"i":"Most ransomware starts with human error."},

        {"q":"Insider threat refers to:",
         "o":["Threat from employee","External hacker","Malware","Firewall"],
         "a":0,"i":"Tesla reported insider sabotage."},

        {"q":"Misconfiguration leads to:",
         "o":["Security gaps","Better performance","Fast internet","Extra storage"],
         "a":0,"i":"Cloud data leaks often happen due to misconfiguration."},

        {"q":"Poor backup practices result in:",
         "o":["Permanent data loss","Better security","Fast recovery","No impact"],
         "a":0,"i":"Hospitals lost data after ransomware attacks."},

        {"q":"Unsecured Wi-Fi can cause:",
         "o":["Data interception","High speed","Better signal","Encrypted traffic"],
         "a":0,"i":"Public Wi-Fi attacks are common."},

        {"q":"Access control ensures:",
         "o":["Authorized access only","Everyone access","Data sharing","Open access"],
         "a":0,"i":"Capital One breach involved access control failure."},

        {"q":"Audit in cyber security means:",
         "o":["Checking systems","Deleting files","Gaming","Formatting"],
         "a":0,"i":"Security audits detect weaknesses."},

        {"q":"Authentication verifies:",
         "o":["User identity","Battery","Speed","RAM"],
         "a":0,"i":"OTP verifies user identity."},

        {"q":"Deception techniques use:",
         "o":["Fake systems","Strong passwords","Encryption","Firewall"],
         "a":0,"i":"Honeypots trap attackers."}
    ],

    # ======================= UNIT 3 =======================
    3: [
        {"q":"IDS stands for:",
         "o":["Intrusion Detection System","Internet Data Server","Internal Device Setup","Information Delivery System"],
         "a":0,"i":"IDS detects suspicious activity."},

        {"q":"IPS stands for:",
         "o":["Intrusion Prevention System","Internet Protocol Service","Internal Protection Setup","Image Processing System"],
         "a":0,"i":"IPS blocks malicious traffic."},

        {"q":"Intrusion means:",
         "o":["Unauthorized access","Authorized login","System update","Backup"],
         "a":0,"i":"LinkedIn breach involved intrusion."},

        {"q":"Firewall acts as:",
         "o":["Network barrier","Battery saver","Storage","Antivirus"],
         "a":0,"i":"Firewalls block unauthorized traffic."},

        {"q":"Session monitoring tracks:",
         "o":["User activity","Battery","Brightness","Keyboard"],
         "a":0,"i":"Banks use session monitoring to detect fraud."},

        {"q":"Log analysis helps in:",
         "o":["Detecting attacks","Playing games","Formatting","Charging"],
         "a":0,"i":"Logs reveal suspicious patterns."},

        {"q":"Brute force attack involves:",
         "o":["Trying many passwords","Encrypting data","Updating OS","Blocking traffic"],
         "a":0,"i":"Weak passwords are cracked via brute force."},

        {"q":"DDoS attack aims to:",
         "o":["Overload server","Encrypt data","Improve speed","Fix bugs"],
         "a":0,"i":"GitHub faced massive DDoS attack."},

        {"q":"IDS mainly:",
         "o":["Detects attacks","Prevents attacks","Encrypts data","Deletes malware"],
         "a":0,"i":"IDS provides alerts."},

        {"q":"IPS mainly:",
         "o":["Prevents attacks","Monitors only","Logs only","Encrypts"],
         "a":0,"i":"IPS blocks intrusions automatically."},

        {"q":"Unauthorized access harms:",
         "o":["Data and systems","Screen","Keyboard","Mouse"],
         "a":0,"i":"Target breach caused major losses."},

        {"q":"Firewalls control:",
         "o":["Network traffic","Volume","Brightness","Camera"],
         "a":0,"i":"Firewalls filter traffic."}
    ],

    # ======================= UNIT 4 =======================
    4: [
        {"q":"Cryptography is used to:",
         "o":["Protect information","Increase speed","Play games","Improve battery"],
         "a":0,"i":"HTTPS uses cryptography."},

        {"q":"Encryption converts data into:",
         "o":["Ciphertext","Plain text","Image","Audio"],
         "a":0,"i":"Encrypted data is unreadable."},

        {"q":"Decryption converts:",
         "o":["Ciphertext to plaintext","Text to image","Audio to text","Data to virus"],
         "a":0,"i":"Banking systems decrypt data."},

        {"q":"TLS is used for:",
         "o":["Secure web communication","Gaming","Sound","Storage"],
         "a":0,"i":"TLS enables HTTPS."},

        {"q":"HTTPS means:",
         "o":["Secure HTTP","High speed transfer","Hidden text","Home protocol"],
         "a":0,"i":"Bank websites use HTTPS."},

        {"q":"Public key is:",
         "o":["Shared openly","Kept secret","Destroyed","Hidden"],
         "a":0,"i":"Public key is safe to share."},

        {"q":"Private key must be:",
         "o":["Kept secret","Shared publicly","Uploaded online","Sent to others"],
         "a":0,"i":"Leaked private keys compromise security."},

        {"q":"Symmetric encryption uses:",
         "o":["One key","Two keys","Passwords","Biometrics"],
         "a":0,"i":"AES is symmetric encryption."},

        {"q":"Asymmetric encryption uses:",
         "o":["Public & private keys","One key","OTP","Password"],
         "a":0,"i":"RSA uses two keys."},

        {"q":"Authentication verifies:",
         "o":["Identity","Speed","Memory","Brightness"],
         "a":0,"i":"OTP verifies users."},

        {"q":"VPN stands for:",
         "o":["Virtual Private Network","Verified Public Network","Voice Protocol Network","Visual Protection Node"],
         "a":0,"i":"VPN secures communication."},

        {"q":"Biometrics use:",
         "o":["Human traits","Passwords","Emails","Usernames"],
         "a":0,"i":"Fingerprint unlock uses biometrics."}
    ],

    5: []
}

# ======================= QUIZ APP =======================

class CyberQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Cyber Security Quiz")
        self.root.geometry("800x500")
        self.root.configure(bg="#111")

        self.username = ""
        self.score = 0
        self.q_index = 0
        self.questions = []

        self.build_name_screen()

    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()

    def build_name_screen(self):
        self.clear()
        tk.Label(self.root, text="CYBER SECURITY QUIZ", fg="cyan", bg="#111",
                 font=("Arial", 26, "bold")).pack(pady=40)

        tk.Label(self.root, text="Enter Your Name:", fg="white", bg="#111",
                 font=("Arial", 14)).pack()

        self.name_entry = tk.Entry(self.root, font=("Arial", 14))
        self.name_entry.pack(pady=10)

        tk.Button(self.root, text="Start", font=("Arial", 14),
                  command=self.chapter_screen).pack(pady=20)

    def chapter_screen(self):
        self.username = self.name_entry.get().strip()
        if not self.username:
            messagebox.showwarning("Error", "Please enter your name.")
            return

        self.clear()
        tk.Label(self.root, text=f"Welcome, {self.username}", fg="cyan",
                 bg="#111", font=("Arial", 22)).pack(pady=25)

        tk.Label(self.root, text="Select Chapter", fg="white", bg="#111",
                 font=("Arial", 16)).pack(pady=10)

        for i in range(1, 6):
            tk.Button(self.root, text=f"Chapter {i}", width=20,
                      font=("Arial", 14),
                      command=lambda c=i: self.start_quiz(c)).pack(pady=6)

    def start_quiz(self, chapter):
        if not question_bank[chapter]:
            messagebox.showinfo("Empty", "This chapter has no questions yet.")
            return

        self.questions = random.sample(question_bank[chapter], 5)
        self.score = 0
        self.q_index = 0
        self.show_question()

    def show_question(self):
        self.clear()
        q = self.questions[self.q_index]

        tk.Label(self.root, text=f"Q{self.q_index+1}: {q['q']}",
                 fg="white", bg="#111", wraplength=700,
                 font=("Arial", 16)).pack(pady=20)

        self.answer_var = tk.IntVar()

        for i, opt in enumerate(q["o"]):
            tk.Radiobutton(self.root, text=opt, variable=self.answer_var,
                           value=i, fg="white", bg="#111",
                           selectcolor="#111",
                           font=("Arial", 13)).pack(anchor="w", padx=100)

        tk.Button(self.root, text="Submit", font=("Arial", 14),
                  command=self.check_answer).pack(pady=20)

    def check_answer(self):
        q = self.questions[self.q_index]
        if self.answer_var.get() == q["a"]:
            self.score += 1
            messagebox.showinfo("Correct ✔️", q["i"])
        else:
            messagebox.showerror("Wrong ❌",
                                 f"Correct Answer: {q['o'][q['a']]}\n\n{q['i']}")

        self.q_index += 1
        if self.q_index < len(self.questions):
            self.show_question()
        else:
            messagebox.showinfo("Quiz Completed 🎉",
                                f"{self.username}, your score is {self.score}/5")
            self.chapter_screen()


# ======================= RUN APP =======================

if __name__ == "__main__":
    root = tk.Tk()
    CyberQuiz(root)
    root.mainloop()
