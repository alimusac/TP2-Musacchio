import pandas as pd
import numpy as np
import matplotlib.pyplot as ptl
import streamlit as st
import plotly.graph_objects as go

st.title('La pandemia en Estados Unidos')

st.write('Por María Alicia Musacchio')

st.write('La pandemia fue un antes y un después a nivel mundial. Veamos los datos sobre los cinco estados con mayor ocupación hospitalaria por COVID en Estados Unidos')

repo_path = "C:\Alicia\Data Science 02\Trabajo individual\Semana 2"

st.image('respuesta1.jpg')

st.write('Ahora nos vamos a enfocar en el estado con mayor cantidad de casos, Nueva York, durante su cuarentena que fue desde el 22 de marzo de 2020 hasta el 13 de junio de 2020')

dfCOVIDp2A= pd.read_csv(r'C:\Alicia\Data Science 02\Trabajo individual\Semana 2\respuesta2.csv')

fig = go.Figure(
    data=[go.Bar(
        x= dfCOVIDp2A['Fecha'],
        y=dfCOVIDp2A['CamasCovid'])],
    layout_title_text="Ocupación de camas por COVID en el Estado de Nueva York durante la cuarentena")
fig.show()

st.image('respuesta2-1.jpg')

st.write('Pareciera que después del estallido inicial, los casos fueron bajando. Sin embargo, como se puede ver en esta segunda imágen, el sistema sanitario siguió saturado incluso cuando bajaron los casos de Covid')


fig = go.Figure(
    data=[go.Bar(
        x= dfCOVIDp2A['Fecha'],
        y=dfCOVIDp2A['Camas'])],
    layout_title_text="Ocupación de camas en el Estado de Nueva York durante la cuarentena"
)
fig.show()

st.image('respuesta2-2.jpg')

st.write('Volviendo a Estado Unidos en su totalidad, comparando algunas variables podemos encontrar similitudes')

st.image('variables.jpg')

st.write('Veamos estos cinco estados en un mapa sobre cantidad de camas ocupadas con casos de Covid')

mapa = pd.read_csv(r'C:\Alicia\Data Science 02\Trabajo individual\Semana 2\mapa.csv')

import chart_studio.plotly as py
import plotly.offline as po
import plotly.graph_objs as pg
import matplotlib.pyplot as plt
po.init_notebook_mode(connected = True)

data = dict(type = 'choropleth', 
 locations = ['AK','AL','AR','AS','AZ','CA','CO','CT','DC','DE','FL','GA','HI','IA','ID','IL','IN','KS','KY','LA','MA','MD','ME',
 'MI','MN','MO','MS','MT','NC','ND','NE','NH','NJ','NM','NV','NY','OH','OK','OR', 'PA','PR','RI', 'SC','SD','TN','TX','UT','VA',
'VI','VT','WA','WI','WV','WY'], 
 locationmode = 'USA-states', 
 z = mapa['Camas de hospitalización usadas por casos de Covid'], 
 text = ['Alaska','Alabama', 'Arizona','Samoa Estadounidense', 'Arkansas','California', 'Colorado','Connecticut','Washington DC',
 'Delaware','Florida','Georgia','Hawái','Iowa','Idaho', 'Illinois','Indiana','Kansas','Kentucky','Luisiana','Massachusetts',
 'Maryland','Maine','Míchigan','Minnesota','Misuri','Misisipi', 'Montana','Carolina del Norte','Dakota del Norte','Nebraska',
 'Nuevo Hampshire','Nueva Jersey','Nuevo México', 'Nevada','Nueva York', 'Ohio', 'Oklahoma','Oregón', 'Pensilvania','Puerto Rico',
 'Rhode Island','Carolina del Sur','Dakota del Sur', 'Tennessee','Texas','Utah','Virginia', 'Islas Virgenes', 
 'Vermont','Washington', 'Wisconsin', 'Virginia Occidental','Wyoming'])

layout = dict(geo = {'scope':'usa'})

x = pg.Figure(data = [data] ,
layout = layout)
po.iplot(x)

st.image('mapa1.jpg')

st.write('Comparemos ese mapa con este que indica la cantidad de población en el 2020')

