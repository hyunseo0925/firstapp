import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="MBTI 궁합으로 보는 미연과의 확률", page_icon="💘")
st.title("💘 MBTI 궁합으로 보는 미연과의 사귈 확률")
st.write("이건 팬심으로 만든 가상 궁합 테스트입니다. 현실과는 다를 수 있어요 😉")

# 사용자의 MBTI 선택
mbti_options = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]
user_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_options)

# INFP(미연)과의 궁합 점수 (가상의 데이터 기반)
# 점수는 0~100 기준으로 설정
compatibility_scores = {
    "INTJ": 75,
    "INTP": 82,
    "ENTJ": 60,
    "ENTP": 88,
    "INFJ": 90,
    "INFP": 100,  # 둘 다 INFP인 경우
    "ENFJ": 85,
    "ENFP": 95,
    "ISTJ": 55,
    "ISFJ": 78,
    "ESTJ": 40,
    "ESFJ": 70,
    "ISTP": 60,
    "ISFP": 92,
    "ESTP": 50,
    "ESFP": 85
}

# 궁합 점수 가져오기
score = compatibility_scores.get(user_mbti, 50)

# Plotly 게이지 차트
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=score,
    title={'text': f"{user_mbti} vs INFP (미연)의 궁합 확률"},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "deeppink"},
        'steps': [
            {'range': [0, 40], 'color': "#ffe6e6"},
            {'range': [40, 70], 'color': "#ffb3c6"},
            {'range': [70, 90], 'color': "#ff6f91"},
            {'range': [90, 100], 'color': "#ff1e56"},
        ],
    }
))

st.plotly_chart(fig)

# 멘트 출력
if score >= 90:
    st.success("✨ 미연이랑 찰떡 궁합이에요! 팬으로서도 기뻐할 수준!")
elif score >= 70:
    st.info("꽤 잘 맞아요! 좋은 대화가 가능할지도?")
elif score >= 50:
    st.warning("성격 차이는 있지만, 노력하면 어울릴 수도 있어요.")
else:
    st.error("현실은 시련이 많지만, 팬심은 그걸 이겨내죠. 화이팅!")

