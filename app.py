import streamlit as st

# 页面设置
st.set_page_config(page_title="小红书文案生成器", page_icon="📝")
st.title("📝 小红书爆款文案生成器")
st.subheader("输入主题，一键生成吸睛文案")

# 输入区
theme = st.text_input("输入你的主题（例如：减脂早餐、平价护肤、大学生穿搭）")
style = st.selectbox("选择文案风格", ["可爱元气", "高级清冷", "干货实用", "搞笑沙雕"])

# 生成按钮
if st.button("生成文案"):
    if not theme:
        st.warning("请输入主题！")
    else:
        # 不同风格模板
        if style == "可爱元气":
            content = f"""✨ {theme} 真的太绝了！
谁懂啊姐妹们！挖到宝了～
软软糯糯 / 香香甜甜 / 超治愈
每天用 / 吃 / 穿都幸福感爆棚💖
# {theme} #好物分享 #学生党必备"""

        elif style == "高级清冷":
            content = f"""▫️ {theme}｜极简质感
不费力的高级感
干净、克制、耐看
日常氛围感拉满
# {theme} #高级感 #小众好物"""

        elif style == "干货实用":
            content = f"""📌 {theme} 保姆级攻略
新手必看！全是干货不废话
步骤清晰 / 效果明显 / 亲测有效
建议收藏慢慢看✨
# {theme} #干货分享 #教程"""

        else:  # 搞笑沙雕
            content = f"""救命！{theme} 笑不活了😂
谁用谁知道！快乐加倍
沙雕女孩必备
快乐就是这么简单～
# {theme} #搞笑日常 #沙雕好物"""

        # 输出结果
        st.success("文案生成成功！")
        st.markdown(f"```\n{content}\n```")
        st.info("直接复制即可发布小红书！")
