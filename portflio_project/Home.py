import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png",width=500)

with col2:
    st.title("Ardit Sulae")
    content = """
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
    """
    st.info(content)

st.write("below you can find some of the app i have build in python, feel free to contact me,below you can find some of the app i have build in python, feel free to contact me")

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f'images/{row['image']}')
        st.write(f"[source code]({row["url"]})")

with col4:
    for index,row in df[11:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f'images/{row['image']}')
