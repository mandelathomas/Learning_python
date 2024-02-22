import pandas as pd
import numpy as np
from matplotlib import pyplot as plt 

import pyodbc 



#establishing the connection
e_connection = pyodbc.connect('DRIVER=FreeTDS;PORT=1433;'
'SERVER=DESKTOP-5TE7V5C\SQLEXPRESS;'
'DATABASE=ATSMAS_Exchange;'
'TDS_Version=8.0;'
'Trust_conn=yes;')


conn = pyodbc.connect(e_connection) 

cursor = pyodbc.connect.cursor
query = "select * from stocks "
cursor.execute(query)


cursor.close()
conn.close()