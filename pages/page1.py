import streamlit as st

#変数
if "number1" not in st.session_state:
    st.session_state.number1=None

if "number2" not in st.session_state:
    st.session_state.number2=None

if "a" not in st.session_state:
    st.session_state.a=0

if "q" not in st.session_state:
    st.session_state.q=0
#入力
if st.button("1"):
    st.session_state.a=f"{st.session_state.a}{str(1)}"

if st.button("+"):
    st.session_state.q="+"
#計算
if st.button("計算"):
    if st.session_state.q=="+":
        st.write(int(st.session_state.number1) + int(st.session_state.number2))
#表示
st.write(f"現在入力中の値：{st.session_state.a}")
st.write(f"現在の計算：{st.session_state.number1}{st.session_state.q}{st.session_state.number2}")

#変数切り替え
if st.button("完了"):
    if st.session_state.number1==None:
        st.session_state.number1=st.session_state.a
    elif st.session_state.number2==None:
        st.session_state.number2=st.session_state.a
    st.session_state.a=0