import streamlit as st
import requests

def search(keyword, category):
    base_url = "https://swapi.dev/api/"
    url = f"{base_url}{category}/?search={keyword}"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()['results']
        return results
    else:
        return []

def display_results(results):
    for result in results:
        name = result['name']
        st.write(f"Nom : {name}")
        for key, value in result.items():
            if key != "name":
                st.write(f"{key.capitalize()} : {value}")
        st.write("---")
