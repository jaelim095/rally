import pandas as pd
import streamlit as st

import elastic


def render_result_box(
    title: str,
    highlight: str,
    final_score: float = None,
    text_score: float = None,
    vector_score: float = None,
    background_color: str = "#f9f9f9"
) -> None:
    """
    검색 결과 박스 하나 출력 (title + highlight + score info)
    """

    # [1] 점수 정보 표시
    score_info = ""
    if final_score is not None:
        score_info = f"""
        <div style="font-size: 18px; color: #888; margin-top: 10px;">
            hybrid_score: {final_score:.4f}
        </div>
        """
    elif text_score is not None:
        score_info = f"""
        <div style="font-size: 18px; color: #888; margin-top: 10px;">
            text_score: {text_score:.4f}
        </div>
        """
    elif vector_score is not None:
        score_info = f"""
        <div style="font-size: 18px; color: #888; margin-top: 10px;">
            vector_score: {vector_score:.4f}
        </div>
        """
    else:
        # 점수 없으면 공백 추가해서 카드 크기 맞추기
        score_info = """<div style="height: 20px;"></div>"""

    # [2] 박스 출력
    st.markdown(f"""
        <div style="
            background-color: {background_color};
            padding: 15px;
            border-radius: 10px;
            box-shadow: 2px 2px 5px #ccc;
            margin-bottom: 15px;
            height: 230px;  /* 카드 높이 통일 */
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        ">
            <div>
                <div style="font-size: 18px; font-weight: bold; margin-bottom: 10px;">{title}</div>
                <div style="font-size: 16px; line-height: 1.5;">{highlight}</div>
            </div>
            {score_info}
        </div>
    """, unsafe_allow_html=True)

def main() -> None:
    st.set_page_config(layout="wide")
    st.title("Vector Search Demo")

    # 검색어 입력 받기
    col_input, _, _ = st.columns([5, 0.1,  5])
    with col_input:
        input_query = st.text_input("검색어를 입력하세요.", value="네이버")

    # 날짜 입력 받기
    col_x, col_y, col_z = st.columns([5, 0.1,  5])
    with col_x:
        start_date = st.date_input("시작 날짜", value=pd.to_datetime("2023-01-01"))
    with col_y:
        st.write('')
    with col_z:
        end_date = st.date_input("종료 날짜", value=pd.to_datetime("2023-12-31"))

    if st.button("검색"):
        st.markdown("")
        st.markdown("")
        col1, col2, col3 = st.columns(3)
        # [1] 텍스트 검색
        with col1:
            st.header('텍스트 검색')
            results, took = elastic.text_search(
                search_word=input_query,
                start_date=start_date.strftime('%Y-%m-%d'),
                end_date=end_date.strftime('%Y-%m-%d')
            )
            st.subheader(f"소요시간: {took}ms")
            for item in results[:3]:
                render_result_box(item['title'], 
                                  item['highlight'], 
                                  text_score=item['text_score'])

        # [2] 벡터 검색
        with col2:
            st.header('벡터 검색')
            results, took = elastic.vector_search(input_query)
            st.subheader(f"소요시간: {took}ms")
            for item in results[:3]:
                display_text = item['highlight'] if item['highlight'].strip() else item['title']
                render_result_box(item['title'], 
                                  display_text, 
                                  vector_score=item['vector_score'],
                                  background_color="#eef6fa")
        # [3] 하이브리드 검색
        with col3:
            st.header('하이브리드 검색')
            results, took = elastic.rrf_hybrid_search(
                search_word=input_query,
                start_date=start_date.strftime('%Y-%m-%d'),
                end_date=end_date.strftime('%Y-%m-%d')
            )

            st.subheader(f"소요시간: {took}ms")
            for item in results[:3]:
                render_result_box(
                    title=item['title'],
                    highlight=item['highlight'],
                    final_score=item['final_score'])

if __name__ == "__main__":
    elastic.enroll_search_template()
    main()
