import streamlit as st

st.title("電卓計算アプリ")

if "input_mode" not in st.session_state:
    st.session_state.input_mode = False

if "numbers" not in st.session_state:
    st.session_state.numbers = []

if "number1" not in st.session_state:
    st.session_state.number1=0

if "number2" not in st.session_state:
    st.session_state.number2=0

if "number3" not in st.session_state:
    st.session_state.number3=0

if "a" not in st.session_state:
    st.session_state.a=0

# 入力開始
if st.button("数値を入力"):
    st.session_state.input_mode = True
    st.session_state.number1=st.session_state.a

# 入力画面
if st.session_state.input_mode:

    number1 = st.session_state.number1
    number2 = st.session_state.number2
    number3 = st.session_state.number3


if st.button("完了"):
    if st.session_state.number1==st.session_state.a:
        st.session_state.number2=st.session_state.a

if st.button("1"):
    st.session_state.a+=1

if st.button("表示"):
    st.write(st.session_state.number1)
    st.write(st.session_state.number2)