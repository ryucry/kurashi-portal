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
<div class="main-content">

    <div class="lead-label">— 調べ尽くして、選ぶ。</div>

    <div class="catch-copy">
        暮らしはゆるく、<br>
        調べるときは本気で。
    </div>

    <div class="description">
        一人暮らしの買い物と契約を、実際に並べて数えて、
        から決める検証ノート。<br>
        タオルは何枚いるか、スマホ代はどこまで下げられるか。
        数字で決める仕事の癖を、暮らしに持ち込みました。
    </div>

    <div class="result-card">
        <div class="result-label">検証した結論</div>

        <div class="result-title">
            まず試すなら、3,000円台の1枚から
        </div>

        <div class="result-text">
            実際に比較した結果、最初から高価なセットを買うより、
            必要なものを一つずつ試すほうが無駄を減らせます。
        </div>
    </div>

</div>
""", unsafe_allow_html=True)
