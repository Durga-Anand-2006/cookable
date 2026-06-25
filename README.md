# 🍳 Cookable.
"Your Fridge, Your Ingredients, Curated Recipes for You."

An AI powered recipe assistant that takes the ingredients you already have and turns them into real, detailed meal ideas instantly. Built as part of the Decoding Data Science 8-Day AI Application Building Challenge.

---

## 📌 About the Project

Cookable solves a problem everyone faces -- standing in front of a full fridge with no idea what to cook and ending up ordering food anyway. You enter your ingredients, set your preferences, and Cookable suggests 5 real recipes you can make right now. It also recommends ingredients to buy that unlock even more meals, with bonus recipes generated when you pick them up.

---

## ✨ Key Features

- AI generated recipes from whatever ingredients you have
- Filters for cuisine, time available, meal type, serving size, and dietary restrictions
- Smart ingredient recommendations with reasons to buy them
- Bonus recipes generated when you select new ingredients you picked up
- One click history to reload any past search instantly
- Clean earthy green and cream UI built entirely with custom CSS in Streamlit

---

## 🛠️ Tech Stack

**Frontend:** Streamlit, Custom CSS  
**Backend:** Python  
**AI Model:** LLaMA 3.3 70B via Groq API  
**Libraries:** openai, python-dotenv  

---

## 🚀 How to Run

1. Clone the repo
   ```bash
   git clone https://github.com/Durga-Anand-2006/cookable.git
   cd cookable
   ```

2. Create and activate a virtual environment
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add your Groq API key
   ```
   GROQ_API_KEY=your_key_here
   ```

5. Run the app
   ```bash
   streamlit run app.py
   ```

---

## 📁 Project Structure

```
cookable/
├── app.py              # Main Streamlit app
├── prompts.py          # Prompt templates for the Groq API
├── requirements.txt    # Dependencies
├── test_api.py         # API connection test script
├── hero.jpg            # Hero image for the UI
├── .env                # API key (not tracked)
├── .gitignore
└── README.md
```

---

## ⚠️ Notes

- Groq free tier has a daily token limit. If you hit it, wait a few hours or use a different API key.
- Ingredient input is capped at 500 characters with a minimum of 3 characters.
- Basic prompt injection protection is included. Inputs containing prompt-like keywords are rejected.
- API calls use a system/user message split with a silent retry on failure for resilience.
- Response latency is logged to the console on every API call.
- Streamlit Link: https://cookable-bydurgaanand.streamlit.app

---

## 🏆 Challenge Info

**Challenge:** Decoding Data Science 8-Day AI Application Building Challenge  
**Track:** Coding Path (Python)  
**Builder:** Durga Anand  
**University:** Heriot-Watt University Dubai  