df= pd.read_csv(r'C:\Alicia\Data Science 02\Trabajo individual\Semana 2\poblacion.csv')
poblacion = pd.DataFrame.from_records(df)
data = dict(type = 'choropleth', 
 locations = ['AK','AL','AR','AS','AZ','CA','CO','CT','DC','DE','FL','GA','HI','IA','ID','IL','IN','KS','KY','LA','MA','MD','ME',
 'MI','MN','MO','MS','MT','NC','ND','NE','NH','NJ','NM','NV','NY','OH','OK','OR', 'PA','PR','RI', 'SC','SD','TN','TX','UT','VA',
'VI','VT','WA','WI','WV','WY'], 
 locationmode = 'USA-states', 
 z = poblacion['Cantidad de habitantes'], 
 text = ['Alaska','Alabama', 'Arizona','Samoa Estadounidense', 'Arkansas','California', 'Colorado','Connecticut','Washington DC',
 'Delaware','Florida','Georgia','Hawái','Iowa','Idaho', 'Illinois','Indiana','Kansas','Kentucky','Luisiana','Massachusetts',
 'Maryland','Maine','Míchigan','Minnesota','Misuri','Misisipi', 'Montana','Carolina del Norte','Dakota del Norte','Nebraska',
 'Nuevo Hampshire','Nueva Jersey','Nuevo México', 'Nevada','Nueva York', 'Ohio', 'Oklahoma','Oregón', 'Pensilvania','Puerto Rico',
 'Rhode Island','Carolina del Sur','Dakota del Sur', 'Tennessee','Texas','Utah','Virginia', 'Islas Virgenes', 
 'Vermont','Washington', 'Wisconsin', 'Virginia Occidental','Wyoming'])

layout = dict(geo = {'scope':'usa'})

x = pg.Figure(data = [data] ,
layout = layout)
po.iplot(x)

st.image('mapa2.jpg')

st.write('Claro, que esta relación entre cantidad personas y contagios se puede entender ya que como una simple cuestión estadística(a más personas, más cantidad de contagiados). Pero también se puede interpretar que la acumulación de personas ya sea para transportarse, hacer las compras, entre otros factores, que implica la vida en las grandes urbes favorece el contagio.')

st.title('Propuesta')

st.write('Una recomendación que excede al CDC(centro de control y prevención de enfermedades) sería descongestionar los grandes centros urbanos. Incentivar la vida en ciudades más pequeñas, el trabajo remoto, darle facilidades a las familias para que decidan realizar un cambio de vida en este sentido e incluso incentivarlo con propagandas oficiales')

st.write('Pero antes, y es prioritario que el CDC se vea involucrado, es necesario que veamos como reforzar todo el sistema de salud y especialmente en estos lugares alejados o con menos habitantes. Miremos el gráfico sobre los estados con mayor porcentaje de utilización de camas UCI por casos de Covid')

st.image('respuesta5.jpg')

st.write('Esta tabla claramente habla de la saturación del sistema de salud, pero no por explosión de casos sino por falta de infraestructura. Es entendible que ante una menor población haya menos infraestructura. Sin embargo, estamos hablando de estados como Alabama que tienen 5.024.279 y solo cuentan con 1.801 camas de terapia intensiva o  Montana que tiene una población de 1.084.225 y sólo tiene 345 camas de terapia intensiva. Ni hablar de Florida (que es uno de los cuatro que aparece en las variables) que tiene una población de 21.538.187 y sólo cuentan con 8.810 camas UCI.')

st.write('Y quiero volver a una idea que vimos al principio de porqué es necesario reforzar el sistema de salud más allá del covid.')

st.write('Estos son los casos de Covid en Estados Unidos desde el 01 de enero de 2020 hasta julio de 2022')

dfCOVIDp8AA= pd.read_csv(r'C:\Alicia\Data Science 02\Trabajo individual\Semana 2\respuesta8.csv')


fig = go.Figure(
    data=[go.Bar(
        x= dfCOVIDp8AA['Fecha'],
        y=dfCOVIDp8AA['CamasCovid'])],
    layout_title_text="Ocupación de camas por Covid"
)
fig.show()

st.image('respuesta8.jpg')

st.write('Hay altas y bajas, picos en enero que coincide con las época invernal, pero luego bajaban. Sin embargo, miremos el gráfico de la ocupación general de camas en los hospitales.')


fig = go.Figure(
    data=[go.Bar(
        x= dfCOVIDp8AA['Fecha'],
        y=dfCOVIDp8AA['Camas'])],
    layout_title_text="Ocupación de camas"
)
fig.show()

st.image('respuesta9.jpg')

st.write('La saturación del sistema de salud continua, ya sea por secuelas de Covid, enfermedades no atendidas, enfermedades previas que empeoraron por falta de atención, cuadros depresivos o de ansiedad que se vieron agravados por la pandemia. Y estos aspectos son algunos, además es necesario tener en cuenta el desgaste que implicó la pandemia para los médicos y enfermeros.')

st.write('Resumiendo, es necesario incentivar un cambio de vida alejado de los grandes centros urbanos para, ante una futura pandemia, disminuir su propagación. Pero además, reforzar el sistema de salud y tener en cuenta que cuando el sistema de salud colapsa no es sólo por la pandemia sino por todos los derivados que implican en la salud de las personas y también deben ser atendidos por el sistema de salud.')