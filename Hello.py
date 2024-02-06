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

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    #intro==================================================================
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("### Selamat data pada aplikasi kami 👋")

    st.markdown(
        """
        berikut adalah aplikasi yang dapat digunakan .....
        
    """
    )
    #intro==================================================================

    #input==================================================================
    name = st.text_input('Siapa Nama Anda?')

    #age--------------------------------------------------------------------
    age = st.number_input('Berapakah Usia Anda? (dalam tahun)', min_value=0)
    #age--------------------------------------------------------------------

    #sex--------------------------------------------------------------------
    sex = st.radio(
        "Jenis Kelamin",
        key="visibility",
        options=["Laki-Laki", "Perempuan"],
    )
    #sex--------------------------------------------------------------------

    #cp---------------------------------------------------------------------
    #Chest Pain = nyeri dada
    cp = st.slider('Berapakah skala nyeri dada anda?', 0, 3)
    #cp---------------------------------------------------------------------

    #trestbps---------------------------------------------------------------
    #Resting blood pressure = tekanan darah saat istirahat
    trestbps = st.number_input('Berapakah tekanan darah anda saat istirahat?', min_value=0)
    #trestbps---------------------------------------------------------------

    #chol--------------------------------------------------------------------
    #Chol = serum kolesterol
    chol = st.number_input('Berapakah serum kolesterol anda?', min_value=0)
    #chol--------------------------------------------------------------------

    #fbs---------------------------------------------------------------------
    #Fbs = fasting blood sugar atau gula darah puasa
    fbs = st.number_input('Berapakah fasting blood sugar atau gula darah puasa anda?', min_value=0)
    #fbs---------------------------------------------------------------------

    #restecg-----------------------------------------------------------------
    #Restecg = rekam jantung (ekg) 
    restecg = st.number_input('rekam jantung (ekg)  anda?', min_value=0)
    #restecg-----------------------------------------------------------------

    #thalach-----------------------------------------------------------------
    #Thalach = maksimum denyut jantung
    thalach = st.number_input('Berapakah maksimum denyut jantung anda?', min_value=0)
    #thalach-----------------------------------------------------------------

    #exang-------------------------------------------------------------------
    #Exang = nyeri dada karena aktivitas fisik
    exang = st.number_input('Berapakah nyeri dada karena aktivitas fisik anda?', min_value=0)
    #exang-------------------------------------------------------------------

    #oldpeak-----------------------------------------------------------------
    #Oldpeak = st depresi karena aktivitas fisik
    oldpeak = st.number_input('Berapakah depresi karena aktivitas fisik anda?', min_value=0)
    #oldpeak-----------------------------------------------------------------

    #input==================================================================

if __name__ == "__main__":
    run()
