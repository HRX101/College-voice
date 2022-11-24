import streamlit as st
import random
from voicebot import send_message
import firebase_admin
import pyrebase
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth
from streamlit_lottie import st_lottie
import requests
st.set_page_config(page_title="BOT",page_icon=":sound:")
r = random.random()
def load_lottieur(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()


firebaseConfig = {

    "apiKey": "AIzaSyCLKBoJ0tYnYP8kpR_Q5AoKhPLknDwcb14",

    "authDomain": "college-48b1b.firebaseapp.com",

    "databaseURL": "https://college-48b1b-default-rtdb.firebaseio.com",

    "projectId": "college-48b1b",

    "storageBucket": "college-48b1b.appspot.com",

    "messagingSenderId": "476697133787",

    "appId": "1:476697133787:web:8abb558a3455d85f0382fe",

    "measurementId": "G-MK0CTWME29"

  }


firebase =pyrebase.initialize_app(firebaseConfig)

autho = firebase.auth()
dbs = firebase.database()
lottie_coding =load_lottieur("https://assets3.lottiefiles.com/packages/lf20_ofa3xwo7.json")
cred = credentials.Certificate('./voice-bot/key.json')
firebase_admin.initialize_app(cred,{'databaseURL': "https://college-48b1b-default-rtdb.firebaseio.com"},name=str(r))
ref = db.reference('question/')
val=random.randint(1,10000)
question_list=[]
answers=[]

question_answers_dictionary={}

with st.container():

    st.subheader(":loudspeaker: ")
    st.markdown("<h1 style='text-align: center; color: Black;'>Hey! I am Here for helping you </h1>", unsafe_allow_html=True)
   # st.write("You can text here to know about JIS University.")
    
    left_column, right_column =st.columns(2) 
    with left_column:  
        name_of_user=st.text_input("Enter your name")
        question = st.text_input("Raise your voice through text typing: ")
        if question!="":
            message=send_message(question)
            st.write('bot: ',message)
            ref.child(name_of_user).push().set(question)
    with right_column:
        st_lottie(lottie_coding,width=200, height=200, key="coding")
#print(message)
#question_list.append(question)
#answers.append(message)
#question_answers_dictionary["question"]=question_list
#question_answers_dictionary["answers"]=answers
