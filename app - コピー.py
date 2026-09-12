import streamlit as st

#ページ設定
st.set_page_config(page_title="一人暮らしサポートポータル", page_icon="🏠")

#タイトル
st.title("🏠 一人暮らしサポートポータル")
st.write("一人暮らしの準備をサポートするツール集です。")

#5つのカテゴリーをカード風に表示するための列構成
col1, col2 = st.columns(2)

#一人暮らし必需品（リンク）
with col1:
    st.subheader("🛒 一人暮らし必需品")
    st.link_button("ツールを開く", "https://ryucry-kurashi-no-yohaku-app-jbr9xr.streamlit.app/")

#Wi-Fi・スマホ通信費（準備中）
with col2:
    st.subheader("📶 Wi-Fi・スマホ通信費")
    st.button("準備中", key="wifi", disabled=True)

#自炊・食生活（準備中）
with col1:
    st.subheader("🍳 自炊・食生活")
    st.button("準備中", key="cooking", disabled=True)

#生活費（準備中）
with col2:
    st.subheader("💰 生活費")
    st.button("準備中", key="budget", disabled=True)

#ふるさと納税（準備中）
with col1:
    st.subheader("🎁 ふるさと納税")
    st.button("準備中", key="tax", disabled=True)

フッター
st.markdown("---")
st.caption("一人暮らしの準備をスムーズに。")
