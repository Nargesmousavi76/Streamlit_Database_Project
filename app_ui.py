import streamlit as st

import app_db

st.title("STREAMLIT DATABASE UI")

option = st.sidebar.selectbox('Select Your Option: ',
                    ('SELECT ALL RECORDS',
                     'SELECT RECORD BY ID',
                     'SELECT RECORD BY TITLE',
                     'SELECT RECORD BY IMDB_RATE',
                     'INSERT RECORD',
                     'DELETE RECORD BY ID',
                     'DELETE RECORD BY TITLE',
                     'UPDATE RECORD BY ID',
                     'UPDATE RECORD BY TITLE'))

if option == 'SELECT ALL RECORDS':
    if st.button("SHOW DATA"):
        result = app_db.select_all_records()
        st.write(result)

if option == 'SELECT RECORD BY ID':
    #user = st.slider("Enter ID : ", 1, 9)
    user = st.number_input("Enter ID: ", min_value=1, max_value=9)
    st.write(f"ID is : {user}")
    if st.button("SHOW DATA"):
        result = app_db.select_record_by_id(user)
        st.write(result)


if option == 'SELECT RECORD BY TITLE':
    user = st.text_input("Enter title:")
    if st.button("SHOW DATA"):
        result = app_db.select_record_by_title(user)
        st.write(result)
    

if option =='SELECT RECORD BY IMDB_RATE':
    user = st.number_input("Enter IMDB_RATE: ",min_value=1.0, max_value=10.0 ,step=0.1)
    st.write(f"IMDB_RATE is : {user}")
    if st.button("SHOW DATA"):
        result = app_db.select_record_by_imdb_rate(user)
        st.write(result)

if option =='INSERT RECORD':
    title = st.text_input("Enter title:")
    year = st.text_input("Enter year:")
    country = st.text_input("Enter country:")
    imdb_rate = st.number_input("Enter IMDB_RATE: ",min_value=1.0, max_value=10.0 ,step=0.1)
    
    if st.button("Save"):
        result = app_db.insert_record(title,year,country,imdb_rate)
        st.success("Record is success add")
        

if option == 'DELETE RECORD BY ID':
    user = st.number_input("Enter ID: ", min_value=1, max_value=100)
    st.write(f"ID is : {user}")
    if st.button("DELET"):
        result = app_db.delete_record_by_id(user)
        st.success("Delet is success")

if option == 'DELETE RECORD BY TITLE':
    user = st.text_input("Enter Title: ")
    st.write(f"Title is : {user}")
    if st.button("DELET"):
        result = app_db.delete_record_by_title(user)
        st.success("Delet is success")
    

if option == 'UPDATE RECORD BY ID': 
    user = st.number_input("Enter ID: ", min_value=1, max_value=100)
    st.write(f"ID is : {user}")
    year = st.text_input("Enter year:")
    imdb_rate = st.number_input("Enter IMDB_RATE: ",min_value=1.0, max_value=10.0 ,step=0.1)
    if st.button("UPDATE") :
        result = app_db.update_record_by_id(user,year,imdb_rate)
        st.success("Update is success")

if option == 'UPDATE RECORD BY TITLE':
    user = st.text_input("Enter Title: ")
    st.write(f"Title is : {user}")
    year = st.text_input("Enter year: ")
    country = st.text_input("Enter Country: ")
    imdb_rate = st.number_input("Enter IMDB_RATE: ",min_value=1.0, max_value=10.0 ,step=0.1)
    if st.button("UPDATE"):
        result = app_db.update_record_by_title(user,year,country,imdb_rate)
        st.success("Update is success")