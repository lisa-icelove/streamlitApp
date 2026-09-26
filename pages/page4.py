import streamlit as st

# =========================
# ページ設定
# =========================
st.set_page_config(
    page_title="単位変換アプリ",
    page_icon="🔄",
    layout="centered"
)

# =========================
# CSS
# =========================
st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #2563eb;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #6b7280;
    margin-bottom: 30px;
}

.category {
    font-size: 20px;
    font-weight: bold;
    color: #1f2937;
    margin-top: 20px;
    margin-bottom: 10px;
}

.selected {
    background-color: #eff6ff;
    border: 2px solid #3b82f6;
    border-radius: 12px;
    padding: 12px;
    text-align: center;
    font-size: 18px;
    font-weight: bold;
    color: #2563eb;
    margin: 15px 0;
}

.result-box {
    background: linear-gradient(135deg, #2563eb, #60a5fa);
    color: white;
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    margin-top: 25px;
    box-shadow: 0 5px 15px rgba(37, 99, 235, 0.2);
}

.result-title {
    font-size: 16px;
    opacity: 0.9;
}

.result {
    font-size: 30px;
    font-weight: bold;
    margin-top: 10px;
}

.info-box {
    background-color: #f3f4f6;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    color: #4b5563;
    margin-top: 15px;
}

</style>
""", unsafe_allow_html=True)


# =========================
# タイトル
# =========================
st.markdown(
    '<div class="title">🔄 単位変換アプリ</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">好きな単位を選んで、かんたんに変換できます</div>',
    unsafe_allow_html=True
)


# =========================
# session_state
# =========================
if "moto" not in st.session_state:
    st.session_state.moto = ""

if "saki" not in st.session_state:
    st.session_state.saki = ""

if "number" not in st.session_state:
    st.session_state.number = 0

if "tan" not in st.session_state:
    st.session_state.tan = ""


# =========================
# 単位
# =========================
tani = {
    "km": 1000,
    "hm": 100,
    "dam": 10,
    "m": 1,
    "dm": 0.1,
    "cm": 0.01,
    "mm": 0.001,

    "kg": 1000,
    "hg": 100,
    "dag": 10,
    "g": 1,
    "dg": 0.1,
    "cg": 0.01,
    "mg": 0.001,

    "秒": 1,
    "分": 60,
    "時間": 3600,
    "日": 86400,

    "cm²": 0.0001,
    "m²": 1,
    "km²": 1_000_000,

    "cm³": 0.000001,
    "m³": 1,
    "km³": 1_000_000_000,
}


# =========================
# 数値入力
# =========================
st.session_state.number = st.number_input(
    "🔢 変換する数値",
    value=st.session_state.number
)


# =========================
# 長さ
# =========================
st.markdown(
    '<div class="category">📏 長さ（m）</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

with col1:
    if st.button("km", use_container_width=True):
        st.session_state.tan = "km"

with col2:
    if st.button("hm", use_container_width=True):
        st.session_state.tan = "hm"

with col3:
    if st.button("dam", use_container_width=True):
        st.session_state.tan = "dam"

with col4:
    if st.button("m", use_container_width=True):
        st.session_state.tan = "m"

with col5:
    if st.button("dm", use_container_width=True):
        st.session_state.tan = "dm"

with col6:
    if st.button("cm", use_container_width=True):
        st.session_state.tan = "cm"

with col7:
    if st.button("mm", use_container_width=True):
        st.session_state.tan = "mm"


# =========================
# 重さ
# =========================
st.markdown(
    '<div class="category">⚖️ 重さ（g）</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

with col1:
    if st.button("kg", use_container_width=True):
        st.session_state.tan = "kg"

with col2:
    if st.button("hg", use_container_width=True):
        st.session_state.tan = "hg"

with col3:
    if st.button("dag", use_container_width=True):
        st.session_state.tan = "dag"

with col4:
    if st.button("g", use_container_width=True):
        st.session_state.tan = "g"

with col5:
    if st.button("dg", use_container_width=True):
        st.session_state.tan = "dg"

with col6:
    if st.button("cg", use_container_width=True):
        st.session_state.tan = "cg"

with col7:
    if st.button("mg", use_container_width=True):
        st.session_state.tan = "mg"


# =========================
# 時間
# =========================
st.markdown(
    '<div class="category">⏰ 時間（秒）</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("秒", use_container_width=True):
        st.session_state.tan = "秒"

with col2:
    if st.button("分", use_container_width=True):
        st.session_state.tan = "分"

with col3:
    if st.button("時間", use_container_width=True):
        st.session_state.tan = "時間"

with col4:
    if st.button("日", use_container_width=True):
        st.session_state.tan = "日"


# =========================
# 面積
# =========================
st.markdown(
    '<div class="category">⬜ 面積（m²）</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("cm²", use_container_width=True):
        st.session_state.tan = "cm²"

with col2:
    if st.button("m²", use_container_width=True):
        st.session_state.tan = "m²"

with col3:
    if st.button("km²", use_container_width=True):
        st.session_state.tan = "km²"


# =========================
# 体積
# =========================
st.markdown(
    '<div class="category">🧊 体積</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("mL", use_container_width=True):
        st.session_state.tan = "mL"

with col2:
    if st.button("L", use_container_width=True):
        st.session_state.tan = "L"

with col3:
    if st.button("m³", use_container_width=True):
        st.session_state.tan = "m³"


# =========================
# 現在選択中
# =========================
st.markdown(
    f'''
    <div class="selected">
        現在選択中の単位： {st.session_state.tan if st.session_state.tan else "未選択"}
    </div>
    ''',
    unsafe_allow_html=True
)


# =========================
# 元の単位・変更先を確定
# =========================
col1, col2 = st.columns(2)

with col1:
    if st.button("⬅️ 元となる単位を確定", use_container_width=True):
        st.session_state.moto = st.session_state.tan

with col2:
    if st.button("➡️ 変更する単位を確定", use_container_width=True):
        st.session_state.saki = st.session_state.tan


# =========================
# 現在の設定
# =========================
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "元の単位",
        st.session_state.moto if st.session_state.moto else "未設定"
    )

with col2:
    st.metric(
        "変更先の単位",
        st.session_state.saki if st.session_state.saki else "未設定"
    )


# =========================
# 計算
# =========================
if st.session_state.moto != "" and st.session_state.saki != "":

    mver = (
        st.session_state.number
        * tani[st.session_state.moto]
    )

    sber = (
        mver
        / tani[st.session_state.saki]
    )

    st.markdown(
        f'''
        <div class="result-box">
            <div class="result-title">✨ 変換結果</div>
            <div class="result">
                {st.session_state.number}{st.session_state.moto}
                →
                {sber:g}{st.session_state.saki}
            </div>
        </div>
        ''',
        unsafe_allow_html=True
    )

else:

    st.markdown(
        '''
        <div class="info-box">
            👆 元の単位と変更する単位を選択してください
        </div>
        ''',
        unsafe_allow_html=True
    )
import streamlit as st

# =========================
# ページ設定
# =========================
st.set_page_config(
    page_title="単位変換アプリ",
    page_icon="🔄",
    layout="centered"
)

# =========================
# CSS
# =========================
st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #2563eb;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #6b7280;
    margin-bottom: 30px;
}

.category {
    font-size: 20px;
    font-weight: bold;
    color: #1f2937;
    margin-top: 20px;
    margin-bottom: 10px;
}

.selected {
    background-color: #eff6ff;
    border: 2px solid #3b82f6;
    border-radius: 12px;
    padding: 12px;
    text-align: center;
    font-size: 18px;
    font-weight: bold;
    color: #2563eb;
    margin: 15px 0;
}

.result-box {
    background: linear-gradient(135deg, #2563eb, #60a5fa);
    color: white;
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    margin-top: 25px;
    box-shadow: 0 5px 15px rgba(37, 99, 235, 0.2);
}

.result-title {
    font-size: 16px;
    opacity: 0.9;
}

.result {
    font-size: 30px;
    font-weight: bold;
    margin-top: 10px;
}

.info-box {
    background-color: #f3f4f6;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    color: #4b5563;
    margin-top: 15px;
}

</style>
""", unsafe_allow_html=True)


