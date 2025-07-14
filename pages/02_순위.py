import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="예쁜 여자 연예인 순위", page_icon="💃")
st.title("💃 가장 예쁜 여자 연예인 TOP 10 (비공식 & 주관적 순위)")
st.write("이 순위는 팬 커뮤니티·비주얼 인기 투표 등을 참고한 가상의 데이터입니다.")

# 가상의 예쁜 여자 연예인 순위 데이터
celebs = [
    "아이유", "지수 (BLACKPINK)", "수지", "쯔위 (TWICE)",
    "사나 (TWICE)", "장원영 (IVE)", "설현", "산다라박",
    "윤아 (소녀시대)", "미연 ((여자)아이들)"
]
votes = [98, 95, 93, 90, 89, 87, 85, 83, 82, 80]  # 가상의 점수 (100점 만점)

# Plotly 막대 그래프
fig = go.Figure(data=[
    go.Bar(
        x=votes,
        y=celebs,
        orientation='h',
        marker=dict(color='hotpink'),
        text=[f"{v}점" for v in votes],
        textposition='outside'
    )
])

fig.update_layout(
    xaxis=dict(range=[0, 105]),
    title="✨ 비공식 인기 기반 여자 연예인 비주얼 순위 TOP 10",
    yaxis_title="연예인",
    xaxis_title="비주얼 점수",
    height=600
)

st.plotly_chart(fig)

# 주의 문구
st.caption("⚠️ 이 순위는 실제 공식 통계나 여론 조사가 아니며, 예시일 뿐입니다. 모두 각자의 개성과 아름다움이 있습니다!")
