import streamlit as st

st.title("電卓計算アプリ")

# 現在入力中の値
if "a" not in st.session_state:
    st.session_state.a = 0

# 保存する変数
if "number1" not in st.session_state:
    st.session_state.number1 = None

if "number2" not in st.session_state:
    st.session_state.number2 = None


# 現在の値を表示
st.write("現在の値:", st.session_state.a)


# 数値を入力
if st.button("1"):
    st.session_state.a = str(1)


# 完了
if st.button("完了"):

    if st.session_state.number1 is None:
        # 1回目の入力
        st.session_state.number1 = st.session_state.a

    elif st.session_state.number2 is None:
        # 2回目の入力
        st.session_state.number2 = st.session_state.a

    # 次の入力のために0に戻す
    st.session_state.a = 0


# 表示
if st.button("表示"):

    st.write("number1 =", st.session_state.number1)
    st.write("number2 =", st.session_state.number2)

#数値をリセット
if st.button("数値リセット"):
    st.session_state.number1=None
    st.session_state.number2=None