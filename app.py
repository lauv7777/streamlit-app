import streamlit as st

# 页面设置
st.set_page_config(page_title="AI工具合集", page_icon="🚀", layout="wide")

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

# 主标题
st.title("🚀 AI 工具合集")
st.markdown("### 好评 | 文案 | 脚本 | 简历 | 考研，一站式搞定！")

# 创建选项卡
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "⭐ 电商好评", 
    "📕 小红书文案", 
    "🎬 短视频脚本", 
    "📄 简历优化", 
    "📚 考研政治", 
    "🍔 外卖好评"
])

# ==================== 1. 电商好评生成 ====================
with tab1:
    st.subheader("淘宝/拼多多/京东 好评生成")
    keyword = st.text_input("输入商品关键词", placeholder="例如：连衣裙、蓝牙耳机、零食", key="good")
    type_good = st.selectbox("选择好评类型", ["通用好评", "质量好评", "物流好评", "服务好评"], key="good_type")

    if st.button("生成好评", key="btn_good"):
        if not keyword:
            st.warning("请输入商品关键词！")
        else:
            if type_good == "通用好评":
                res = f"非常满意！{keyword}质量很好，做工精细，性价比超高！卖家服务好，发货快，物流给力，值得推荐！五星好评！"
            elif type_good == "质量好评":
                res = f"{keyword}质量超出预期！材质好，手感舒服，做工精致，没有瑕疵，比实体店便宜，物超所值！"
            elif type_good == "物流好评":
                res = f"物流超级快！包装严实无损坏，{keyword}和描述一致，质量好，使用效果棒，好评！"
            else:
                res = f"卖家服务态度超好！有问必答，{keyword}质量好，发货快，包装仔细，满意！"
            
            st.success("✅ 好评生成成功！")
            st.code(res, language="text")

# ==================== 2. 小红书文案生成 ====================
with tab2:
    st.subheader("小红书爆款文案生成")
    theme = st.text_input("输入文案主题", placeholder="例如：穿搭、美食、护肤、旅行", key="note")
    style_note = st.selectbox("选择文案风格", ["干货分享", "情绪共鸣", "搞笑沙雕", "种草测评"], key="note_type")

    if st.button("生成文案", key="btn_note"):
        if not theme:
            st.warning("请输入文案主题！")
        else:
            if style_note == "干货分享":
                res = f"💡{theme}干货分享｜新手也能学会\n\n今天给大家整理了{theme}的保姆级教程，亲测有效，建议收藏慢慢看✨\n\n#干货分享 #教程"
            elif style_note == "情绪共鸣":
                res = f"谁懂啊😭 {theme}真的太治愈了\n\n快乐就是这么简单，{theme}真的会让人心情变好❤️\n\n#情绪治愈 #日常分享"
            elif style_note == "搞笑沙雕":
                res = f"家人们谁懂啊🤣 {theme}真的笑不活了\n\n没想到{theme}能这么搞笑，笑到肚子疼😂\n\n#搞笑沙雕 #日常"
            else:
                res = f"🔥{theme}测评｜真实体验\n\n亲测{theme}真的好用，性价比超高，姐妹们可以冲！\n\n#种草测评 #好物分享"
            
            st.success("✅ 文案生成成功！")
            st.code(res, language="text")

