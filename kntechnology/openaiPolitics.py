import os
import pandas as pd
import openai
import time
from dotenv import load_dotenv
# API 키 설정
load_dotenv()
openai.api_key = os.getenv('MYKEY')

# 엑셀 파일 불러오기
df = pd.read_excel(r"C:\Users\정유진\Desktop\코난테크놀로지\코난테크놀로지_DS사업부_뉴스기사데이터_240423\코난테크놀로지_DS사업부_뉴스기사데이터_240423\politics\pol_set1(2).xlsx")
def safe_api_call(func, *args, **kwargs):
    for _ in range(5):  # 최대 5번 시도
        try:
            return func(*args, **kwargs)
        except openai.error.RateLimitError as e:
            print(f"요금 초과, 5초 대기 중... 오류: {str(e)}")
            time.sleep(5)
        except (openai.error.APIError, openai.error.APIConnectionError) as e:
            print(f"API 또는 연결 오류 발생, 재시도 중... 오류: {str(e)}")
            time.sleep(5)
        except Exception as e:
            print(f"오류 발생: {str(e)}")
            return None
    return None  # 모든 재시도 실패 시 None 반환

def generate_summary(text1, text2):
        messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"""아래와 같은 기준을 모두 충족하게 맨 아래에 괄호 안에 있는 기사 내용 중 5문장을 선택해줘. 설명이랑 글머리 번호는 필요없어 딱 문장만 작성해주면돼!! 문장 앞에 번호 넣지말고 문장들은 쉼표로 구분해줘. 문장 순서는 주어진 순서가 아니라 중요한 순서대로 해야해. 
1. 주요 구문 갯수
- 기사 1개당 5개의 주요 문장을 선정한다. (중요도 순으로 배열한다.)
1. 주요 문장 선택 기준
- 주요 문장 중 1개 문장은 기사 제목인 "{text1}"과 가장 유사한 문장으로 선택한다.
- 주어나 목적어가 명확하지 않은 문장은 제외한다.	예) “약 90%가 미혼이었다.”, “삶의 만족도도 매우 낮은 편이었다.”
- 사건에 대한 서술 + 원인이 잘 드러날 수 있도록 문장을 구성한다.	예) - 사건에 대한 서술: 올해 삼성전자·SK하이닉스의 아픈 손가락인 낸드플래시 메모리 반도체 시장도 회복 조짐을 보이고 있다.
- 원인: 올해 글로벌 빅테크들이 단행한 대대적인 생성형 인공지능 투자의 온기가 D램에 이어 낸드에까지 미치는 양상이다., 삼성전자·SK하이닉스 등 메모리 기업들이 지난해 연말부터 시행한 낸드 감산이 이제서야 빛을 보고 있다고 평가된다.,이에 더해 올 연말 들어 PC·스마트폰 등 정보기술 기기 수요가 되살아날 조짐을 보이면서 낸드 수요 증가로 이어지는 모양새다.
- 제목"{text1}"에 포함되어 있는 주체 혹은 이슈 관련 분류에 속하는 명사는 요약문 내에 포함되어 있어야 한다.
- 용어에 대한 정의, 인물에 대한 이력을 설명하는 문장은 요약문에서 제외한다.
- 요약문 생성 시, 요약문 내 문장은 서로 독립된 내용으로 구성되어야 한다. (요약문 내의 문장 간 겹치는 내용 최소화)
- 해당 이슈에 대한, 전망, 예상 등을 표현하는 문장은 요약문에 포함한다.	예) 정부는 미복귀한 전공의에게 업무개시명령을 내린 뒤 불이행확인서를 받아 3개월의 면허정지 처분을 내리는 수순을 밟을 것으로 예상된다.
\n\n{text2}"""}]
        response = safe_api_call(
            openai.ChatCompletion.create,
            model="gpt-4",  # gpt-4 채팅 모델 사용
            messages=messages,
            max_tokens=1500,
            temperature=0.5
        )
        if isinstance(response, dict) and 'choices' in response:
             return response.choices[0].message['content'].strip()
        return None

