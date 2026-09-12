import streamlit as st

st.set_page_config(
    page_title="新生活 暮らしアップデート",
    page_icon="🌙",
    layout="wide"
)

# デザイン設定
st.markdown("""
<style>
.stApp {
    background-color: #171b1d;
    color: #f5f5f5;
    background-image:
        linear-gradient(rgba(100, 120, 125, 0.12) 1px, transparent 1px),
        linear-gradient(90deg, rgba(100, 120, 125, 0.12) 1px, transparent 1px);
    background-size: 52px 52px;
}

/* 上部ヘッダー */
.header {
    padding: 25px 5% 10px 5%;
    border-bottom: 1px solid #394044;
}

.logo {
    font-size: 30px;
    letter-spacing: 8px;
    color: #ffffff;
}

.subtitle {
    color: #8d999d;
    font-size: 16px;
    letter-spacing: 3px;
}

/* ナビゲーション */
.nav-box {
    margin-top: 25px;
    padding: 12px 0;
    color: #9ca8ac;
    font-size: 16px;
}

/* メイン文章 */
.main-content {
    max-width: 950px;
    margin: 70px auto;
    padding: 0 30px;
}

.lead-label {
    color: #479dcc;
    font-size: 16px;
    letter-spacing: 4px;
    margin-bottom: 25px;
}

.catch-copy {
    color: #ffffff;
    font-size: clamp(36px, 6vw, 76px);
    font-weight: bold;
    line-height: 1.35;
    letter-spacing: 5px;
    margin-bottom: 45px;
}

.description {
    color: #a9b1b4;
    font-size: 20px;
    line-height: 2.2;
    letter-spacing: 2px;
}

/* カード */
.result-card {
    margin-top: 70px;
    padding: 35px;
    border: 1px solid #3c474b;
    border-radius: 12px;
    background: rgba(15, 18, 19, 0.65);
}

.result-label {
    color: #65acd2;
    font-size: 18px;
    letter-spacing: 3px;
}

.result-title {
    color: white;
    font-size: 30px;
    font-weight: bold;
    margin: 25px 0;
}

.result-text {
    color: #a9b1b4;
    font-size: 17px;
    line-height: 2;
}
</style>
""", unsafe_allow_html=True)


# ヘッダー
st.markdown("""
<div class="header">
    <div class="logo">新生活 暮らしアップデート</div>
    <div class="subtitle">がんばりすぎない、ちょうどいい暮らし</div>
</div>
""", unsafe_allow_html=True)


# 選択メニューを上部に配置
menu = st.selectbox(
    "カテゴリーを選択",
    [
        "一人暮らし必需品",
        "Wi-Fiとsim",
        "食",
        "生活必需品",
        "ふるさと納税"
    ],
    label_visibility="collapsed"
)


# メニューの下に表示
st.markdown(f"""
<div class="nav-box">
    選択中：{menu}
</div>
""", unsafe_allow_html=True)


# メイン文章
st.markdown("""
<div class="description">
    「片づけたいのに、なかなか進まない」
    そんな人に向けて、無理なく続けられる
    暮らしの整え方を紹介します。
</div>

<div class="result-card">
    <div class="result-label">診断結果</div>

    <div class="result-title">
        楽しみながら、少しずつ整えるタイプ
    </div>

    <div class="result-text">
        無理に全部を捨てるのではなく、
        今の暮らしに必要なものを選びながら、
        自分のペースで整えていくのがおすすめです。
    </div>
</div>
""", unsafe_allow_html=True)