# ==================== 3. 短视频脚本生成（探店号） ====================
with tab3:
    st.subheader("探店短视频脚本生成")
    shop_name = st.text_input("店铺名称", placeholder="例如：XX火锅店、XX咖啡馆")
    shop_type = st.selectbox("店铺类型", ["美食探店", "奶茶探店", "景点打卡", "好物测评"])

    if st.button("生成脚本", key="btn_script"):
        if not shop_name:
            st.warning("请输入店铺名称！")
        else:
            if shop_type == "美食探店":
                script = f"""【开头3秒】
家人们！今天发现一家宝藏{shop_name}！🔥

【中间内容】
环境超有氛围感，菜品新鲜分量足，性价比绝了！
推荐必点：招牌菜，一口沦陷！

【结尾】
人均XX元，闭眼冲不亏！赶紧艾特饭搭子冲！
#探店 #美食 #宝藏店铺"""
            elif shop_type == "奶茶探店":
                script = f"""【开头3秒】
奶茶脑袋集合！这家{shop_name}太绝了！🥤

【中间内容】
颜值爆表，口感丝滑，甜度刚好不腻！
新品必冲，喝一口直接爱上！

【结尾】
奶茶控快冲，不好喝你来打我！
#奶茶 #探店 #网红奶茶"""
            else:
                script = f"""【开头3秒】
发现小众打卡地！{shop_name}超出片！📸

【中间内容】
环境绝美，随手一拍都是大片！
人少景美，周末放松好去处！

【结尾】
快约上姐妹来打卡，刷爆朋友圈！
#打卡 #小众景点 #周末去哪儿"""
            
            st.success("✅ 脚本生成成功！")
            st.code(script, language="text")

# ==================== 4. 简历优化（大学生） ====================
with tab4:
    st.subheader("大学生简历优化")
    job = st.text_input("应聘岗位", placeholder="例如：新媒体运营、产品经理、教师")
    experience = st.text_area("你的经历", placeholder="描述你的实习/项目/校园经历")

    if st.button("优化简历", key="btn_resume"):
        if not job or not experience:
            st.warning("请填写完整信息！")
        else:
            optimized = f"""【{job}岗位】
{experience}
✅ 熟练掌握相关技能，具备良好的沟通能力与团队协作精神
✅ 工作认真负责，学习能力强，能快速适应岗位需求
✅ 拥有相关项目/实习经验，能独立完成工作任务"""
            
            st.success("✅ 简历优化成功！")
            st.code(optimized, language="text")

# ==================== 5. 考研政治模板生成 ====================
with tab5:
    st.subheader("考研政治答题模板")
    type_poli = st.selectbox("题型", ["马原分析题", "毛中特分析题", "史纲分析题"])

    if st.button("生成模板", key="btn_poli"):
        if type_poli == "马原分析题":
            template = """【答题模板】
1. 原理名称+内容
2. 结合材料分析
3. 总结+方法论"""
        elif type_poli == "毛中特分析题":
            template = """【答题模板】
1. 点明核心观点
2. 结合材料分析意义/原因
3. 总结+展望"""
        else:
            template = """【答题模板】
1. 历史事件背景+内容
2. 历史意义+启示
3. 总结升华"""
        
        st.success("✅ 模板生成成功！")
        st.code(template, language="text")

# ==================== 6. 外卖好评生成（商家） ====================
with tab6:
    st.subheader("外卖好评生成")
    food = st.text_input("菜品名称", placeholder="例如：红烧肉、麻辣烫、炸鸡")
    type_wm = st.selectbox("好评类型", ["通用好评", "口味好评", "包装好评", "配送好评"])

    if st.button("生成外卖好评", key="btn_wm"):
        if not food:
            st.warning("请输入菜品名称！")
        else:
            if type_wm == "通用好评":
                res = f"味道超赞！{food}口感很好，分量足，性价比高，配送快，包装严实，非常满意！五星好评！"
            elif type_wm == "口味好评":
                res = f"{food}太好吃了！味道正宗，口感绝佳，咸淡适中，食材新鲜，下次还点！"
            elif type_wm == "包装好评":
                res = f"包装非常严实，没有洒漏，{food}还是热乎的，干净卫生，非常用心！"
            else:
                res = f"配送速度超快，小哥态度好，{food}完好无损，准时送达，非常满意！"
            
            st.success("✅ 外卖好评生成成功！")
            st.code(res, language="text")

# ==================== 底部引流 ====================
st.markdown("---")
st.markdown("### 💡 更多AI工具 + 副业变现")
st.markdown("**微信：Lauv_0613（备注：AI工具）**")
st.markdown("👉 领取AI赚钱玩法，轻松起步
             福利：转发本网站到朋友圈/群聊，截图发微信，免费领取【100套小红书爆款标题库】")
