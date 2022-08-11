import pandas as pd
import numpy as np
import matplotlib.pyplot as ptl
import streamlit as st
import plotly.graph_objects as go


import chart_studio.plotly as py
import plotly.offline as po
import plotly.graph_objs as pg
import matplotlib.pyplot as plt
po.init_notebook_mode(connected = True)


dfCOVIDp8AA= pd.read_csv(r'C:\Alicia\Data Science 02\Trabajo individual\Semana 2\respuesta8.csv')


fig = go.Figure(
    data=[go.Bar(
        x= dfCOVIDp8AA['Fecha'],
        y=dfCOVIDp8AA['Camas'])],
    layout_title_text="Ocupación de camas"
)
fig.show()

