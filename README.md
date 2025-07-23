🚨 Automated Threat Detection & Incident Response System
A SIEM-driven solution for real-time log monitoring, threat analysis, and automated countermeasures

🔍 Overview
This project implements a Security Information and Event Management (SIEM) solution that enables:

Real-time log analysis

Threat detection using both rule-based and machine learning (Isolation Forest) methods

Automated responses to malicious activity, including IP blocking

Centralized visualization and alerting

Whether you're securing a single server or managing infrastructure at scale, this system helps you stay proactive against potential threats.

✨ Key Features
📥 Log Ingestion: Collects logs from SSH and syslog via Logstash

🧠 Threat Detection: Combines rule-based logic with ML-based anomaly detection (Isolation Forest)

📢 Live Alerts: Instantly notifies via Slack or Email on suspicious activity

🔒 Automated Defense: Dynamically blocks malicious IPs using iptables

📊 Dashboard: Visualize logs and threats in real-time with Kibana

⚙️ Installation
Clone the repository and run the setup:

bash
Copy
Edit
git clone https://github.com/Pawanchandraupreti/Threat-Detection-System.git
cd Threat-Detection-System
sudo bash setup/install_elk.sh
pip install -r requirements.txt
📌 Prerequisites
Python 3.8+

Elasticsearch, Logstash, and Kibana stack (auto-installed via setup)

Slack webhook or email SMTP settings for alerts

🧪 Want to Test It?
Simulate log entries or SSH brute-force attempts to see the detection and response system in action. Logs will be analyzed, alerts will be sent, and offending IPs will be blocked in real-time.

🤝 Contributions
Contributions, suggestions, and improvements are welcome! Please open an issue or submit a pull request.

📜 License
MIT License — Feel free to use and adapt for your own security projects.