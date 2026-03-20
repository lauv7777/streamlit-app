import streamlit as st

# 页面设置
st.set_page_config(page_title="电商好评生成器", page_icon="⭐")
st.title("⭐ 电商好评生成器（淘宝卖家专用）")
st.subheader("输入商品关键词，一键生成真实好评")

# 输入区
keyword = st.text_input("输入商品关键词（例如：连衣裙、蓝牙耳机、充电宝、零食）")
type_ = st.selectbox("选择好评类型", ["通用好评", "质量好评", "物流好评", "服务好评", "图文风"])

# 生成按钮
if st.button("生成好评"):
    if not keyword:
        st.warning("请输入商品关键词！")
    else:
        if type_ == "通用好评":
            content = f"""非常满意！{keyword}质量很好，做工精细，颜色和图片一致，
没有色差，大小合适，穿着使用很舒服，性价比超高！
卖家服务态度好，发货快，物流给力，值得推荐！五星好评！"""

        elif type_ == "质量好评":
            content = f"""质量真的超出预期！{keyword}材质很好，手感舒服，
细节处理到位，没有瑕疵，做工很精致，比实体店便宜很多，
物超所值，非常满意，已经推荐给朋友了！"""

        elif type_ == "物流好评":
            content = f"""物流超级快！下单第二天就收到了，包装严实没有损坏，
{keyword}和描述一致，质量很好，使用效果很棒，
卖家服务态度好，回复及时，非常满意！好评！"""

        elif type_ == "服务好评":
            content = f"""卖家服务态度超级好！有问必答，非常耐心，
{keyword}质量很好，款式好看，性价比高，发货速度快，
包装仔细严实，非常满意，以后还会再来光顾！"""

        else:
            content = f"""推荐指数：五星
{keyword}真的太好用了！质量好、颜值高、性价比绝了！
实物和图片一模一样，没有色差，手感超棒！
物流快、服务好、包装严实，强烈推荐大家购买！"""

        # 输出结果
        st.success("好评生成成功！")
        st.code(content, language="text")
        st.info("直接复制即可使用！")
