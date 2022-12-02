import pickle
import streamlit as st

model= pickle.load(open('rf.pkl','rb'))

def main():
    st.title('Prediksi Keslamatan Pasien Gagal Jantung')

    #input variables
    age = st.text_input('age')
    anaemia = st.text_input('anaemia')
    creatinine_phosphokinase = st.text_input('creatinine_phosphokinase')
    diabetes = st.text_input('diabetes')
    ejection_fraction = st.text_input('ejection_fraction')
    high_blood_pressure = st.text_input('high_blood_pressure')
    platelets = st.text_input('platelets')
    serum_creatinine = st.text_input('serum_creatinine')
    serum_sodium = st.text_input('serum_sodium')
    sex = st.text_input('sex')
    smoking = st.text_input('smoking')
    time = st.text_input('time')

    #prediction code
    if st.button('Predict'):
        makeprediction = model.predict([[age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking, time]])
        output=makeprediction[0]
        st.success('Pasien Tidak Selamat/Meninggal')

if __name__=='__main__':
    main()