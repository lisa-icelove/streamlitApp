import streamlit as st

st.title("電卓計算アプリ")

# 初期状態
if "input_mode" not in st.session_state:
    st.session_state.input_mode = False

if "value" not in st.session_state:
    st.session_state.value = None

# ① 「数値を入力」ボタン
if st.button("数値を入力"):
    st.session_state.input_mode = True

# ② ボタンを押した後に入力欄を表示
if st.session_state.input_mode:
    number = st.number_input(
        "数値を入力してください",
        min_value=0,
        value=0
    )

    # ③ 「完了」ボタン
    if st.button("完了"):
        st.session_state.value = number
        st.session_state.input_mode = False

# ④ 完了後
if st.session_state.value is not None:
    new_variable = st.session_state.value * 2

    st.write("入力した値:", st.session_state.value)
    st.write("新しい変数:", new_variable