# =========================
# タイトル
# =========================
st.markdown(
    '<div class="title">🔄 単位変換アプリ</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">好きな単位を選んで、かんたんに変換できます</div>',
    unsafe_allow_html=True
)


# =========================
# session_state
# =========================
if "moto" not in st.session_state:
    st.session_state.moto = ""

if "saki" not in st.session_state:
    st.session_state.saki = ""

if "number" not in st.session_state:
    st.session_state.number = 0

if "tan" not in st.session_state:
    st.session_state.tan = ""


# =========================
# 単位
# =========================
tani = {
    "km": 1000,
    "hm": 100,
    "dam": 10,
    "m": 1,
    "dm": 0.1,
    "cm": 0.01,
    "mm": 0.001,

    "kg": 1000,
    "hg": 100,
    "dag": 10,
    "g": 1,
    "dg": 0.1,
    "cg": 0.01,
    "mg": 0.001,

    "秒": 1,
    "分": 60,
    "時間": 3600,
    "日": 86400,

    "cm²": 0.0001,
    "m²": 1,
    "km²": 1_000_000,

    "cm³": 0.000001,
    "m³": 1,
    "km³": 1_000_000_000,
}


# =========================
# 数値入力
# =========================
st.session_state.number = st.number_input(
    "🔢 変換する数値",
    value=st.session_state.number
)


