import pandas as pd
import numpy as np
import matplotlib.pyplot as ptl
import streamlit as st
import plotly.graph_objects as go



dfCOVIDp2A= pd.read_csv(r'C:\Alicia\Data Science 02\Trabajo individual\Semana 2\respuesta2.csv')

fig = go.Figure(
    data=[go.Bar(
        x= dfCOVIDp2A['Fecha'],
        y=dfCOVIDp2A['Camas'])],
    layout_title_text="Ocupación de camas en el Estado de Nueva York durante la cuarentena"
)
fig.show()