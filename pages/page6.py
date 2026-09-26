import streamlit as st
import math as m

# ========================================
# ページ設定
# ========================================
st.set_page_config(
    page_title="税込み＆税抜き計算アプリ",
    page_icon="💰",
    layout="centered"
)


# ========================================
# CSS
# ========================================
st.markdown("""
<style>

body {
    background-color: #f5f7fb;
}

/* タイトル */
.title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #2563eb;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #6b7280;
    font-size: 16px;
    margin-bottom: 30px;
}

/* セクション */
.section-title {
    font-size: 20px;
    font-weight: bold;
    color: #1f2937;
    margin-top: 15px;
    margin-bottom: 10px;
}

/* 説明 */
.info {
    background-color: #eff6ff;
    border-left: 5px solid #3b82f6;
    padding: 12px 15px;
    border-radius: 8px;
    color: #374151;
    font-size: 14px;
    margin-top: 10px;
    margin-bottom: 20px;
}

/* 計算ボタン */
div.stButton > button {
    width: 100%;
    height: 50px;
    border-radius: 12px;
    border: none;
    background-color: #2563eb;
    color: white;
    font-size: 18px;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: #1d4ed8;
    color: white;
}

/* 結果エリア */
.result-box {
    background: linear-gradient(
        135deg,
        #2563eb,
        #60a5fa
    );
    color: white;
    padding: 25px;
    border-radius: 18px;
    margin-top: 20px;
    margin-bottom: 20px;
    box-shadow: 0 5px 15px rgba(37, 99, 235, 0.2);
}

.result-title {
    text-align: center;
    font-size: 18px;
    opacity: 0.9;
    margin-bottom: 15px;
}

.result-row {
    display: flex;
    justify-content: space-between;
    font-size: 18px;
    padding: 8px 0;
}

.result-main {
    font-size: 28px;
    font-weight: bold;
    text-align: center;
    margin-top: 10px;
}

/* 補足 */
.note {
    color: #6b7280;
    font-size: 13px;
    line-height: 1.7;
}

</style>
""", unsafe_allow_html=True)


# ========================================
# タイトル
# ========================================
st.markdown(
    '<div class="title">💰 税込み＆税抜き計算アプリ</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">消費税をかんたんに計算できます</div>',
    unsafe_allow_html=True
)


# ========================================
# session_state
# ========================================
if "price" not in st.session_state:
    st.session_state.price = 0

if "y" not in st.session_state:
    st.session_state.y = 0

if "w" not in st.session_state:
    st.session_state.w = 0

if "s" not in st.session_state:
    st.session_state.s = 0


# ========================================
# 値段
# ========================================
st.markdown(
    '<div class="section-title">💴 値段</div>',
    unsafe_allow_html=True
)

st.session_state.price = st.number_input(
    "値段を入力してください（円）",
    format="%d"
)


# ========================================
# 税込み・税抜き
# ========================================
st.markdown(
    '<div class="section-title">📊 計算方法</div>',
    unsafe_allow_html=True
)

z = st.radio(
    "数値を税込みにするか税抜きにするか選んでください",
    ["税込み", "税抜き"],
    horizontal=True
)


# ========================================
# 税率
# ========================================
st.markdown(
    '<div class="section-title">📈 消費税率</div>',
    unsafe_allow_html=True
)

x = st.radio(
    "消費税の％を選んでください",
    ["10％", "8％", "その他"],
    horizontal=True
)

st.markdown(
    """
    <div class="info">
    💡 <b>補足</b><br>
    消費税が8％になるものは飲食料品
    （※酒類・外食などを除く）と、
    新聞（定期購読契約のもの）です。
    </div>
    """,
    unsafe_allow_html=True
)


# ========================================
# その他の税率
# ========================================
if x == "その他":

    st.session_state.y = st.number_input(
        "その他の場合はここに税率を入力（％）",
        format="%d"
    )


# ========================================
# 端数処理
# ========================================
st.markdown(
    '<div class="section-title">🔢 端数処理</div>',
    unsafe_allow_html=True
)

p = st.radio(
    "四捨五入、切り捨て、切り上げを選んでください",
    ["四捨五入", "切り捨て", "切り上げ"],
    horizontal=True
)


# ========================================
# 計算ボタン
# ========================================
st.write("")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    if st.button("🔄 計算する"):

        if z == "税込み":

            if x == "10％":
                st.session_state.w = (
                    st.session_state.price * 1.1
                )

            elif x == "8％":
                st.session_state.w = (
                    st.session_state.price * 1.08
                )

            elif x == "その他":
                st.session_state.w = (
                    st.session_state.price
                    * (1 + st.session_state.y / 100)
                )

        elif z == "税抜き":

            if x == "10％":
                st.session_state.w = (
                    st.session_state.price / 1.1
                )

            elif x == "8％":
                st.session_state.w = (
                    st.session_state.price / 1.08
                )

            elif x == "その他":
                st.session_state.w = (
                    st.session_state.price
                    / (1 + st.session_state.y / 100)
                )


        # 端数処理
        if p == "四捨五入":

            st.session_state.s = m.floor(
                st.session_state.w + 0.5
            )

        elif p == "切り捨て":

            st.session_state.s = m.floor(
                st.session_state.w
            )

        elif p == "切り上げ":

            st.session_state.s = m.ceil(
                st.session_state.w
            )


# ========================================
# 結果
# ========================================
st.markdown("---")

st.markdown(
    '<div class="section-title" style="text-align:center;">📋 計算結果</div>',
    unsafe_allow_html=True
)


# ========================================
# 税込みの場合
# ========================================
if z == "税込み":

    st.markdown(
        f"""
        <div class="result-box">

            <div class="result-title">
                ✨ 計算結果
            </div>

            <div class="result-row">
                <span>税抜き価格</span>
                <span>{st.session_state.price:,} 円</span>
            </div>

            <div class="result-row">
                <span>消費税</span>
                <span>
                    {st.session_state.s - st.session_state.price:,} 円
                </span>
            </div>

            <hr style="border-color: rgba(255,255,255,0.4);">

            <div class="result-main">
                税込み価格<br>
                {st.session_state.s:,} 円
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ========================================
# 税抜きの場合
# ========================================
elif z == "税抜き":

    st.markdown(
        f"""
        <div class="result-box">

            <div class="result-title">
                ✨ 計算結果
            </div>

            <div class="result-row">
                <span>税込み価格</span>
                <span>{st.session_state.price:,} 円</span>
            </div>

            <div class="result-row">
                <span>消費税</span>
                <span>
                    {st.session_state.price - st.session_state.s:,} 円
                </span>
            </div>

            <hr style="border-color: rgba(255,255,255,0.4);">

            <div class="result-main">
                税抜き価格<br>
                {st.session_state.s:,} 円
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ========================================
# フッター
# ========================================
st.markdown(
    '<div class="note">※ 端数処理は選択した方法に従って計算されます。</div>',
    unsafe_allow_html=True
)