# 키워드를 추출하는 프롬프트 생성
def generate_keywords(summary):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"""{summary} 이 문장들에서 아래와 같은 기준을 모두 충족하게 우선 순위대로 키워드를 뽑아내줘. 키워드만 입력하고 설명이나 글머리기호 같은 건 입력하지마.(잘못된예시: 2. "상무부는 깐깐한 검증을 위해 투자은행 출신 재무 전문가까지 영입했다.", 맞는 예시:"상무부는 깐깐한 검증을 위해 투자은행 출신 재무 전문가까지 영입했다.") 최소 3개 이상 5개 이하여야해.
1. 분류		
주체 관련-인명, 직책 ∙ 직위명, 직업명, 기관∙단체명, 지역명, 종교명,     
이슈 관련-사건∙사고∙사태명, 법∙제도∙정책명, 기술∙IT 용어, 금융 용어, 제품명, 화학약품∙의약품, 행사명, 문화∙예술∙스포츠 관련 명칭 	
		
2. 키워드 선정 우선 순위		 	
사건∙사고∙사태명 →  기관∙단체명 → 인명 → 지역명 → 직책 ∙ 직위명, 기술∙IT 용어 → 법∙제도∙정책명 →  금융용어 → 직업명, 제품명, 화학약품∙의약품, 행사명, 문화∙예술∙스포츠 관련 명칭 		
	

3. 기타 사항 		
- 품사: 체언에 해당하는 명사		
- 범위: 키워드는 주체 관련 분류에 속하는 명사 1개 이상, 이슈 관련 분류에 속하는 명사 1개 이상을 포함해야한다. 		
- 키워드는 단수형 & 단일 명사 형태이며, 기사 1개당 최소 3개 이상 5개 이하로 선정한다.		
- 키워드는 기 선정한 기사 내 주요 구문 상에 존재하는 명사여야 한다.		
- 제목에 등장하는 주체 혹은 이슈 관련 명사 중 1개 이상은 반드시 주요 키워드에 포함한다.		
- 기사 내에 동일 키워드에 대한 중복 표현이 존재하는 경우, 약어가 아닌 원 단어를 키워드로 선정한다.		예) 중대재해처벌법 (O) 중처법(X)
- 동일 인물에 대한 표현이 다수 존재하고, 해당 인물의 인명이 등장하였을 경우에는 인명을 키워드로 선정한다.		예) 국무총리(X) 한덕수(O)
- 특정 인물의 성+직위/직업/직책이 표기되어 있는 경우, 직위/직업/직책을 키워드로 선정한다. 		예) 조교육감(X) 교육감(O)
- 특정 대상을 지칭하지 않는 명사는 2개 이하로 제한한다.		예) 특정 대상을 지칭하지 않는 명사: 쇄신, 도용, 급락, 동맹, 저출산, 고령화, 인하 등
		        키워드 추출 예시: 앱, 접속장애, 먹통, 불편, 지연  →  앱, 접속장애, 불편 
 - 동사, 형용사의 명사형, 감정표현, 기타 용어 분류에 포함되는 명사는  제목에 등장하는 단어만을 키워드로 선정한다. 		예) 檢, 범죄자 가상자산 신속·철저하게 환수한다 
		
*예외 사항 		
키워드는 주요 구문 상에 존재하는 명사로 선정하나, 
주요 구문 내 인물에 대한 표현이 모두 성+직위/직업/직책 형태이고, 기사 내 해당 인물의 인명이 등장한 경우, 해당 인물의 인명을 키워드로 선정한다. 		예) 기사 제목: “당 분열에도 손 놓아”…이재명 ‘안한다 리더십’ 비판 커져
		주요 구문: 이날 시사회에서 이 대표와 이낙연 전 대표 만남이 성사될지 관심이 쏠렸으나 불발됐다,
      당 일각에선 이 대표가 김건희 여사 특검법으로 윤석열 정부를 압박하면서 ‘검찰 때리기’로 지지층을 결집하려 할 뿐 당내 통합에는 소극적이라는 비판이 나온다.,
      갈등 해결을 위해 아무것도 하지 않는 ‘무위(無爲) 리더십’이란 불만이다.
		주요 키워드: 이 대표(X) 이재명(O)
원 단어가 복합 명사 형태의 단어이고, 원 단어의 약어가 한 단어의 영어 단어인 경우에는 약어를 키워드로 선정한다. 		예) 5세대 이동통신(X), 5G(O) """}
    ]
    response = safe_api_call(
            openai.ChatCompletion.create,
            model="gpt-4",  # gpt-4 채팅 모델 사용
            messages=messages,
            max_tokens=1500,
            temperature=0.5
        )
    return response.choices[0].message['content'].strip()

