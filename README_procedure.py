
readme_content = """# ⚙️ 기계재료 물성치 검색 및 공학 단위 변환 프로그램

파이썬(Python)을 활용하여 기계재료의 물성치를 검색하고, 자주 사용되는 공학 단위를 변환할 수 있는 콘솔 기반 프로그램입니다. 코드를 기능별로 분리하여 모듈화(`data.py`, `functions.py`, `main.py`)함으로써 유지보수와 데이터 확장이 용이하도록 설계되었습니다.

## 📂 프로젝트 구조

본 프로그램은 동일한 폴더 내에 아래 3개의 파일이 존재해야 정상적으로 작동합니다.

```text
.
├── data.py          # 기계재료 물성치 데이터베이스 (EvenData)
├── functions.py     # 메뉴 표출, 재료 검색, 단위 변환 등 핵심 로직 함수
└── main.py          # 프로그램의 시작점 (Entry Point)

```

---

## 💻 소스 코드 및 구성

### 1. `data.py` (데이터 레이어)

재료의 다양한 물성치 데이터를 딕셔너리 구조로 보관합니다. 새로운 재료(예: Steel, Copper 등)를 추가하고 싶다면 이 파일의 `EvenData`에 간단히 추가할 수 있습니다.

```python
# data.py

# 기계재료 물성치 데이터베이스
EvenData = {
    "Aluminum": {
        "Modulus of Elasticity E (Mpsi)": 10.4,
        "Modulus of Elasticity E (GPa)": 71.7,
        "Modulus of Rigidity G (Mpsi)": 3.9,
        "Modulus of Rigidity G (GPa)": 26.9,
        "Poisson's Ratio": 0.333,
        "Unit Weight w (lbf/in³)": 0.098,
        "Unit Weight w (lbf/ft³)": 169,
        "Unit Weight w (kN/m³)": 26.6
    }
    # 여기에 새로운 재료 데이터를 동일한 형식으로 추가할 수 있습니다.
}

```

### 2. `functions.py` (비즈니스 로직 레이어)

사용자 입력을 처리하고 검색 및 단위 변환을 수행하는 모든 핵심 기능이 구현되어 있습니다. 대소문자 구분 없는 검색 기능과 예외 처리(숫자 오입력 방지)가 포함되어 있습니다.

```python
# functions.py
from data import EvenData

def display_menu():
    \"\"\"메인 메뉴를 화면에 표출합니다.\"\"\"
    print("\\n========================================")
    print("     기계재료 물성치 검색 프로그램")
    print("========================================")
    print("1. 물성치 검색")
    print("2. 공학 단위 변환기")
    print("3. 전체 검색 가능 목록 보기")
    print("4. 프로그램 종료")
    print("----------------------------------------")

def get_user_choice():
    \"\"\"사용자 입력을 받아 해당하는 함수를 호출하는 메인 루프입니다.\"\"\"
    while True:
        display_menu()
        choice = input("원하시는 메뉴 번호를 입력하세요: ")
        
        if choice == '1':
            search_material()
        elif choice == '2':
            convert_units()
        elif choice == '3':
            display_all_materials() 
        elif choice == '4':
            print("\\n프로그램을 종료합니다.")
            break
        else:
            print("\\n잘못된 입력입니다. 화면에 있는 번호를 입력해주세요.")

def search_material():
    \"\"\"입력받은 재료명을 대소문자 구분 없이 데이터베이스에서 검색합니다.\"\"\"
    raw_name = input("\\n검색할 재료의 이름을 입력하세요: ")
    search_name = raw_name.strip()
    search_name_lower = search_name.lower()

    found_key = None

    for key in EvenData.keys():
        if key.lower() == search_name_lower:
            found_key = key
            break            
            
    if found_key:
        print(f"\\n--- 🔍 검색 결과: {found_key} ---")
        for k, v in EvenData[found_key].items():
            print(f"* {k}: {v}")
    else:
        print(f"\\n안내: '{search_name}' 재료를 찾을 수 없습니다.\\n이름을 확인하시거나 '3. 전체 검색 가능 목록'을 확인해 주세요.")

def display_all_materials():
    \"\"\"현재 등록된 모든 재료 목록을 확인합니다.\"\"\"
    print("\\n--- 📋 전체 검색 가능 목록 ---")
    for name in EvenData.keys():
        print(f"- {name}")

def convert_units():
    \"\"\"자주 사용되는 공학 단위(응력, 길이, 온도) 상호 변환을 지원합니다.\"\"\"
    print("\\n--- 🔄 공학 단위 변환기 ---")
    print("1. 강도 및 응력 (MPa ↔ kpsi)")
    print("2. 길이 (Meter ↔ Inch)")
    print("3. 온도 (°C ↔ °F)")
    
    sub_choice = input("원하시는 변환 메뉴 번호를 선택하세요 (1~3): ").strip()
    
    if sub_choice not in ['1', '2', '3']:
        print("\\n 오류: 1, 2, 3 중에서 선택해주세요.")
        return
        
    try:
        val = float(input("\\n변환할 숫자(값)를 입력하세요: ").strip())
    except ValueError:
        print("\\n 오류: 문자가 아닌 숫자로 입력해주세요.")
        return
        
    print("\\n---  변환 결과 ---")
    
    if sub_choice == '1':
        print(f"▶ {val} MPa   =  {val * 0.145038:.2f} kpsi")
        print(f"▶ {val} kpsi  =  {val * 6.89476:.2f} MPa")
    elif sub_choice == '2':
        print(f"▶ {val} Meter =  {val * 39.3701:.2f} Inch")
        print(f"▶ {val} Inch  =  {val * 0.0254:.4f} Meter")
    elif sub_choice == '3':
        c_to_f = (val * 9/5) + 32
        f_to_c = (val - 32) * 5/9
        print(f"▶ {val} °C    =  {c_to_f:.2f} °F")
        print(f"▶ {val} °F    =  {f_to_c:.2f} °C")

```

### 3. `main.py` (실행 진입점)

프로그램을 실행하는 메인 엔트리 포인트 파일입니다. `functions.py`에서 무한 루프 제어 함수를 불러와 구동합니다.

```python
# main.py
from functions import get_user_choice
    
def main():
    get_user_choice() 

if __name__ == "__main__":
    main()

```

---

## 🚀 실행 및 사용 방법

1. **환경 준비**: 컴퓨터에 파이썬(Python 3.x 버전 이상)이 설치되어 있어야 합니다.
2. **파일 저장**: 한 폴더 내에 위의 `data.py`, `functions.py`, `main.py` 코드를 각각 저장합니다.
3. **실행**: 터미널 또는 명령 프롬프트(cmd)를 열고 파일이 있는 경로로 이동한 뒤 아래 명령어를 입력합니다.
```bash
python main.py

```



## 🛠️ 기능 특징

* **대소문자 무시 검색**: 사용자가 `aluminum`이나 `ALUMINUM`으로 입력하더라도 데이터베이스 내의 `Aluminum`을 매칭하여 정확한 물성치를 출력합니다.
* **철저한 예외 처리**: 단위 변환기 이용 시 문자를 입력하면 프로그램이 튕기지 않고 오류 메시지를 띄우며 안전하게 복귀합니다.
* **데이터 확장성**: `data.py` 파일의 딕셔너리 포맷에 맞추어 기계재료 규격(예: 탄소강, 합금강 등)을 자유롭게 누적하여 확장할 수 있습니다.
"""