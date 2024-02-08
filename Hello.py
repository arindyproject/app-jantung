# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time
import streamlit as st
from streamlit.logger import get_logger
import pandas as pd
from joblib import  load
import numpy as np

from sklearn.preprocessing import StandardScaler

LOGGER = get_logger(__name__)

scaler=load('std_scaler.bin')
model = load('model.joblib') 


def run():
    #data==================================================================
    data = {
        'name' : ['nama'],
        'age': [0],      
        'sex': [0],         
        'cp' : [0],        
        'trestbps': [0],   
        'chol'    : [0],   
        'fbs'     : [0],      
        'thalach' : [0],   
        'exang'   : [0],    
    }
    #data==================================================================

    #intro==================================================================
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.header("Selamat data pada aplikasi kami 👋", divider='rainbow')

    st.markdown(
        """
        berikut adalah aplikasi yang dapat digunakan .....
        
    """
    )
    #intro==================================================================

    #input==================================================================

    name = st.text_input('Siapa Nama Anda?')
    data['name'] = [name]

    #age--------------------------------------------------------------------
    age = st.number_input('Berapakah Usia Anda? (dalam tahun)', min_value=0)
    data['age'] = [age]
    #age--------------------------------------------------------------------

    #sex--------------------------------------------------------------------
    sex_options = {"Laki-Laki": 1, "Perempuan": 0}
    sex = st.radio(
        "Jenis Kelamin",
        key="sex",
        options=list(sex_options.keys()),
    )
    sex_val     = sex_options[sex]
    data['sex'] = [sex_val]
    st.write("You selected: ", sex, ' : ', sex_val)
    #sex--------------------------------------------------------------------

    #cp---------------------------------------------------------------------
    #Chest Pain = nyeri dada
    cp_options = {
        "Nyeri dada kiri seperti tertindih atau nyeri dada kiri berat": 0, 
        "Nyeri dada kiri tidak khas": 1,
        "Nyeri dada selain di dada kiri" : 2,
        "Tidak ada keluhan" : 3
    }
    cp = st.radio(
        "Berapakah skala nyeri dada anda?",
        key="cp",
        options=list(cp_options.keys()),
    )
    cp_val      = cp_options[cp]
    data['cp']  = [cp_val]
    st.write("You selected: ", cp, ' : ', cp_val)
    #cp---------------------------------------------------------------------

    #trestbps---------------------------------------------------------------
    #Resting blood pressure = tekanan darah saat istirahat
    trestbps = st.number_input('Berapakah tekanan darah Sistol anda saat istirahat?', min_value=0)
    data['trestbps']  = [trestbps]
    st.write("You selected: ", trestbps)
    #trestbps---------------------------------------------------------------

    #chol--------------------------------------------------------------------
    #Chol = serum kolesterol
    chol = st.number_input('Berapakah serum kolesterol anda?', min_value=0)
    data['chol']  = [chol]
    #chol--------------------------------------------------------------------

    #fbs---------------------------------------------------------------------
    #Fbs = fasting blood sugar atau gula darah puasa
    fbs = st.number_input('Berapakah fasting blood sugar atau gula darah puasa anda?', min_value=0)
    fbs_val = 0
    if(fbs >= 120):
        fbs_val = 1
    data['fbs']  = [fbs_val]
    st.write("You selected: ", fbs, ' : ', fbs_val)
    #fbs---------------------------------------------------------------------

    #thalach-----------------------------------------------------------------
    #Thalach = maksimum denyut jantung
    thalach = st.number_input('Berapakah maksimum denyut jantung anda?', min_value=0)
    data['thalach']  = [thalach]
    #thalach-----------------------------------------------------------------

    #exang-------------------------------------------------------------------
    #Exang = nyeri dada karena aktivitas fisik
    exang_options = {"Ya": 1, "Tidak": 0}
    exang = st.radio(
        "Apakah aktivitas fisik menyebabkan nyeri dada kiri?",
        key="exang",
        options=list(exang_options.keys()),
    )
    exang_val = exang_options[exang]
    data['exang']  = [exang_val]
    st.write("You selected: ", exang, ' : ', exang_val)
    #exang-------------------------------------------------------------------


    #input==================================================================


    #data===================================================================
    #st.write("##### Ringkasan Data")
    df = pd.DataFrame(data)
    #st.write(df)

    columns_to_scale = ['age', 'trestbps', 'chol', 'thalach']
    df[columns_to_scale] = scaler.transform(df[columns_to_scale])
    #st.write(df)
    #data===================================================================

    #submit==================================================================
    if st.button('Prediksi'):
        if(name == ''):
            st.warning('Silahkan isi dahulu Nama anda!', icon="⚠️")
        
        if(age <= 0):
            st.warning('Silahkan isi dahulu Usia anda!', icon="⚠️")

        if(trestbps <= 0):
            st.warning('Silahkan isi dahulu tekanan darah Sistol anda saat istirahat anda!', icon="⚠️")

        if(chol <= 0):
            st.warning('Silahkan isi dahulu serum kolesterol anda!', icon="⚠️")

        if(fbs <= 0):
            st.warning('Silahkan isi dahulu fasting blood sugar atau gula darah puasa anda!', icon="⚠️")

        if(thalach <= 0):
            st.warning('Silahkan isi dahulu maksimum denyut jantung anda!', icon="⚠️")

        #Peroses Predisksi=================================================
        if((name != '') and (age > 0) and (trestbps > 0) and (chol > 0) and (fbs > 0) and (thalach > 0) ):
            progress_text = "Memulai Prediksi. Please wait...."
            my_bar = st.progress(0, text=progress_text)

            for percent_complete in range(100):
                time.sleep(0.001)
                my_bar.progress(percent_complete + 1, text=progress_text)
            time.sleep(1)
            my_bar.empty()

            #mulai prediksi
            #--------------------------------------------------------------
            hasil = model.predict( df.drop(['name'], axis=1) )
            if(hasil[0]):
                st.success('Risiko anda menderita sakit jantung rendah!!, tetap jaga pola hidup yang sehat' , icon="😀")
            else:
                st.error( 'Risiko anda menderita sakit jantung tinggi!!, segera konsultasikan ke Dokter terdekat', icon="💪")
            #--------------------------------------------------------------
        #Peroses Predisksi=================================================
            
    #submit==================================================================

if __name__ == "__main__":
    run()
