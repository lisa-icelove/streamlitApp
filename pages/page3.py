import streamlit as st
st.title("単位変換アプリ")
st.write("長さ(m)")
if "moto" not in st.session_state:
    st.session_state.moto=""
if "saki" not in st.session_state:
    st.session_state.saki=""
if "number" not in st.session_state:
    st.session_state.number=0
if "tan" not in st.session_state:
    st.session_state.tan=""
tani={
    "km":1000,
    "hm":100,
    "dam":10,
    "m":1,
    "dm":0.1,
    "cm":0.01,
    "mm":0.001,
    "kg":1000,
    "hg":100,
    "dag":10,
    "g":1,
    "dg":0.1,
    "cg":0.01,
    "mg":0.001,
    "秒": 1,
    "分": 60,
    "時間": 3600,
    "日": 86400,
    "cm²": 0.0001,
    "m²": 1,
    "km²": 1_000_000,
    "mL": 0.001,
    "L": 1,
    "m³": 1000,
}
st.session_state.number=st.number_input("数値を入力してください")
col1,col2,col3,col4,col5,col6,col7=st.columns(7)
with col1:
    if st.button("km"):
        st.session_state.tan="km"
with col2:
    if st.button("hm"):
        st.session_state.tan="hm"
with col3:
    if st.button("dam"):
        st.session_state.tan="dam"
with col4:
    if st.button("m"):
        st.session_state.tan="m"
with col5:
    if st.button("dm"):
        st.session_state.tan="dm"
with col6:
    if st.button("cm"):
        st.session_state.tan="cm"
with col7:
    if st.button("mm"):
        st.session_state.tan="mm"
st.write(f"現在選択中の単位:{st.session_state.tan}")
if st.button("元となる単位を確定"):
    st.session_state.moto=st.session_state.tan
if st.button("変更する単位を確定"):
    st.session_state.saki=st.session_state.tan
if st.session_state.moto != "" and st.session_state.saki != "":
    mver = st.session_state.number * tani[st.session_state.moto]
    sber = mver / tani[st.session_state.saki]

    st.write(
        f"結果　元の単位："
        f"{st.session_state.number}{st.session_state.moto}"
        f" → {sber}{st.session_state.saki}"
    )
else:
    st.write("元の単位と変更する単位を選択してください")