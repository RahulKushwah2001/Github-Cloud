#  GitHub Cloud Connector (FastAPI)

A simple and clean backend service built using FastAPI that integrates with the GitHub API.
This project demonstrates API integration, authentication, and modular backend architecture.

---

##  Features

*  Authentication using GitHub Personal Access Token (PAT)
*  Fetch repositories of a user
*  Create issues in a repository
*  List issues from a repository
*  Fetch commits from a repository
*  Create pull requests

---

## 🛠️ Tech Stack

* Python 3.x
* FastAPI
* Uvicorn
* Requests
* Pydantic

---

##  Project Structure

app/
├── main.py
├── config.py
├── api/
│   └── routes.py
├── models/
│   └── github.py
├── services/
│   └── github_service.py

---

##  Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/github-connector.git
cd github-connector
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup environment variables

Create a `.env` file in root:

```
GITHUB_TOKEN=your_github_personal_access_token
```

---

##  How to Run the Project

```bash
uvicorn app.main:app --reload
```

Open in browser:

👉 http://127.0.0.1:8000/docs

---

##  API Endpoints

### 🔹 Get User Repositories

```
GET /api/repos/{username}
```

---

### 🔹 Create Issue

```
POST /api/create-issue
```

Request Body:

```json
{
  "owner": "your-username",
  "repo": "your-repo",
  "title": "Issue title",
  "body": "Issue description"
}
```

---

### 🔹 List Issues

```
GET /api/list-issues?owner=your-username&repo=your-repo&state=open
```

---

### 🔹 Fetch Commits

```
GET /api/commits?owner=your-username&repo=your-repo
```

---

### 🔹 Create Pull Request

```
POST /api/create-pull-request
```

Request Body:

```json
{
  "owner": "your-username",
  "repo": "your-repo",
  "title": "PR title",
  "head": "feature-branch",
  "base": "main",
  "body": "PR description"
}
```

---

##  Notes

* Ensure your GitHub token has proper permissions (`repo`)
* Repository and branches must exist before creating PR
* API errors are handled and returned with proper messages

---

##  Highlights

* Clean modular architecture (routes, services, models)
* Proper error handling and validation
* Real GitHub API integration
* Easy to extend and maintain

---

