import streamlit as st

# 页面设置
st.set_page_config(page_title="电商好评生成器")
st.title("电商好评生成器")
st.subheader("输入商品关键词，一键生成好评")

# 输入
keyword = st.text_input("输入商品关键词")
style = st.selectbox("选择类型", ["通用", "质量", "物流", "服务"])

# 生成
if st.button("生成好评"):
    if not keyword:
        st.warning("请输入关键词")
    else:
        if style == "通用":
            res = f"非常满意！{keyword}质量很好，做工精细，性价比高，卖家服务好，发货快，值得推荐！"
        elif style == "质量":
            res = f"{keyword}质量超出预期，材质好，手感舒服，做工精致，物超所值，非常满意！"
        elif style == "物流":
            res = f"物流很快，包装严实，{keyword}和描述一致，质量好，使用效果棒，好评！"
        else:
            res = f"卖家服务态度好，有问必答，{keyword}质量好，发货快，包装仔细，满意！"
        
        st.success("生成成功")
        st.write(res)
