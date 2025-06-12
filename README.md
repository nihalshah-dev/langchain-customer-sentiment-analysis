# 🛍️ LangChain Customer Sentiment Analyzer

This project uses **LangChain** and **LLMs** to extract insights from synthetic customer emails at a fictional mega retail store — **BuyBuy**.

---

## 📌 Use Case

Retail chains receive thousands of customer feedback emails. The goal is to extract structured insights from these emails using **prompt engineering** with a language model.

We aim to answer:

1. What **product category** receives the most **negative feedback**?
2. Which **store location** has the most **customer complaints**?

---

## ❓ Problem Statement

Each email may:

- Praise or criticize a product
- Mention a specific item (e.g., "blue sofa", "laptop stand")
- Include a store location

We leverage an LLM to:

- Understand sentiment from free-text
- Infer the **category** of each product (e.g., electronics, furniture, clothing)
- Aggregate and summarize insights

---

## 🧩 LLM Chain Architecture

- **Model**: `meta/llama-3.1-8b-instruct` via LangChain's NVIDIA endpoint
- **Technique**: Prompt Engineering (no manual rule-based filtering)
- **Framework**: [LangChain](https://www.langchain.com/)
- **Parser**: Pydantic + JSON output parser

---

## 🧪 How It Works

1. Load 10 customer emails from `data/emails.json`
2. Feed the entire list into the LLM with a custom prompt
3. LLM analyzes sentiment and categorizes complaints
4. Final output:

```json
   {
     "most_complained_category": "furniture",
     "most_complained_location": "Chicago"
   }
```

## ▶️ Run It

```bash
# Clone and run
git clone <this-project>
cd langchain-customer-sentiment-analysis
pip install -r requirements.txt
python app/chain.py
```

## ✅ Output Example

```json
{
  "most_complained_category": "furniture",
  "most_complained_location": "Chicago"
}
```

## 🌟 Results

✅ Successfully identifies complaints using LLM-based reasoning, not rule-based filters

✅ Categorizes natural language products into broader semantic groups

✅ Provides actionable insight to businesses on what and where to improve

## Build with

- [LangChain](https://www.langchain.com/)
- [Nvidia Inference API](https://catalog.ngc.nvidia.com/)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [JsonOutputParser](https://python.langchain.com/docs/concepts/output_parsers/)

## 🤝 Contribution

Pull requests welcome! If you’d like to extend this with a UI (e.g., Streamlit) or an API (e.g., FastAPI), feel free to fork and build on it.
