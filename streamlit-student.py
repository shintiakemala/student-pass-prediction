import pickle
import streamlit as st

# load save model
student_model = pickle.load(open('student_model.sav', 'rb'))

# Judul Untuk Web
st.title('Prediksi Lulus atau Tidaknya Nilai Siswa')
st.text('Nama : Shintia Kemala Dewi')
st.text('Nim : 191351208')
st.text('Matkul : Business Intelligence')
st.text('Keterangan : Untuk Inputan 0 = Nilai siswa tidak lulus')
st.text('Apabila inputan 1 = Nilai siswa lulus')

#membagi kolom
col1, col2, col3 = st.columns(3)

with col1:
    school = st.text_input ('Input nilai School')

with col2:
    sex = st.text_input ('Input nilai Sex')

with col3:
    age = st.text_input ('Input nilai Age')

with col1:
    address = st.text_input('Input nilai Address')

with col2:
    famsize = st.text_input('Input nilai Fam Size')

with col3:
    Pstatus = st.text_input('Input nilai Free Pstatus')

with col1:
    Medu = st.text_input('Input nilai Total Medu')

with col2:
    Fedu = st.text_input('Input nilai Fedu')

with col3:
    traveltime = st.text_input('Input nilai Travel Time')

with col1:
    studytime = st.text_input('Input nilai Study Time')

with col2:
    failures = st.text_input('Input nilai Failures')

with col3:
    schoolsup = st.text_input('Input nilai School Sup')

with col1:
    famsup = st.text_input('Input nilai Fam Sup')

with col2:
    paid = st.text_input('Input nilai School Paid')

with col3:
    activities = st.text_input('Input nilai Activities')

with col1:
    nursery = st.text_input('Input nilai Nursery')

with col2:
    higher = st.text_input('Input nilai Higher')

with col3:
    internet = st.text_input('Input nilai Internet')

with col1:
    romantic = st.text_input('Input nilai Romantic')

with col2:
    famrel = st.text_input('Input nilai Famrel')

with col3:
    freetime = st.text_input('Input nilai FreeTime')

with col1:
    goout = st.text_input('Input nilai GoOut')

with col2:
    Dalc = st.text_input('Input nilai Dalc')

with col3:
    Walc = st.text_input('Input nilai Walc')

with col1:
    health = st.text_input('Input nilai Health')

with col2:
    absences = st.text_input('Input nilai Absences')

with col3:
    G1 = st.text_input('Input nilai G1')

with col1:
    G2 = st.text_input('Input nilai G2')

with col2:
    G3 = st.text_input('Input nilai G3')


#code untuk prediksi
student_pass = ''

#membuat tombol prediksi
if st.button('Test Prediksi Lulus Atau Tidaknya Nilai Siswa') :
    student_prediction = student_model.predict([[school, sex, age, address, famsize, Pstatus, Medu, Fedu, traveltime, studytime, failures, schoolsup, famsup, paid, activities, nursery, higher, internet, romantic, famrel, freetime, goout, Dalc, Walc, health, absences, G1, G2, G3]])

    if(student_prediction[0]==1):
        student_pass = 'Nilai Siswa Lulus'
    else :
        student_pass = 'Nilai Siswa Tidak Lulus'

    st.success(student_pass)