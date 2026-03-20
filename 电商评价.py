import streamlit as st

# 页面设置
st.set_page_config(page_title="电商好评生成器", page_icon="⭐", layout="wide")

# 自定义样式
st.markdown("""
<style>
    .stButton>button {
        background-color: #ff4d4f;
        color: white;
        border-radius: 10px;
        font-size: 18px;
        height: 50px;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# 标题
st.title("⭐ 电商好评生成器")
st.markdown("### 淘宝/拼多多/京东 通用好评，一键生成！")

# 输入区
col1, col2 = st.columns(2)
with col1:
    keyword = st.text_input("📦 输入商品名称", placeholder="例如：连衣裙、蓝牙耳机、零食")
with col2:
    type_ = st.selectbox("🎯 选择好评类型", ["通用好评", "质量好评", "物流好评", "服务好评"])

# 生成按钮
if st.button("✨ 立即生成好评"):
    if not keyword:
        st.warning("⚠️ 请输入商品名称！")
    else:
        if type_ == "通用好评":
            content = f"非常满意！{keyword}质量很好，做工精细，性价比超高！卖家服务好，发货快，物流给力，值得推荐！五星好评！"
        elif type_ == "质量好评":
            content = f"{keyword}质量超出预期！材质好，手感舒服，做工精致，没有瑕疵，比实体店便宜，物超所值！"
        elif type_ == "物流好评":
            content = f"物流超级快！包装严实无损坏，{keyword}和描述一致，质量好，使用效果棒，非常满意！"
        else:
            content = f"卖家服务态度超好！有问必答，{keyword}质量好，发货快，包装仔细，以后还会再来！"
        
        st.success("✅ 好评生成成功！")
        st.code(content, language="text")
        st.info("📋 直接复制粘贴到评价区即可！")
