import streamlit as st
import requests
import pandas as pd
import time

# Title
# Drop_down
# Electricity is cheaper
# Graph of el price vs gas

#functions

def get_today():
    current_year = time.strftime("%Y")
    current_month = time.strftime("%m")
    current_day = time.strftime("%d")
    return get_csv(current_year, current_month, current_day, current_year, current_month, current_day)

# Returns 0 if electriic tariff is cheaper, 1 if gas tariff is cheaper
def work_out_cheaper(value_inc_vat, boiler_efficiency):
    gas_price = 3.8325 / boiler_efficiency
    if value_inc_vat <= gas_price:
        return 0
    else:
        return 1


def get_csv(year, month, day, year_end, month_end, day_end):
    product_id = 'VAR-19-04-12'
    url = ('https://api.octopus.energy/v1/products/AGILE-18-02-21/electricity-tariffs/E-1R-AGILE-18-02-21-C/standard-unit-rates/?period_from=' + str(year) + '-' + str(month) + '-' + str(day) + 'T00:00Z&period_to=' + str(year_end) + '-' + str(month_end) + '-' + str(day_end) + 'T23:59Z&page_size=2500')

    r = requests.get(url)
    output_dict = r.json()
    print(output_dict)

    # Only results
    output_dict = output_dict['results'] # Uncomment if only wanting results list

    # save output_dict to csv
    df = pd.DataFrame(output_dict)

    # if dataframe is not empty
    if df.empty == False:
        #df.to_csv(str(year) + '-' + str(month) + '-' + str(day) + 'gas.csv')
        # Get value_with_vat
        df['value_inc_vat'] = df['value_inc_vat'].astype(float)
        return work_out_cheaper(df['value_inc_vat'][0], boiler_efficiency)

#Title
st.title('Green Switch')

#Drop down
label = 'How efficient is your boiler?'
options = ["Please select an option", "High efficiency boiler (>90%)", "Medium efficiency boiler (80%-90%)", "Low efficiency boiler (<20%)"]
boiler = st.selectbox(label, options)

if boiler == "High efficiency boiler (>90%)":
    boiler_efficiency = 0.95
elif boiler == "Medium efficiency boiler (80%-90%)":
    boiler_efficiency = 0.85
elif boiler == "Low efficiency boiler (<20%)":
    boiler_efficiency = 0.1

Cheap_el_message = 'Electricity is cheaper right now!'
Cheap_gas_message = 'Gas is cheaper right now!'

if boiler != "Please select an option":
    if get_today():
        Cheap_gas_message
    else:
        Cheap_el_message
        


#my_csv = pd.read_csv('electricity-data.csv')

#times = list(my_csv['datetime'])
#prices = list(my_csv['unit-price'])
#st.line_chart(times, prices)


