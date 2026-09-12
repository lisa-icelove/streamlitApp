import streamlit as st

# ============================================================
# CSS（見た目）
# ============================================================

st.markdown("""
<style>

    /* 全体 */
    .block-container {
        max-width: 500px;
        padding-top: 2rem;
    }

    /* タイトル */
    h1 {
        text-align: center;
        margin-bottom: 25px;
    }

    /* 計算式表示 */
    .display {
        background-color: #222;
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: right;
        font-size: 28px;
        margin-bottom: 10px;
        min-height: 45px;
    }

    /* 現在入力中 */
    .input-display {
        background-color: #f0f2f6;
        color: #222;
        padding: 12px 20px;
        border-radius: 10px;
        text-align: right;
        font-size: 20px;
        margin-bottom: 20px;
    }

    /* ボタン */
    div.stButton > button {
        width: 100%;
        height: 55px;
        border-radius: 10px;
        font-size: 20px;
        font-weight: bold;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# 変数
# ============================================================

if "number1" not in st.session_state:
    st.session_state.number1 = None

if "number2" not in st.session_state:
    st.session_state.number2 = None

if "a" not in st.session_state:
    st.session_state.a = ""

if "q" not in st.session_state:
    st.session_state.q = ""

if "k" not in st.session_state:
    st.session_state.k=""


# ============================================================
# タイトル
# ============================================================

st.title("🧮 電卓")


# ============================================================
# 現在の状態を表示
# ============================================================

st.markdown(
    f"""
    <div class="display">
        {st.session_state.number1 if st.session_state.number1 is not None else ""}
        {st.session_state.q}
        {st.session_state.number2 if st.session_state.number2 is not None else ""}
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="input-display">
        {st.session_state.a if st.session_state.a != "" else "0"}
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# 数字・演算子
# ============================================================

# 7 8 9 ÷
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("7", use_container_width=True):
        st.session_state.a = f"{st.session_state.a}{str(7)}"
        if st.session_state.number1 != None and st.session_state.number2 != "None":
            st.session_state.number2 = "None"

with col2:
    if st.button("8", use_container_width=True):
        st.session_state.a = f"{st.session_state.a}{str(8)}"
        if st.session_state.number1 != None and st.session_state.number2 != "None":
            st.session_state.number2 = "None"

with col3:
    if st.button("9", use_container_width=True):
        st.session_state.a = f"{st.session_state.a}{str(9)}"
        if st.session_state.number1 != None and st.session_state.number2 != "None":
            st.session_state.number2 = "None"

with col4:
    if st.button("÷", use_container_width=True):
        st.session_state.q = "/"


# 4 5 6 ×
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("4", use_container_width=True):
        st.session_state.a = f"{st.session_state.a}{str(4)}"
        if st.session_state.number1 != None and st.session_state.number2 != "None":
            st.session_state.number2 = "None"

with col2:
    if st.button("5", use_container_width=True):
        st.session_state.a = f"{st.session_state.a}{str(5)}"
        if st.session_state.number1 != None and st.session_state.number2 != "None":
            st.session_state.number2 = "None"

with col3:
    if st.button("6", use_container_width=True):
        st.session_state.a = f"{st.session_state.a}{str(6)}"
        if st.session_state.number1 != None and st.session_state.number2 != "None":
            st.session_state.number2 = "None"

with col4:
    if st.button("×", use_container_width=True):
        st.session_state.q = "*"


# 1 2 3 -
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("1", use_container_width=True):
        st.session_state.a = f"{st.session_state.a}{str(1)}"
        if st.session_state.number1 != None and st.session_state.number2 != "None":
            st.session_state.number2 = "None"

with col2:
    if st.button("2", use_container_width=True):
        st.session_state.a = f"{st.session_state.a}{str(2)}"
        if st.session_state.number1 != None and st.session_state.number2 != "None":
            st.session_state.number2 = "None"

with col3:
    if st.button("3", use_container_width=True):
        st.session_state.a = f"{st.session_state.a}{str(3)}"
        if st.session_state.number1 != None and st.session_state.number2 != "None":
            st.session_state.number2 = "None"

with col4:
    if st.button("-", use_container_width=True):
        st.session_state.q = "-"


# 0 ＋
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("0", use_container_width=True):
        st.session_state.a = f"{st.session_state.a}{str(0)}"
        if st.session_state.number1 != None and st.session_state.number2 != "None":
            st.session_state.number2 = "None"

with col4:
    if st.button("+", use_container_width=True):
        st.session_state.q = "+"


# ============================================================
# 符号変更
# ============================================================

st.divider()

col1, col2 = st.columns(2)

with col1:
    if st.button("±  マイナス", use_container_width=True):
        st.session_state.a = st.session_state.a.replace("+", "")
        st.session_state.a = "-" + st.session_state.a

with col2:
    if st.button("±  プラス", use_container_width=True):
        st.session_state.a = st.session_state.a.replace("-", "")
        st.session_state.a = "+" + st.session_state.a


# ============================================================
# 計算・完了・リセット
# ============================================================

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("✓ 完了", use_container_width=True):

        if st.session_state.number1 == None:
            st.session_state.number1 = st.session_state.a

        elif st.session_state.number2 == "None":
            st.session_state.number2 = st.session_state.a

        st.session_state.a = ""


with col2:
    if st.button("＝ 計算", use_container_width=True):

        if st.session_state.q == "+":
            st.session_state.k=int(st.session_state.number1)+ int(st.session_state.number2)
            st.write(st.session_state.k)

        elif st.session_state.q == "-":
            st.session_state.k=int(st.session_state.number1)- int(st.session_state.number2)
            st.write(st.session_state.k)

        elif st.session_state.q == "*":
            st.session_state.k=int(st.session_state.number1)* int(st.session_state.number2)
            st.write(st.session_state.k)

        elif st.session_state.q == "/":
            st.session_state.k=int(st.session_state.number1) / int(st.session_state.number2)
            st.write(st.session_state.k)


with col3:
    if st.button("🗑 リセット", use_container_width=True):

        st.session_state.number1 = None
        st.session_state.number2 = None
        st.session_state.a = ""
        st.session_state.q = ""
        st.session_state.k = None


# ============================================================
# デバッグ用表示
# ============================================================

with st.expander("現在の変数を確認"):

    st.write("number1 =", st.session_state.number1)
    st.write("q =", st.session_state.q)
    st.write("number2 =", st.session_state.number2)
    st.write("a =", st.session_state.a)
    st.write("k =", st.session_state.k)