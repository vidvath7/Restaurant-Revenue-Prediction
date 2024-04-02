import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression
import datetime

model=pickle.load(open('model_rf.pkl','rb'))

st.title('Restaurant Revenue Predictor')
st.image("""https://www.tripsavvy.com/thmb/-8bRmWGUjuqgpzPxNvJMXBEMif8=/900x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/new-york-city-s-11-madison-park-named-world-s-best-restaurant-665447878-5914e2965f9b586470511aaa.jpg""")
st.header('Enter the Details here :')


def predict_revenue(month,year,years_old,city_group,restaurant_type):

    x=np.zeros(42)
    x[0]=month
    x[1]=year
    x[2]=years_old
    x[3]=city_group
    x[4]=restaurant_type

    prediction=model.predict([x])[0]
    return prediction



open_year=st.date_input('Restaurant Open Date',max_value= datetime.date(2015, 1, 25),min_value=datetime.date(1996, 1, 1),
                        value=datetime.date(2005, 1, 1))

year=open_year.year
month=open_year.month
years_old=2015-year

restuarant_type=st.selectbox('Please select the Restaurant type',['Food Court','Inline','Drive-Thru','Mobile'])


if restuarant_type=='Food Court':
    restuarant_type=1
elif restuarant_type=='Inline':
    restuarant_type=2
elif restuarant_type=='Drive-Thru':
    restuarant_type=0
elif restuarant_type=='Mobile':
    restuarant_type=3


city= st.selectbox('City ',['İstanbul', 'Ankara', 'Diyarbakır', 'Tokat', 'Gaziantep',
       'Afyonkarahisar', 'Edirne', 'Kocaeli', 'Bursa', 'İzmir', 'Sakarya',
       'Elazığ', 'Kayseri', 'Eskişehir', 'Şanlıurfa', 'Samsun', 'Adana',
       'Antalya', 'Kastamonu', 'Uşak', 'Muğla', 'Kırklareli', 'Konya',
       'Karabük', 'Tekirdağ', 'Denizli', 'Balıkesir', 'Aydın', 'Amasya',
       'Kütahya', 'Bolu', 'Trabzon', 'Isparta', 'Osmaniye'])


if (city=='İstanbul' or city=='Ankara' or city=='İzmir'):
    city_group=0
else:
    city_group=1



if st.button('Predict Revenue'):
    revenue=predict_revenue(month,year,years_old,city_group,restuarant_type)
    st.success(f'The predicted revenue for the Restaurant is : {int(revenue)}  ')

