import streamlit as st
import random
from voicebot import send_message

val=random.randint(1,10000)
title = st.text_input("raise your voice through text typing: ")
if title!="":
    st.write('bot: ',send_message(title))
print(send_message(title))