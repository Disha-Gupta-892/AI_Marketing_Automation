# 🤖 AI-Powered Telegram Personal Assistant using n8n + Gemini

An end-to-end **AI-powered personal assistant automation** that operates entirely inside Telegram.
This system understands **text and voice commands**, reasons using **Google Gemini AI**, maintains conversational memory, and autonomously interacts with **Gmail, Google Calendar, and Google Sheets** to perform real-world productivity tasks.

This workflow transforms Telegram into a **command center for emails, schedules, and data** — with zero manual effort.

---

## 🚀 What This Automation Does

✔️ Accepts **text & voice messages** from Telegram

✔️ Automatically **transcribes voice notes using Gemini AI**

✔️ Uses an **AI Agent with memory** to understand user intent

✔️ Reads & sends emails via **Gmail**

✔️ Creates & fetches events from **Google Calendar**

✔️ Retrieves structured data from **Google Sheets**

✔️ Responds back to the user in Telegram in real time

In short:
**Telegram → AI Brain → Google Workspace → Telegram.**

---

## 🧠 High-Level Workflow Architecture

1. **Telegram – Message Trigger**

   * Listens for incoming Telegram messages
   * Supports both text and voice inputs

2. **Message Processing Layer**

   * Detects message type
   * Routes voice messages to transcription flow
   * Routes text directly to AI Agent

3. **Gemini AI – Voice Transcription**

   * Converts Telegram voice notes into text
   * Feeds clean text into the AI Agent

4. **AI Agent (Gemini + Memory)**

   * Interprets user intent
   * Maintains conversational context per user
   * Decides which tool to invoke:

     * Gmail
     * Google Calendar
     * Google Sheets

5. **Tool Execution Layer**

   * Fetch unread emails
   * Send emails
   * Create calendar events
   * Retrieve events
   * Read structured data from sheets

6. **Telegram – Response Delivery**

   * Formats AI output
   * Sends results back to the user in Telegram

---

## 🧩 Tools & Technologies Used

| Category            | Tool / Platform              |
| ------------------- | ---------------------------- |
| Workflow Automation | n8n                          |
| Messaging Platform  | Telegram Bot API             |
| AI Model            | Google Gemini (Chat + Audio) |
| Email Automation    | Gmail API                    |
| Scheduling          | Google Calendar API          |
| Data Storage        | Google Sheets API            |
| AI Memory           | LangChain Memory Buffer      |

---

## 📊 Data Sources & Actions

### Gmail

* Fetch unread emails
* Send AI-generated replies
* Maintain thread context

### Google Calendar

* Create events using natural language
* Retrieve upcoming or past events

### Google Sheets

* Fetch rows from task and contact sheets
* Use Sheets as a lightweight database

---

## 🛠️ Setup Instructions

1. Import the **n8n workflow JSON** into your n8n instance
2. Connect the following credentials:

   * Telegram Bot
   * Google Gemini API
   * Gmail
   * Google Calendar
   * Google Sheets
3. Update:

   * Telegram Bot ID
   * Sheet IDs (Tasks / Contacts)
4. Activate the workflow
5. Start chatting with your AI assistant on Telegram 🚀

---

## 🧪 Example Commands

* “Read my unread emails”
* “Send an email to HR saying I’ll join Monday”
* “Create a meeting tomorrow at 10 AM”
* “What events do I have this week?”
* 🎙️ *Voice note:* “Add gym at 6 PM to my calendar”

---

## 🔒 Reliability & Safety

* OAuth-based authentication for all Google services
* User sessions isolated by Telegram user ID
* No destructive actions without explicit user intent
* All actions logged through workflow execution history

---

## 📈 Future Enhancements (Ideas)

* Confirmation step before sending emails
* Intent classification layer
* Priority tagging for emails
* Slack / WhatsApp integration
* Dashboard for usage analytics
* Multi-user role-based access

---

## 👤 Author

**Disha Gupta**

AI Automation Engineer

Focused on building **agentic AI systems**, workflow automation, and real-world AI assistants.

---

