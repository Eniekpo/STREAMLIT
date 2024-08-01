import streamlit as st
import time as ts
from datetime import time

st.title('Timer Application')

def converter(value):
    m,s,mm=value.split(":")
    t_s=int(m)*60+int(s)+int(mm)/1000
    return t_s

val=st.time_input('Set Timer', value=time(0, 0, 0))
if str(val) == "00:00:00":
    st.write('Please set timer')
else:
    sec=converter(str(val))
    bar=st.progress(0)
    per=sec/100
    progress_status=st.empty()
    for i in range(100):
        bar.progress(i+1)
        progress_status.write(str(i+1) + " %")
        ts.sleep(per)
    