# =========================
# 長さ
# =========================
st.markdown(
    '<div class="category">📏 長さ（m）</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

with col1:
    if st.button("km", use_container_width=True):
        st.session_state.tan = "km"

with col2:
    if st.button("hm", use_container_width=True):
        st.session_state.tan = "hm"

with col3:
    if st.button("dam", use_container_width=True):
        st.session_state.tan = "dam"

with col4:
    if st.button("m", use_container_width=True):
        st.session_state.tan = "m"

with col5:
    if st.button("dm", use_container_width=True):
        st.session_state.tan = "dm"

with col6:
    if st.button("cm", use_container_width=True):
        st.session_state.tan = "cm"

with col7:
    if st.button("mm", use_container_width=True):
        st.session_state.tan = "mm"


# =========================
# 重さ
# =========================
st.markdown(
    '<div class="category">⚖️ 重さ（g）</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

with col1:
    if st.button("kg", use_container_width=True):
        st.session_state.tan = "kg"

with col2:
    if st.button("hg", use_container_width=True):
        st.session_state.tan = "hg"

with col3:
    if st.button("dag", use_container_width=True):
        st.session_state.tan = "dag"

with col4:
    if st.button("g", use_container_width=True):
        st.session_state.tan = "g"

with col5:
    if st.button("dg", use_container_width=True):
        st.session_state.tan = "dg"

with col6:
    if st.button("cg", use_container_width=True):
        st.session_state.tan = "cg"

with col7:
    if st.button("mg", use_container_width=True):
        st.session_state.tan = "mg"


# =========================
# 時間
# =========================
st.markdown(
    '<div class="category">⏰ 時間（秒）</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("秒", use_container_width=True):
        st.session_state.tan = "秒"

with col2:
    if st.button("分", use_container_width=True):
        st.session_state.tan = "分"

with col3:
    if st.button("時間", use_container_width=True):
        st.session_state.tan = "時間"

with col4:
    if st.button("日", use_container_width=True):
        st.session_state.tan = "日"


# =========================
# 面積
# =========================
st.markdown(
    '<div class="category">⬜ 面積（m²）</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("cm²", use_container_width=True):
        st.session_state.tan = "cm²"

with col2:
    if st.button("m²", use_container_width=True):
        st.session_state.tan = "m²"

with col3:
    if st.button("km²", use_container_width=True):
        st.session_state.tan = "km²"


# =========================
# 体積
# =========================
st.markdown(
    '<div class="category">🧊 体積(m³)</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("cm³", use_container_width=True):
        st.session_state.tan = "cm³"

with col2:
    if st.button("m³", use_container_width=True):
        st.session_state.tan = "m³"

with col3:
    if st.button("km³", use_container_width=True):
        st.session_state.tan = "km³"


# =========================
# 現在選択中
# =========================
st.markdown(
    f'''
    <div class="selected">
        現在選択中の単位： {st.session_state.tan if st.session_state.tan else "未選択"}
    </div>
    ''',
    unsafe_allow_html=True
)


# =========================
# 元の単位・変更先を確定
# =========================
col1, col2 = st.columns(2)

with col1:
    if st.button("⬅️ 元となる単位を確定", use_container_width=True):
        st.session_state.moto = st.session_state.tan

with col2:
    if st.button("➡️ 変更する単位を確定", use_container_width=True):
        st.session_state.saki = st.session_state.tan


# =========================
# 現在の設定
# =========================
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "元の単位",
        st.session_state.moto if st.session_state.moto else "未設定"
    )

with col2:
    st.metric(
        "変更先の単位",
        st.session_state.saki if st.session_state.saki else "未設定"
    )


# =========================
# 計算
# =========================
if st.session_state.moto != "" and st.session_state.saki != "":

    mver = (
        st.session_state.number
        * tani[st.session_state.moto]
    )

    sber = (
        mver
        / tani[st.session_state.saki]
    )

    st.markdown(
        f'''
        <div class="result-box">
            <div class="result-title">✨ 変換結果</div>
            <div class="result">
                {st.session_state.number}{st.session_state.moto}
                →
                {sber:g}{st.session_state.saki}
            </div>
        </div>
        ''',
        unsafe_allow_html=True
    )

else:

    st.markdown(
        '''
        <div class="info-box">
            👆 元の単位と変更する単位を選択してください
        </div>
        ''',
        unsafe_allow_html=True
    )
