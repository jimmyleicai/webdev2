# This creates the page for displaying data visualizations.
# It should read data from both 'data.csv' and 'data.json' to create graphs.

import streamlit as st
import pandas as pd
import json # The 'json' module is needed to work with JSON files.
import os   # The 'os' module helps with file system operations.

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visualizations",
    page_icon="📈",
)

# PAGE TITLE AND INFORMATION
st.title("Data Visualizations 📈")
st.write("This page displays graphs based on the collected data.")


# DATA LOADING
# A crucial step is to load the data from the files.
# It's important to add error handling to prevent the app from crashing if a file is empty or missing.

st.divider()
st.header("Load Data")

# TO DO:
# 1. Load the data from 'data.csv' into a pandas DataFrame.
#    - Use a 'try-except' block or 'os.path.exists' to handle cases where the file doesn't exist.
try:
    csv_dataframe = pd.read_csv('data.csv')  
    csv_dataframe['Number of Items'] = pd.to_numeric(csv_dataframe['Number of Items'], errors='coerce')
    st.write(csv_dataframe)
    st.success("CSV data loaded successfully.")

except FileNotFoundError:
    st.info("Your CSV file was not found.")
    csv_dataframe = pd.DataFrame()
    
# 2. Load the data from 'data.json' into a Python dictionary.

try:
    with open('data.json', 'r') as dj:
        newdict = json.load(dj)
        data_points = newdict.get('data_points', [])
        json_dataframe = pd.DataFrame(data_points)
        json_dataframe['value'] = pd.to_numeric(json_dataframe['value'], errors='coerce')
        st.success("JSON data loaded successfully.")

except FileNotFoundError:
    st.info("Your JSON file was not found.")
    json_dataframe = pd.DataFrame()

#    - Use a 'try-except' block here as well.




# GRAPH CREATION
# The lab requires you to create 3 graphs: one static and two dynamic.
# You must use both the CSV and JSON data sources at least once.

st.divider()
st.header("📈Graphs")

# GRAPH 1: STATIC GRAPH
st.subheader("🛒Grocery Statistics") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
# TO DO:
# - Create a static graph (e.g., bar chart, line chart) using st.bar_chart() or st.line_chart().
# - Use data from either the CSV or JSON file.
# - Write a description explaining what the graph shows.

try:
    data_points = newdict.get('data_points', [])
    chart_title = newdict.get('chart_title', 'JSON Data Bar Chart')
    pDataFrame = pd.DataFrame(data_points)
    indexed = pDataFrame.set_index('item')    
    st.bar_chart(indexed)       #NEW
    st.write('''The bar graph shown above graphs the type of item on the x-axis to the number of that item in the y-axis.
                ***The data shown here is from the JSON file.***''')

except:
    st.warning("Sorry. Your CSV file either doesn't exist or is empty.")



# GRAPH 2: DYNAMIC GRAPH
st.subheader("Interactive Line Graph👨‍💻") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
# TODO:
# - Create a dynamic graph that changes based on user input.
# - Use at least one interactive widget (e.g., st.slider, st.selectbox, st.multiselect).
# - Use Streamlit's Session State (st.session_state) to manage the interaction.
# - Add a '#NEW' comment next to at least 3 new Streamlit functions you use in this lab.
# - Write a description explaining the graph and how to interact with it.

try:

    if 'fewest_items' not in st.session_state:  #NEW
        st.session_state['fewest_items'] = 0

    largest_num = csv_dataframe['Number of Items'].max()

    chosen_min = st.slider("Use this slider to select the minimum number of items to display in the graph:",    #NEW
                           min_value = 0,
                           max_value = int(largest_num),
                           value=st.session_state['fewest_items'])

    st.session_state['fewest_items'] = chosen_min

    filtered_dataframe = csv_dataframe[csv_dataframe['Number of Items'] >= st.session_state['fewest_items']]

    st.line_chart(filtered_dataframe.set_index('Grocery Item')['Number of Items'])  #NEW

    st.write('''This interative chart graphs a line that connects the name of each grocery item to their quantity.
             By using the slider to select a number, you can filter out items that have a quantity fewer
             than the minimum threshold number. ***The data shown here is from the CSV file.***''')

except:
    
    st.warning("Sorry. Your CSV file either doesn't exist or is empty.")

# GRAPH 3: DYNAMIC GRAPH
st.subheader("Dynamic Scatterplot🎯") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
# TO DO:
# - Create another dynamic graph.
# - If you used CSV data for Graph 1 & 2, you MUST use JSON data here (or vice-versa).
# - This graph must also be interactive and use Session State.
# - Remember to add a description and use '#NEW' comments.

try:
    
    all_items = json_dataframe['item'].tolist()

    if 'chosen_items' not in st.session_state:
        st.session_state['chosen_items'] = all_items

    chosen_items_list = st.multiselect('Select which grocery items you want the graph to display:',     #NEW
                                       options = all_items,
                                       default = st.session_state['chosen_items'],
                                       )

    st.session_state['chosen_items'] = chosen_items_list

    filtered_json_dataframe = json_dataframe[json_dataframe['item'].isin(st.session_state['chosen_items'])]

    st.scatter_chart(filtered_json_dataframe, x='item', y='value', size=None)

    st.write('''This is a scatterplot graph connecting the name of each grocery item to their respective quantities.
                The multi-select box allows you to choose which items you want displayed in the scatterplot. All grocery items
                in the JSON file are selected by default, so just delete/remove the ones that you don't want displayed.
                ***The data shown here is from the JSON file.***''')

except:
    
    st.warning("Sorry. Your JSON file either doesn't exist or is empty.")
        
        
