import os
import streamlit as st
import google.generativeai as genai
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
genai.configure(api_key='AIzaSyDBv0ZZzaaKrk_SRkw8oz4pjW04mvyOOB4')
model = genai.list_models()
for model in model:
    print(model)
llm = GoogleGenerativeAI (model="gemini-2.5-flash",
                          google_api_key='AIzaSyDBv0ZZzaaKrk_SRkw8oz4pjW04mvyOOB4',
                          temperature=0.3)
nutritional_info_template =PromptTemplate(
    input_variables=["food_items"],
    template="""provide detailed nutritional informations for the following food items: {food_items}.
    include macronutrients (protein, fat, carbohydrates), micronutrients (vitamins, minarals), and calorie content."""
)
def get_food_items_input():
    with st.form("food_items_input_form"):
        food_items = st.text_area("Enter Food Items (separate by commas):","")
        submitted = st.form_submit_button("Get Nutritional Information")
        if submitted:
            return {"food_items": food_items}
def get_nutritional_info_response(input_data):
    if input_data is None:
        return "Error: no food items provided."
    prompt = nutritional_info_template.format(**input_data)
    response = llm.invoke(prompt)
    return response
st.title("NutriAI - Instant Nutritional Information")
input_data = get_food_items_input()
if input_data:
    with st.spinner("Fetching Nutritional Information..."):
        response = get_nutritional_info_response(input_data)
        st.subheader("Nutritional Information:")
        st.write(response)