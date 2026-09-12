import streamlit as st

#変数
if "number1" not in st.session_state:
    st.session_state.number1=None

if "number2" not in st.session_state:
    st.session_state.number2=None

if "a" not in st.session_state:
    st.session_state.a=""

if "q" not in st.session_state:
    st.session_state.q=""
#入力

#----------------------------------------------------------------
if st.button("1"):
    st.session_state.a=f"{st.session_state.a}{str(1)}"
    if st.session_state.number1 != None and st.session_state.number2 != "None":
        st.session_state.number2="None"

#----------------------------------------------------------------
if st.button("2"):
    st.session_state.a=f"{st.session_state.a}{str(2)}"
    if st.session_state.number1 != None and st.session_state.number2 != "None":
        st.session_state.number2="None"

#----------------------------------------------------------------
if st.button("3"):
    st.session_state.a=f"{st.session_state.a}{str(3)}"
    if st.session_state.number1 != None and st.session_state.number2 != "None":
        st.session_state.number2="None"

#----------------------------------------------------------------
if st.button("4"):
    st.session_state.a=f"{st.session_state.a}{str(4)}"
    if st.session_state.number1 != None and st.session_state.number2 != "None":
        st.session_state.number2="None"

#----------------------------------------------------------------
if st.button("5"):
    st.session_state.a=f"{st.session_state.a}{str(5)}"
    if st.session_state.number1 != None and st.session_state.number2 != "None":
        st.session_state.number2="None"

#----------------------------------------------------------------
if st.button("6"):
    st.session_state.a=f"{st.session_state.a}{str(6)}"
    if st.session_state.number1 != None and st.session_state.number2 != "None":
        st.session_state.number2="None"

#----------------------------------------------------------------
if st.button("7"):
    st.session_state.a=f"{st.session_state.a}{str(7)}"
    if st.session_state.number1 != None and st.session_state.number2 != "None":
        st.session_state.number2="None"

#----------------------------------------------------------------
if st.button("8"):
    st.session_state.a=f"{st.session_state.a}{str(8)}"
    if st.session_state.number1 != None and st.session_state.number2 != "None":
        st.session_state.number2="None"

#----------------------------------------------------------------
if st.button("9"):
    st.session_state.a=f"{st.session_state.a}{str(9)}"
    if st.session_state.number1 != None and st.session_state.number2 != "None":
        st.session_state.number2="None"

#----------------------------------------------------------------
if st.button("0"):
    st.session_state.a=f"{st.session_state.a}{str(0)}"
    if st.session_state.number1 != None and st.session_state.number2 != "None":
        st.session_state.number2="None"

if st.button("+"):
    st.session_state.q="+"

if st.button("-"):
    st.session_state.q="-"

if st.button("符号を - に変更"):
    st.session_state.a="-" + st.session_state.a

if st.button("符号を + に変更"):
    st.session_state.a="+" + st.session_state.a
#計算
if st.button("計算"):
    if st.session_state.q=="+":
        st.write(int(st.session_state.number1) + int(st.session_state.number2))
    elif st.session_state.q=="-":
        st.write(int(st.session_state.number1) - int(st.session_state.number2))
#表示
st.write(f"現在入力中の値：{st.session_state.a}")
st.write(f"現在の計算：{st.session_state.number1}{st.session_state.q}{st.session_state.number2}")

#変数切り替え
if st.button("完了"):
    if st.session_state.number1==None:
        st.session_state.number1=st.session_state.a
    elif st.session_state.number2=="None":
        st.session_state.number2=st.session_state.a
    st.session_state.a=""