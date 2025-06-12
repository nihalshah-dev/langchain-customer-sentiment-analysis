# 🧠 LangChain-Powered Customer Sentiment Analyzer

A LangChain project that leverages LLMs to analyze customer emails from a fictional mega retail brand — **BuyBuy** — and determine:

- 📦 Which **product category** has the most negative sentiment
- 🏪 Which **store location** receives the most complaints

---

## 🚀 Use Case

Retail businesses receive tons of unstructured feedback via customer emails. Manually analyzing and classifying these is time-consuming and error-prone. We use **LLMs + prompt engineering** to automate:

- Sentiment analysis
- Product category classification
- Complaint frequency detection
- Insight extraction from natural language

---

## ❓ Problem Statement

> Given 10 synthetic customer emails from BuyBuy stores:
>
> - Identify negative sentiment emails
> - Map the product mentioned to a broader category (e.g., "shirt" → "clothing")
> - Track which store location is most often associated with complaints
>
> Then, return:
> ```json
> {
>   "most_complained_category": "...",
>   "most_complained_location": "..."
> }
> ```

---

## 🧩 LLM Chain Architecture

- **Model**: `meta/llama-3.1-8b-instruct` via LangChain's NVIDIA endpoint
- **Technique**: Prompt Engineering (no manual rule-based filtering)
- **Framework**: [LangChain](https://www.langchain.com/)
- **Parser**: Pydantic + JSON output parser

---

## ✅ Output Example

```json
{
  "most_complained_category": "furniture",
  "most_complained_location": "Chicago"
}
