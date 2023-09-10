import streamlit as st

st.title("CampusX")

col1, col2 = st.columns(2)

with col1:
    st.image("me10.jpg")

with col2:
    st.write("Campus X is an online platform")

st.header("Caurses")
st.subheader("DSMP")
st.subheader("DAMP")
st.subheader("DEMP")
st.subheader("DSA")

st.sidebar.title("Menu")
st.sidebar.markdown("""
- Home
- About
- Contact
- Career
- Login
""")

option = st.sidebar.selectbox("Select 1", ["Teacher", "Student"])
btn = st.sidebar.button("Select")

if btn:
    st.title("hello + ",option)
