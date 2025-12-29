# 🤖 AI-Powered GitHub Pull Request Review Automation (n8n + LLM)

An end-to-end **AI-driven code review automation** that automatically reviews GitHub pull requests, generates structured senior-developer feedback using an LLM, posts the review as a PR comment, and optionally labels the PR — all in real time.

This workflow removes manual review overhead while maintaining **consistent, opinionated, and high-quality code reviews** at scale.

---

## 🚀 What This Automation Does

✔️ Triggers automatically on **GitHub pull request events**

✔️ Fetches **file-level diffs** from the PR using GitHub API

✔️ Converts raw diffs into a **structured review prompt**

✔️ Uses an **AI Code Review Agent** to analyze changes

✔️ Posts **review comments directly on the PR**

✔️ Optionally adds a **“Reviewed by AI / Senior Developer” label**

In short:
**Pull Request → AI Reviewer → GitHub Comment → Label → Done.**

---

## 🧠 High-Level Workflow Architecture

1. **GitHub – Pull Request Trigger**

   * Listens for pull request events on a repository
   * Initiates the workflow in real time

2. **GitHub API – Fetch PR Diffs**

   * Retrieves:

     * List of modified files
     * Unified diffs (`patch`)
   * Dynamically constructed using PR metadata

3. **Prompt Builder (Code Node)**

   * Parses file-level diffs
   * Formats each diff with filename context
   * Builds a structured natural-language instruction for the AI
   * Example instruction:

     > *“You are a senior developer. Please review the following code changes…”*

4. **AI Code Review Agent**

   * Uses an LLM to:

     * Analyze code changes
     * Identify issues and improvements
     * Suggest best practices
   * Produces concise, point-wise review feedback

5. **GitHub Comment Poster**

   * Posts the AI-generated review directly on the pull request
   * Maintains PR discussion context

6. **PR Labeler (Optional)**

   * Automatically applies a label such as:

     * `ReviewedByAI`
     * `ReviewedBySeniorDeveloper`

---

## 🧩 Tools & Technologies Used

| Category            | Tool / Platform        |
| ------------------- | ---------------------- |
| Workflow Automation | n8n                    |
| Version Control     | GitHub                 |
| AI Model            | OpenAI / LLM           |
| API Integration     | GitHub REST API        |
| Logic Processing    | JavaScript (Code Node) |
| Review Automation   | GitHub Reviews API     |

---

## 📊 AI Review Behavior

The AI agent is instructed to:

* Review changes **file by file**
* Focus on **logic, readability, and best practices**
* Ignore files without diffs
* Avoid repeating code snippets
* Provide **direct, actionable feedback**
* Write reviews like a **senior engineer**

This ensures feedback is:

* Useful
* Non-spammy
* Production-oriented

---

## 🛠️ Setup Instructions

1. Import the **n8n workflow JSON** into your n8n instance
2. Connect credentials:

   * GitHub OAuth
   * OpenAI / LLM provider
3. Configure:

   * Repository name
   * Allowed PR events
   * Label name (optional)
4. Activate the workflow
5. Open a pull request and watch the AI review it automatically 🚀

---

## 🧪 Example Use Cases

* Automated code reviews for small teams
* Startup repositories without dedicated reviewers
* Enforcing consistent coding standards
* Reducing PR review turnaround time
* AI-assisted mentoring for junior developers

---

## 🔒 Reliability & Safety

* Read-only access to PR diffs
* No direct code modification
* OAuth-secured GitHub access
* Reviews are transparent and auditable
* Human reviewers remain in control

---

## 📈 Future Enhancements (Ideas)

* Inline review comments per line
* Language-specific reviewers (Python, JS, Java, etc.)
* Integration with Google Sheets for coding standards
* Severity tagging (Critical / Warning / Suggestion)
* Slack / Teams notifications for PR reviews
* Review quality scoring dashboard

---

## 👤 Author

**Disha Gupta**

AI Automation Engineer

Focused on building **agentic AI workflows**, developer productivity tools, and scalable automation systems.

---
