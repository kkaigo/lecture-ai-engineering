import streamlit as st
import pandas as pd
import numpy as np
import time

# ============================================
# ページ設定
# ============================================
st.set_page_config(
    page_title="Streamlit demo",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# タイトルと説明
# ============================================
st.title("Streamlit demo for beginner")
st.markdown("### Learn about features of Streamlit while uncommenting!")
# st.markdown("このデモコードでは、コメントアウトされた部分を順番に解除しながらUIの変化を確認できます。")

# ============================================
# サイドバー 
# ============================================
# st.sidebar.header("guide to demo")
# st.sidebar.info("コードのコメントを解除して、Streamlitのさまざまな機能を確認しましょう。")

# ============================================
# 基本的なUI要素
# ============================================
st.header("Basic UI elements")

# テキスト入力
st.subheader("Text Input")
name = st.text_input("Your Name", "Guest")
st.write(f"Hello, {name}!")

# ボタン
st.subheader("Button")
if st.button("Click Here"):
    st.success("Click Success!")

# チェックボックス
st.subheader("Check Box")
if st.checkbox("Additional content will be displayed when checked!"):
    st.info("This is hidden content!")

# スライダー
st.subheader("Slider")
age = st.slider("Age", 0, 100, 20)
st.write(f"Your Age: {age}")

# セレクトボックス
st.subheader("Dropdown")
option = st.selectbox(
    "好きなプログラミング言語は?",
    ["Python", "JavaScript", "Java", "C++", "Go", "Rust"]
)
st.write(f"Your choice is {option}!")

# ============================================
# レイアウト
# ============================================
st.header("Layout")

# カラム
st.subheader("Column Layout")
col1, col2 = st.columns(2)
with col1:
    st.write("Left")
    st.number_input("Enter number", value=10)
with col2:
    st.write("Right")
    st.metric("Metrics", "42", "2%")

# タブ
st.subheader("Tab")
tab1, tab2 = st.tabs(["First", "Second"])
with tab1:
    st.write("This is content of First!")
with tab2:
    st.write("This is content of Second!")

# エクスパンダー
st.subheader("Expander")
with st.expander("Display details"):
    st.write("This is hidden contents in Display details!")
    st.code('print("Damn it. I\'ve been found!")')

# ============================================
# データ表示
# ============================================
st.header("Display data")

# サンプルデータフレームを作成
df = pd.DataFrame({
    'Name': ['Adam', 'Cristina', 'Lee', 'Sato', 'Julie'],
    'Age': [25, 30, 22, 28, 33],
    'City': ['London', 'Texas', 'Seoul', 'Tokyo', 'Paris']
})

# データフレーム表示
st.subheader("Dataframe")
st.dataframe(df, use_container_width=True)

# テーブル表示
st.subheader("Table")
st.table(df)

# メトリクス表示
st.subheader("Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "23°C", "1.5°C")
col2.metric("Humidity", "45%", "-5%")
col3.metric("Pressure", "1013hPa", "0.1hPa")

# ============================================
# グラフ表示
# ============================================
st.header("Graph Display")

# ラインチャート
st.subheader("Line Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C'])
st.line_chart(chart_data)

# バーチャート
st.subheader("Bar Chart")
chart_data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [10, 25, 15, 30]
}).set_index('Category')
st.bar_chart(chart_data)

# ============================================
# インタラクティブ機能
# ============================================
st.header("Interactive Function")

# プログレスバー
st.subheader("Progress Chart")
progress = st.progress(0)
if st.button("Simulate Progress"):
    for i in range(101):
        time.sleep(0.01)
        progress.progress(i / 100)
    st.balloons()

# ファイルアップロード
st.subheader("Upload File")
uploaded_file = st.file_uploader("Upload File", type=["csv", "txt"])
if uploaded_file is not None:
    # ファイルのデータを表示
    bytes_data = uploaded_file.getvalue()
    st.write(f"File size: {len(bytes_data)} bytes")
    
    # CSVの場合はデータフレームとして読み込む
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
        st.write("Preview CSV data:")
        st.dataframe(df.head())

# ============================================
# カスタマイズ
# ============================================
st.header("Style Customization")

# カスタムCSS
st.markdown("""
<style>
.big-font {
    font-size:20px ！important;
    font-weight: bold;
    color: #0066cc;
}
</style>
""", unsafe_allow_html=True)
# 
st.markdown('<p class="big-font">This is text styled with custom CSS!</p>', unsafe_allow_html=True)

# ============================================
# デモの使用方法
# ============================================
# st.divider()
# st.subheader("How to use this demo.")
# st.markdown("""
# 1. コードエディタでコメントアウトされた部分を見つけます（#で始まる行）
# 2. 確認したい機能のコメントを解除します（先頭の#を削除）
# 3. 変更を保存して、ブラウザで結果を確認します
# 4. 様々な組み合わせを試して、UIがどのように変化するか確認しましょう
# """)

st.code("""
コメントアウトされた例:
if st.button("Click Here"):
    st.success("Click Success!")

# コメントを解除した例:
if st.button("Click Here"):
    st.success("Click Success!")
""")