import streamlit as st
import time


st.write("プログレスバーの表示")
"Start!!"

# バーの上に文字をおく
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.1)


# リストみたいなやつ
expander1 = st.expander("問い合わせ1")
expander1.write("問い合わせ内容1")

expander2 = st.expander("問い合わせ2")
expander2.write("問い合わせ内容2")

expander3 = st.expander("問い合わせ3")
expander3.write("問い合わせ内容3")


