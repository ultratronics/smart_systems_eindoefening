import streamlit as st
st.markdown("## Contractor day-rate calculator")
st.text("""This calculator is based on a blog post by Jonathan Sedar.
https://sedar.co/posts/on-contractor-day-rates/""")

currency = st.radio('currency',('$', '£', '€'))
salary = st.slider('Salary',min_value=35000, max_value=300000, value=90000, step=2500)
st.write("Desired yearly salary:", currency,salary)
days_off = st.slider('days off, including weekends, sick days and holidays',min_value=1, max_value=365, value=140, step=1)
work_days =365-days_off
