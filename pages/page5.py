import streamlit as st

st.title("税込み＆税抜き計算アプリ")
st.write("消費税の計算をします")

if "price" not in st.session_state:
    st.session_state.price=0
if "y" not in st.session_state:
    st.session_state.y=0
if "w" not in st.session_state:
    st.session_state.w=0

st.session_state.price=st.number_input("値段を入力してください（円）",format="%d")
z=st.radio(
    "数値を税込みにするか税抜きにするか選んでください",
    ["税込み","税抜き"]
)
x=st.radio(
    "消費税の％を選んでください",
    ["10％","8％","その他"]
)
st.write("補足：消費税が8％になるものは飲食料品（※酒類(アルコール分1%以上)・外食などを除く）と、新聞（定期購読契約のもの）です")
if x=="その他":
    st.session_state.y=st.number_input("その他の場合はここに税率を入力(％)",format="%d")



col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("計算する"):
        if z=="税込み":
            if x=="10％":
                st.session_state.w = st.session_state.price*1.1
            elif x=="8％":
                st.session_state.w = st.session_state.price*1.08
            elif x=="その他":
                st.session_state.w = st.session_state.price*(1 + st.session_state.y / 100)
        elif z=="税抜き":
            if x=="10％":
                st.session_state.w = st.session_state.price/1.1
            elif x=="8％":
                st.session_state.w = st.session_state.price/1.08
            elif x=="その他":
                st.session_state.w = st.session_state.price/(1 + st.session_state.y / 100)

st.write("---------------------------------------------------------------------------------")
col1,col2,col3=st.columns([1,2,1])
with col2:
    st.write("計算結果")
st.write("  ")
if z=="税込み":
    st.write(f"税抜き価格　　　{st.session_state.price}")
    st.write(f"消費税　　　　　{st.session_state.w-st.session_state.price}")
    st.write("---------------------------------------------------------------------------------")
    st.write(f"税込み価格　　　{st.session_state.w}")
elif z=="税抜き":
    st.write(f"税込み価格　　　{st.session_state.price}")
    st.write(f"消費税　　　　　{st.session_state.price-st.session_state.w}")
    st.write("---------------------------------------------------------------------------------")
    st.write(f"税抜き価格　　　{st.session_state.w}")