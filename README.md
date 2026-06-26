# 🔍 Advanced Python Port Scanner

A fast, multithreaded TCP Port Scanner built with Python that scans target hosts, identifies open ports, performs banner grabbing, detects common services, and exports scan results in multiple formats.

This project demonstrates Python networking, socket programming, multithreading, report generation, and cybersecurity fundamentals, making it an excellent portfolio project for aspiring SOC Analysts, Cybersecurity Analysts, and Python Developers.

---

## 🚀 Features

- ⚡ Fast multithreaded TCP port scanning
- 🌐 Scan IP addresses or hostnames
- 🔎 Service detection using common port mapping
- 🏷️ Banner grabbing
- 📊 Progress bar while scanning
- 🎨 Colored terminal output
- 📄 Export reports in:
  - TXT
  - JSON
  - CSV
- 🎯 Custom port range scanning
- 📌 Scan only common ports
- 📈 Scan statistics
- 🖥️ Command-line interface

---

## 📁 Project Structure

```
Advanced-Port-Scanner/
│
├── scanner.py
├── banner.py
├── common_ports.py
├── report.py
├── utils.py
├── requirements.txt
├── README.md
```

---

## 🛠 Technologies Used

- Python 3
- Socket Programming
- ThreadPoolExecutor
- Colorama
- tqdm
- JSON
- CSV

---

## 📦 Installation

### Clone the repository

```bash
git clone https://github.com/HK690/Port-Scanner.git

cd Port-Scanner
```

### Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

Command Prompt

```bash
venv\Scripts\activate
```

PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Scan default ports (1-1024)

```bash
python scanner.py scanme.nmap.org
```

---

### Scan custom port range

```bash
python scanner.py scanme.nmap.org --start 20 --end 1000
```

---

### Scan common ports

```bash
python scanner.py scanme.nmap.org --common
```

---

### Increase thread count

```bash
python scanner.py scanme.nmap.org --threads 200
```

---

## 📊 Sample Output

```
========================================================
Target : scanme.nmap.org

Scanning...

[OPEN] Port 22    | SSH
[OPEN] Port 80    | HTTP
[OPEN] Port 443   | HTTPS

Scan Completed

Open Ports : 3

Time Taken : 2.14 seconds
========================================================
```

---

## 📄 Reports Generated

After each scan, reports are automatically saved in the `reports/` directory.

Example:

```
reports/
│
├── scan_20260626_181500.txt
├── scan_20260626_181500.csv
└── scan_20260626_181500.json
```
1.
<img width="910" height="241" alt="image" src="https://github.com/user-attachments/assets/21d32981-da1c-4a73-b0df-6cf2dd7935b0" />

2.
<img width="869" height="442" alt="image" src="https://github.com/user-attachments/assets/643561cd-af8b-4854-bc9e-c801f2843a4d" />

3.
<img width="680" height="436" alt="image" src="https://github.com/user-attachments/assets/39e1723c-5601-4f77-b32e-fd100c09f817" />

---

## 🔍 Supported Features

| Feature | Status |
|----------|--------|
| TCP Port Scan | ✅ |
| Hostname Resolution | ✅ |
| Banner Grabbing | ✅ |
| Service Detection | ✅ |
| Multithreading | ✅ |
| Progress Bar | ✅ |
| TXT Report | ✅ |
| JSON Report | ✅ |
| CSV Report | ✅ |
| Colored Output | ✅ |

---

## 📚 Learning Objectives

This project helped demonstrate:

- Python Networking
- Socket Programming
- Multithreading
- TCP Connections
- Banner Grabbing
- Report Generation
- Cybersecurity Fundamentals
- Command Line Applications

---

## 🚧 Future Improvements

- HTML Report Generation
- Excel (.xlsx) Reports
- Service Version Detection
- UDP Port Scanning
- CIDR/Subnet Scanning
- IP Geolocation
- Vulnerability Detection
- Streamlit Web Dashboard
- GUI Version
- Nmap XML Export

---

## ⚠️ Disclaimer

This tool is intended **only for educational purposes and authorized security testing**.

Only scan systems that you own or have explicit permission to test. Unauthorized scanning may violate laws, regulations, or organizational policies.

---

## 🤝 Contributing

Contributions are welcome!

Feel free to fork the repository, open issues, or submit pull requests to improve the project.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Harshal Kapse**

Cybersecurity Enthusiast | Python Developer | SOC Analyst Aspirant

If you found this project useful, don't forget to ⭐ star the repository!
