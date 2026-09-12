import streamlit as st

st.title("電卓計算アプリ")

if "input_mode" not in st.session_state:
    st.session_state.input_mode = False

if "numbers" not in st.session_state:
    st.session_state.numbers = []

# 入力開始
if st.button("数値を入力"):
    st.session_state.input_mode = True

# 入力画面
if st.session_state.input_mode:

    number1 = st.number_input("数値1", key="number1")
    number2 = st.number_input("数値2", key="number2")
    number3 = st.number_input("数値3", key="number3")

    if st.button("完了"):
        st.session_state.numbers = [
            number1,
            number2,
            number3
        ]

        st.session_state.input_mode = False