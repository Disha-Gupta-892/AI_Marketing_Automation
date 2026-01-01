# 🤖 Customer Feedback Automation using Make.com + Gemini AI

An end-to-end **AI-powered customer feedback handling system** that automatically monitors incoming emails, analyzes customer sentiment and issues using Google Gemini AI, sends a professional response back to the customer, and logs everything into Google Sheets for tracking and analytics.

This workflow eliminates manual effort in customer support while ensuring fast, polite, and consistent responses at scale.

---

## 🚀 What This Automation Does

✔️ Monitors customer feedback emails in real time

✔️ Uses AI to **draft a calm, professional response**

✔️ Automatically **categorizes customer issues**

✔️ Sends the AI-generated reply back to the customer

✔️ Logs feedback + response into Google Sheets

✔️ Runs continuously with zero manual intervention

In short: **Inbox → AI Brain → Action → Record → Done.**

---

## 🧠 High-Level Workflow Architecture

1. **Gmail – Watch Emails**

   * Monitors inbox for new emails
   * Filters emails containing:

     * `customer review`
     * `customer feedback`

2. **Gemini AI – Response Generator**

   * Analyzes the email content
   * Generates a polite, concise, and customer-friendly reply
   * Addresses the customer by first name
   * Ensures the tone is calm and non-rude

3. **Gemini AI – Issue Categorization**

   * Classifies customer issues into:

     * Late Delivery
     * Poor Chat Support
     * Poor Quality of Work
     * All Good
   * Supports multiple issue tags if needed

4. **Router (Decision Node)**

   * Branch 1 → Send reply email to customer
   * Branch 2 → Log feedback and response into Google Sheets

5. **Gmail – Send Email**

   * Replies directly to the customer
   * Uses the AI-generated response
   * Maintains email thread context

6. **Google Sheets – Add Row**

   * Stores:

     * Customer email
     * Subject
     * Original feedback
     * AI-generated response
     * Issue category
   * Creates a structured feedback database

---

## 🧩 Tools & Technologies Used

| Category            | Tool                           |
| ------------------- | ------------------------------ |
| Workflow Automation | Make.com                       |
| Email Handling      | Gmail API                      |
| AI Model            | Google Gemini 2.5 Flash-Lite   |
| Data Storage        | Google Sheets                  |
| Logic Control       | Router (Conditional branching) |

---

## 📊 Data Logged in Google Sheets

| Column             | Description               |
| ------------------ | ------------------------- |
| Customer Email     | Sender’s email address    |
| Subject            | Email subject             |
| Customer Feedback  | Full email content        |
| Issue Category     | AI-detected issue type    |
| Response Generated | AI reply sent to customer |

This makes it easy to build dashboards later for:

* Issue trends
* Response quality audits
* Customer satisfaction analysis

---

## 🛠️ Setup Instructions

1. Import the **Make.com blueprint JSON** into your Make account
2. Connect the following accounts:

   * Gmail
   * Google Gemini AI
   * Google Sheets
3. Update:

   * Gmail filters (if needed)
   * Google Sheet ID
4. Turn on the scenario
5. Sit back and let automation cook 🔥

---
## Preview Of Workflow

![Image](https://github.com/Disha-Gupta-892/Workflow_Automations/blob/21d3b58575549517d2dd21435bea7a382b456671/Automated_Customer_Feedback_Platform/Automated_Customer_Feedback_Platform.png)

---
## 🧪 Example Use Cases

* SaaS customer support automation
* Freelancers handling client feedback
* Small businesses without a support team
* Startups scaling customer communication
* AI-first customer experience systems

---

## 🔒 Reliability & Safety

* No destructive actions
* Read-only email monitoring
* AI responses are controlled via prompt constraints
* Logs everything for transparency

---

## 📈 Future Enhancements (Ideas)

* Sentiment scoring (Positive / Neutral / Negative)
* Slack / Teams alerts for critical issues
* CRM integration (HubSpot / Zoho)
* Auto-priority tagging for urgent complaints
* Dashboard using Looker Studio / Power BI

---

## 👤 Author

**Disha Gupta**

AI Automation Engineer

Focused on building scalable, AI-driven business workflows

---
