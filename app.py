import streamlit as st
import json
import os
from openai import OpenAI
from dotenv import load_dotenv
from prompts import get_recipes_prompt, get_bonus_recipes_prompt

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def call_groq(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=4000
        )
        raw = response.choices[0].message.content.strip()
        raw = raw.replace("```json", "").replace("```", "").strip()
        return json.loads(raw)
    except json.JSONDecodeError:
        st.error("Something went wrong parsing the response. Try again.")
        return None
    except Exception as e:
        st.error(f"API error: {e}")
        return None


st.set_page_config(page_title="Cookable.", page_icon="🍳")
st.title("🍳 Cookable.")
st.write("Your fridge, your ingredients, curated recipes for you.")
st.divider()

st.markdown("### What's in your fridge?")
ingredients = st.text_area(
    label="Ingredients",
    placeholder="e.g. eggs, carrot, cheese, onion...",
    height=100,
    label_visibility="collapsed"
)

col1, col2, col3 = st.columns(3)
with col1:
    cuisine = st.selectbox("Cuisine", ["Any", "Indian", "Italian", "Chinese", "Mexican", "Mediterranean"])
with col2:
    time = st.selectbox("Time available", ["No limit", "Under 15 mins", "30 mins", "1 hour"])
with col3:
    dietary = st.multiselect("Dietary restrictions", ["Vegetarian", "Vegan", "No dairy", "Gluten free"], placeholder="Select...")

col4, col5 = st.columns(2)
with col4:
    meal_type = st.selectbox("Meal type", ["Any", "Breakfast", "Lunch", "Dinner", "Snack", "Dessert"])
with col5:
    servings = st.selectbox("Servings", ["1 person", "2 people", "4 people", "6 people"])

if st.button("🍳 Generate Recipes"):
    if not ingredients.strip():
        st.warning("Please enter at least one ingredient.")
    else:
        with st.spinner("Finding recipes for you..."):
            prompt = get_recipes_prompt(ingredients, cuisine, time, dietary, meal_type, servings)
            result = call_groq(prompt)
        if result:
            st.session_state["result"] = result

if "result" in st.session_state and st.session_state["result"] is not None:
    result = st.session_state["result"]
    recipes = result.get("recipes", [])
    get_these = result.get("get_these", [])

    st.divider()
    st.markdown("### 5 recipes you can make right now")
    for recipe in recipes:
        with st.expander(f"{recipe['name']} -- {recipe['prep_time']} -- {recipe['difficulty']}"):
            st.markdown("**Ingredients used:**")
            st.write(", ".join(recipe["ingredients_used"]))
            st.markdown("**Steps:**")
            for i, step in enumerate(recipe["steps"], 1):
                st.write(f"{i}. {step}")

    st.divider()
    st.markdown("### 🛒 Get these to unlock more meals")
    for item in get_these:
        st.write(f"**{item['ingredient']}** -- {item['reason']}")