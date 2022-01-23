import streamlit as st

# Title
# Drop_down
# Electricity is cheaper
# Graph of el price vs gas

#Title
st.title('Green Switch')

#Drop down
label = 'Which boiler do you have?'
options = ["AFFECT-FIX-12M-22-01-21", "SUPER-GREEN-12M-22-01-21"]
t.selectbox(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False)

Cheap_el_message = 'Electricity is cheaper!'
Cheap_gas_message = 'Gas is cheaper!'

Cheap_el_message