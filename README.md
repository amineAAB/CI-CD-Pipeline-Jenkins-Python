# 🚀 CI/CD Pipeline with Jenkins & Python

## 🧩 Project Overview
This project demonstrates the implementation of a **complete CI/CD pipeline** using **Jenkins** and **Python**.  
It automates **unit testing** and integrates with **GitHub** to trigger builds automatically after each push,  
as well as **scheduled builds every 5 minutes**.  

The project simulates a **real-world DevOps workflow** — from **version control** to **automated testing** and **continuous integration** — within a lightweight WSL environment.

---

## ⚙️ Architecture

**Developer → GitHub → Jenkins → Test Execution → Build Result**

- **GitHub:** Hosts source code and triggers webhook on each push  
- **Jenkins:** Automates testing and build process  
- **Python (unittest):** Provides unit testing framework  
- **WSL Environment:** Local Linux setup for DevOps automation  

---



## 🔁 CI/CD Workflow

### 🔹 Continuous Integration
- Every **GitHub push** triggers Jenkins automatically via a webhook.  
- Jenkins pulls the latest code, installs dependencies if necessary, and runs the test suite (`unittest`).  

---

### 🔹 Scheduled Builds
Builds are also scheduled **every 5 minutes** using Jenkins cron syntax:

```groovy
triggers {
    cron('H/5 * * * *')
}
```

This ensures the pipeline is regularly validated even without new commits.


---  


### 🔹 Automated Testing
- Jenkins runs:

```bash
python3 -m unittest test_script.py
```

---

## 🖼️ CI/CD Diagram



```
Developer → GitHub → Jenkins → Test Execution → Build Result
```


---

## Example Output

```bash
$ python3 -m unittest test_script.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

---


## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| 🐍 **Python** | Application and unit testing |
| 🧰 **Jenkins** | Automation and CI/CD orchestration |
| 💾 **Git / GitHub** | Version control and webhook triggers |
| 🐧 **WSL (Ubuntu)** | Local Linux environment |
| ⏱️ **Cron** | Scheduled periodic builds |



---


## 💡 Key Features

✅ Fully automated CI/CD pipeline  
✅ GitHub webhook integration  
✅ Scheduled builds every 5 minutes  
✅ Real-time build logs in Jenkins  
✅ Unit test automation with Python





