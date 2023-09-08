import streamlit as st
import duckdb
import pandas as pd
import pandasai as pdai
from timeit import default_timer as timer
import numpy as np
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode


start_timer = timer()

data = pd.read_parquet('../db/df_data_virada.parquet')
#con = duckdb.connect(database='df_repasses_final.duckdb', read_only=True)

st.set_page_config(layout="wide")

st.title('ciadosorriso - analise')

AgGrid(data)
gb = GridOptionsBuilder.from_dataframe(data)
gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
gb.configure_side_bar() #Add a sidebar
gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
gridOptions = gb.build()

grid_response = AgGrid(
    data,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=False,
    theme='blue', #Add theme color to the table
    enable_enterprise_modules=True,
    height=350, 
    width='100%',
    reload_data=True
)

data = grid_response['data']
selected = grid_response['selected_rows'] 
df = pd.DataFrame(selected) #Pass the selected rows to a new dataframe df

end_timer = timer()

st.write("Total running time: ", end_timer-start_timer, " seconds")

