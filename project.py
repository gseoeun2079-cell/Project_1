import streamlit as st
from streamlit_gsheets import GSheetsConnection

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(spreadsheet="https://docs.google.com/spreadsheets/d/1aH0yr2MrIu8aIjd2TR-HmvKZV2CmLJf_zVaHwj8V5UE/edit?gid=888589420#gid=888589420")

def user_menu_selected(a):
    output = df[(df['국가'] == a['국가']) & (df['국물'] == a['국물']) & (df['맵기'] == a['맵기']) & (df['온도'] == a['온도']) & (df['주식'] == a['주식']) & (df['스타일'] == a['스타일'])]
    return output['추천 메뉴'].values[0]

if '결과' not in st.session_state:
    st.session_state.결과 = ''

if 'page' not in st.session_state:
    st.session_state.page = '첫화면'

if st.session_state.page == '첫화면':
    st.title("배달 메뉴 추천")
    st.subheader("사용자의 기분에 맞게 배달 메뉴를 추천해드립니다.")
    if st.button("시작하기"):
        st.session_state.page = '선택화면'
        st.rerun()


elif st.session_state.page == '선택화면':
    st.header("질문에 답해주세요")
    selected_option1 = st.selectbox("한식과 중식, 양식 중 골라주세요",("한식","중식","양식"))
    selected_option2 = st.selectbox("국물이 있는 음식을 원하시나요?",("있음","없음"))
    selected_option3 = st.selectbox("매운 음식을 원하시나요?",("매움","안매움"))
    selected_option4 = st.selectbox("시원한 음식을 원하시나요, 따뜻한 음식을 원하시나요?",("차가움","뜨거움"))
    selected_option5 = st.selectbox("밥 종류의 음식을 원하시나요, 면 종류의 음식을 원하시나요?",("밥","면"))
    selected_option6 = st.selectbox("기름진 음식을 원하시나요, 깔끔한 음식을 원하시나요?",("기름짐","깔끔함"))
    a = {'국가':selected_option1,'국물':selected_option2,'맵기':selected_option3,'온도':selected_option4,'주식':selected_option5,'스타일':selected_option6}
    if st.button("선택완료"):
        st.session_state.page = '결과화면'
        st.session_state.결과 = user_menu_selected(a)
        st.rerun()
        
elif st.session_state.page == '결과화면':
    st.header("오늘의 추천메뉴는?")
    st.write(st.session_state.결과)
    if st.button("처음으로 돌아가기"):
        st.session_state.page = '첫화면'
        st.rerun()
