from fpdf import FPDF
from datetime import datetime

# FPDF 클래스를 상속받은 PDF 클래스 정의
class PDF(FPDF):
    # 페이지 헤더를 설정하는 메소드
    def header(self):
        self.set_font('Arial', 'B', 25)  # 폰트 설정: Arial, Bold, 크기 25
        self.cell(0, 10, '> XSAS Results Report <', 0, 1, 'C')  # 셀 추가: 넓이 0(전체), 높이 10, 텍스트, 테두리 없음, 다음 셀 위치(다음 줄), 정렬 가운데
        self.set_line_width(1)
        self.set_draw_color(0, 0, 0)  # 색 설정
        #self.line(10, 45, 200, 45)  # 라인 그리기
        #self.set_line_width(1)
        self.set_draw_color(0, 0, 0)  # 검은색 설정
        self.set_text_color(0, 0, 0)  # 텍스트 색상 검은색 설정

    # 페이지 푸터를 설정하는 메소드
    def footer(self):
        self.set_y(-15)  # 페이지 하단에서 15단위 위로 이동
        self.set_font('Arial', 'I', 8)  # 폰트 설정: Arial, Italic, 크기 8
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')  # 셀 추가: 페이지 번호 표시, 정렬 가운데

    # 챕터 제목을 설정하는 메소드
    def chapter_title(self, title):
        self.set_y(65)  # Y 좌표를 헤더 아래로 이동
        self.set_font('Arial', 'B', 20)  # 폰트 설정: Arial, Bold, 크기 20
        self.cell(0, 10, title, 0, 1, 'L')  # 셀 추가: 넓이 0(전체), 높이 10, 제목 텍스트, 테두리 없음, 다음 셀 위치(다음 줄), 정렬 왼쪽
        self.ln(10)  # 줄 간격 추가

    # 챕터 본문을 설정하는 메소드
    def chapter_body(self, title, links):
        self.set_font('Arial', 'B', 12)  # 취약점 유형을 굵게 설정
        self.cell(0, 10, title, ln=1, border=1)  # 취약점 유형 추가
        self.set_font('Arial', '', 10)  # 링크들을 작은 글씨로 설정
        for link in links:
            self.multi_cell(0, 8, link, border=1, align='L')  # 링크 추가
            # self.cell(0, 10, link, ln=1, border=1)  # 링크 추가
        self.ln(10)  # 줄 간격 추가

    # 검은색 선을 그리는 메소드
    def draw_black_line(self):
        self.set_line_width(1)
        self.set_draw_color(0, 0, 0)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(10)

    # 동적으로 URL과 취약점 목록을 설정하는 메소드
    def set_dynamic_content(self, inputURL, collectVul):
        self.set_font("Arial", 'B', 12)
        self.cell(30, 10, "Website URL : ", ln=0)  # 굵게 표시
        self.set_text_color(255, 150, 0)  # 노란색 설정

        # URL 리스트를 문자열로 변환
        if isinstance(inputURL, list):
            inputURL = ', '.join(inputURL)
            
        self.cell(0, 10, inputURL, ln=1)  # URL 노란색으로 표시

        self.set_text_color(0, 0, 0)  # 다시 검은색으로 설정
        self.set_font("Arial", 'B', 12)
        self.cell(50, 10, "Selected Vulnerability : ", ln=0)  # 굵게 표시
        
        # 취약점 목록을 문자열로 결합
        vulnerabilities = ', '.join(collectVul)
        self.set_text_color(255, 0, 0)  # 빨간색 설정
        self.cell(0, 10, vulnerabilities, ln=1)  # 수정된 부분: 모든 취약점을 한 줄로 출력
        '''
        for idx, vul in enumerate(collectVul):
            self.set_text_color(255, 0, 0)  # 빨간색 설정
            self.cell(29, 10, vul, ln=0 if idx < len(collectVul) - 1 else 1)  # 취약점을 셀에 배치
        '''

        self.set_text_color(0, 0, 0)  # 텍스트 색상 다시 검은색으로 설정

# PDF 파일을 생성하는 함수
def create_pdf(filename, inputURL, collectVul, RXSS=[], SXSS=[], DXSS=[], NSQL=[], BSQL=[]):
    pdf = PDF()  # PDF 객체 생성
    pdf.add_page()  # 새로운 페이지 추가
    pdf.set_dynamic_content(inputURL, collectVul)  # 동적 내용 설정

    # 보고서 생성 시간 추가
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    pdf.set_font("Arial", 'I', 10)
    pdf.cell(0, 10, f"Report Creation Time: {current_time}", ln=1)
    
    # 윗 부분 검은색 선 추가
    pdf.draw_black_line()

    # 취약점 발견 페이지 섹션
    pdf.chapter_title('Vulnerability Discovery Page')
    
    # 취약점별 링크들
    vulnerabilities_links = {
        "Reflected XSS": RXSS,
        "Stored XSS": SXSS,
        "DOM XSS": DXSS,
        "Normal SQLi": NSQL,
        "Blind SQLi": BSQL
    }

    for vul in collectVul:
        if vul in vulnerabilities_links and vulnerabilities_links[vul]:
            pdf.chapter_body(vul, vulnerabilities_links[vul])

    # 검은색 선 추가
    pdf.draw_black_line()

    # Solution 링크 섹션 -> 해당 섹션에는 후에 가이드라인 및 대응법을 안내해주는 링크로 바꿔서 작성해야함
    solutions = {
        "Reflected XSS": 'https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html',
        "Stored XSS": 'https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html',
        "DOM XSS": 'https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html',
        "Normal SQLi": 'https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html',
        "Blind SQLi": 'https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html'
    }

    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Solution:', ln=1, border=1)
    pdf.set_font('Arial', '', 10)
    for vul in collectVul:
        if vul in solutions:
            pdf.cell(0, 10, f'{vul}:  {solutions[vul]}', ln=1, border=1)
    
    pdf.output(filename)  # 파일 출력

# # PDF 파일 생성 함수 호출
# inputURL = "https://testwebsite.php" # <- 입력된 도메인 값 외부에서 불러오기
# collectVul = ["Stored XSS", "Normal SQLi", "Blind SQLi"] # <- 선택한 취약점 종류 값 외부에서 불러오기
# # ㄴ> 5가지의 취약점 종류의 이름이 들어가면 인식하며, 특정 취약점 유형을 제외하면 해당하는 유형의 리스트는 제외됨.

# # 외부에서 취약점 링크들을 할당 -> 이는 외부에서 처리한 주소들의 배열을 값으로 가져와 할당해주면 됨.
# # 현재 할당되어있는 링크들은 예시로 구성
# RXSS = ['https://reflectedxss1.php', 'https://reflectedxss2.php']
# SXSS = ['https://storedxss1.php', 'https://storedxss2.php']
# DXSS = []  # 값을 못 받아오는 경우 빈 리스트로 설정하기 -> 테스트를 위해 일부로 비워뒀기 때문에 해당 유형의 리스트는 출력 제외됨.
# NSQL = ['https://normalsqli1.php', 'https://normalsqli2.php']
# BSQL = ['https://blindsqli1.php', 'https://blindsqli2.php']

# create_pdf("XSAS Results Report.pdf", inputURL, collectVul, RXSS, SXSS, DXSS, NSQL, BSQL) 
# # ㄴ> 생성 경로 바탕화면으로 디폴트값 되어있음. 수정해주기

