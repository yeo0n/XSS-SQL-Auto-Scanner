import re
from urllib.parse import urlparse

# 주어진 JavaScript 코드
script_code = 'match([&]param1=123&param2="abc"&param3=\'xyz\');'

# 정규 표현식
pattern = r'match\([&]([\w]+)=(?:"([^"]*)"|\'([^\']*)\'|([^&"\']+))'

# 정규식을 사용하여 파라미터 추출
matches = re.finditer(pattern, script_code)

# 각 매치에 대해 처리
for match in matches:
    param_name = match.group(1)
    param_value = match.group(2) or match.group(3) or match.group(4)
    print(f"{param_name}, {param_value}")    
    # 여기서 test_xss 함수 호출 등 추가 작업 수행