# 태그를 추천하는 프롬프트 생성
def generate_tags(keywords):
       messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"""{keywords} 이 키워드들을 태깅해줘(ex.PS_NAME), 중복되는 같은 태깅은 제외. 키워드 한글은 입력하지 말고 딱 태깅 영어만 입력해줘!!!(ex. 잘못된 예시: 미국 상무부 - OG_ADMINISTRATION , 맞는 예시:OG_ADMINISTRATION) 1.	PERSON(PS)	인명 및 인물의 별칭		
		1.1.	PS_NAME	- 실존/비실존 인물의 이름, 별칭, 인터넷 사용자명
		1.2.	PS_TITLE	- 직책, 직위명 
		1.3.	PS_OCCUPATION	- 직업 명칭
		1.4. 	PS_OTHERS	"- 기타
(주체의 행위에 의한 분류)"
2.	ORGANIZATION(OG)	기관 및 단체		
		2.1.	OGG_ECONOMY	- 경제 관련 기관/단체
		2.2.	OGG_FINANCE	- 금융 기관
		2.3.	OGG_EDUCATION	- 교육 기관/단체, 교육 관련 기관
		2.4.	OGG_MILITARY	- 군사 기관/단체 및 유형, 국방 기관
		2.5.	OGG_MEDIA	- 미디어 기관/단체, 방송 관련 기관/기업
		2.6.	OGG_SPORTS	- 스포츠 기관/단체
		2.7.	OGG_ART	- 예술 기관/단체
		2.8.	OGG_MEDICINE	- 의학/의료 기관/단체
		2.9.	OGG_RELIGION	- 종교 기관/단체, 종파
		2.10.	OGG_SCIENCE	- 과학 기관/단체
		2.11.	OGG_LIBRARY	- 도서관 및 도서관 관련 기관/단체
		2.12.	OGG_ADMINISTRATION	- 정부/행정 기관, 공공기관
		2.13.	OGG_POLITICS	- 정당/정치 기관
		2.14.	OGG_FOOD	- 음식 관련 업체/회사
		2.15.	OGG_HOTEL	- 숙박 관련 업체
		2.16.	OGG_CITIZEN	- 노조/협회/시민단체
		2.17.	OGG_COMMITTEE	- 위원회, 협의체 (임시로 조직된 기구)
		2.19.	OGG_CRIME	- 범죄단체
		2.20.	OGG_OTHERS	- 기타 단체
3.	LOCATION(LC)	지역/장소, 지형/지리		
		3.1.	LC_COUNTRY	- 국가명
		3.2.	LC_PROVINCE	- 도, 주 지역명
		3.3.	LC_COUNTY	- 군, 면, 읍, 리, 동 등과 같은 세부 행정구역명
		3.4.	LC_CITY	- 도시명
		3.5.	LC_GEOGRAPHY	- 지리
		3.6.	LC_CULTURE	- 문화시설
		3.7.	LC_COMMERCE	- 상업시설
		3.8.	LC_TRANSPORTATION	- 교통시설
		3.9.	LC_WELFARE	- 복지시설
		3.10.	LC_OTHERS	- LC 계열의 세부 유형이 아닌 기타 장소
4.	CIVILIZATION(CV)	법/제도/정책		
		4.1.	CV_POLICY	- 제도/정책 명칭
		4.2.	CV_LAW	- 법/법률 명칭
		4.3.	CV_CLAIM	- 법률적 권리
		4.4.	CV_ACTION	- 법률에 의한 행위
		4.5.	CV_TAX	- 조세 명칭
		4.6.	CV_FUNDS	- 연금, 기금, 자금, 펀드 명칭 (기업 운영 상품, 공공 목적 기금 등)
5.	EVENT(EV)	특정 사건/사고/행사 명칭		
		5.1.	EV_ACTIVITY	- 사회운동 및 선언 명칭
		5.2.	EV_SECURITY	- 군사/안보 관련 명칭
		5.3.	EV_SPORTS	- 스포츠/레저 관련 행사 명칭
		5.4.	EV_FESTIVAL	                                                                 
		5.5.	EV_POLITICS	- 정치적 이벤트
		5.6.	EV_CRIME	- 범죄/사건/사고
		5.7.	EV_MEETING	- 회의/학술대회, 조약
		5.8.	EV_DISASTER	- 자연재해
		5.9.	EV_PHENOMENON	- 사회현상
6.	TERM(TM)	용어		
		6.1.	TM_PRODUCT	- 제품명 
		6.2.	TM_FINANCE	- 금융 용어
		6.3.	TM_IT	- 기술∙IT 용어
		6.4.	TM_MEDICINE	- 화학약품 및 의약품명
		6.5.	TM_ADJECTIVE	- 동사, 형용사의 명사형 
		6.6.	TM_EMOTION	- 감정표현
		6.7.	TM_ART	- 문화예술 관련 명칭 
		6.8.	TM_SPORTS	- 스포츠/레포츠/레저 명칭 
		6.9.	TM_OTHERS	- 기타 용어
		6.10.	TM_TRENDWORD	- 신조어
7.	ACTION(ACT)	행위		
		7.1.	ACT_ECONOMY	경제 행위
		7.2.	ACT_LAW	법률 행위
		7.3.	ACT_EDUCATION	교육 행위
		7.4.	ACT_MEDICINE	보건∙의료 행위
		7.5.	ACT_RELIGION	종교 행위
		7.6.	ACT_BROADCAST	언론 행위
		7.7.	ACT_DIPLOMACY	외교 행위
		7.8.	ACT_SECURITY	군사/안보 행위
		7.9.	ACT_LABOR	고용∙노동 행위

\n\n{keywords}"""}]
       response = safe_api_call(
            openai.ChatCompletion.create,
            model="gpt-4",  # gpt-4 채팅 모델 사용
            messages=messages,
            max_tokens=1500,
            temperature=0.5
        )
       return response.choices[0].message['content'].strip()


df['Summary'] = df.apply(lambda row: generate_summary(row[4], row[6]), axis=1)

# None 값 제거
df.dropna(subset=['Summary'], inplace=True)

# 키워드 생성
df['Keywords'] = df['Summary'].apply(lambda x: generate_keywords(x) if pd.notna(x) else None)

# 태그 생성
df['Tags'] = df['Keywords'].apply(lambda x: generate_tags(x) if pd.notna(x) else None)
# 결과를 새로운 엑셀 파일로 저장
df.to_excel(r"C:\Users\정유진\Desktop\코난테크놀로지\코난테크놀로지_DS사업부_뉴스기사데이터_240423\코난테크놀로지_DS사업부_뉴스기사데이터_240423\politics\output(2).xlsx", index=False)

