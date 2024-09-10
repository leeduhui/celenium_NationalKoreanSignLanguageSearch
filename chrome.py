import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ChromeDriver 경로 설정
service = Service('C:/Users/scott/chrome/128/chromedriver-win64/chromedriver-win64/chromedriver.exe')  
options = webdriver.ChromeOptions()

# WebDriver 실행
driver = webdriver.Chrome(service=service, options=options)

# 웹 페이지 열기
driver.get('https://sldict.korean.go.kr/searchKor/searchMain/searchMain.do')

# 엑셀 파일에서 데이터 읽기
file_path = '전문용어선정_후보_from_Erin.xlsx'
df = pd.read_excel(file_path, engine='openpyxl', usecols="B", skiprows=1)  # B열만 읽기, B2부터 시작
df["검색 결과"] = ""  # E열을 의미하는 '검색 결과' 열을 추가

# B열의 각 단어에 대해 검색하고 결과 추출
for index, row in df.iterrows():
    word = row[0]

    # 검색창 찾기
    search_box = driver.find_element(By.ID, 'searchKeyword')
    search_box.clear()

    # 단어 입력 및 검색
    search_box.send_keys(word)
    search_box.send_keys(Keys.RETURN)

    # 잠시 대기 (결과 로딩 시간 고려)
    time.sleep(2)

    # 결과 페이지에서 '한국어 표제어' 부분 확인
    try:
        result_element = driver.find_element(By.CSS_SELECTOR, 'div.search_tit.black_line')
        result_text = result_element.text

        # 결과 수 확인
        result_count_element = driver.find_element(By.CSS_SELECTOR, 'strong.red')
        result_count = result_count_element.text

        # 검색 결과 콘솔에 출력
        print(f"[{index + 1}] 검색어: {word}, 결과: {result_text}: {result_count}건")

        # 검색 결과 E열에 추가
        df.at[index, "검색 결과"] = f"{result_text}: {result_count}건"

    except Exception:
        # 결과가 없을 경우
        print(f"[{index + 1}] 검색어: {word}, 결과 없음")
        df.at[index, "검색 결과"] = "결과 없음"

# 브라우저 닫기
driver.quit()

# 결과를 엑셀 파일에 저장
df.to_excel('전문용어선정_후보_with_results.xlsx', index=False, engine='openpyxl')

print("검색 완료 및 엑셀 파일 저장 완료.")
