from data import EvenData

def get_user_choice():
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
            print("\n프로그램을 종료합니다.")
            break
        else:
            print("\n잘못된 입력입니다. 화면에 있는 번호를 입력해주세요.")

def display_menu():
    print("\n========================================")
    print("    🛠️ 기계재료 물성치 검색 프로그램")
    print("========================================")
    print("1. 물성치 검색")
    print("2. 공학 단위 변환기")
    print("3. 전체 검색 가능 목록 보기")
    print("4. 프로그램 종료")
    print("----------------------------------------")

def search_material():
    raw_name = input("\n검색할 재료의 이름을 입력하세요: ")
    search_name = raw_name.strip()
    search_name_lower = search_name.lower()

    found_key = None

    for key in EvenData.keys():
        # 데이터베이스의 이름표도 임시로 소문자로 바꿔서 비교합니다.
        if key.lower() == search_name_lower:
            found_key = key  # 모양이 일치하면 원래의 대문자/소문자가 섞인 진짜 이름표를 저장합니다.
            break            # 찾았으니 더 이상 반복문을 돌지 않고 빠져나옵니다.
            
    # 검색 결과 출력
    if found_key:
        print(f"\n--- 🔍 검색 결과: {found_key} ---")
        for k, v in EvenData[found_key].items():
            print(f"* {k}: {v}")
    else:
        print(f"\n⚠️ 안내: '{search_name}' 재료를 찾을 수 없습니다.\n 이름을 확인하시거나 '3. 전체 검색 가능 목록'을 확인해 주세요.")

def display_all_materials():
    print("\n--- 📋 전체 검색 가능 목록 ---")
    # EvenData의 키(재료 이름)만 가져와서 하나씩 출력합니다.
    for name in EvenData.keys():
        print(f"- {name}")

# --- 기능 4 ---
def convert_units():
    print("\n--- 🔄 공학 단위 변환기 ---")
    print("1. 강도 및 응력 (MPa ↔ kpsi)")
    print("2. 길이 (Meter ↔ Inch)")
    print("3. 온도 (°C ↔ °F)")
    
    sub_choice = input("원하시는 변환 메뉴 번호를 선택하세요 (1~3): ").strip()
    
    if sub_choice not in ['1', '2', '3']:
        print("\n🚨 오류 (잘못 기입하셨습니다): 1, 2, 3 중에서 선택해주세요.")
        return
        
    try:
        # float()를 사용하여 소수점 입력도 가능하게 만듭니다.
        val = float(input("\n변환할 숫자(값)를 입력하세요: ").strip())
    except ValueError:
        print("\n🚨 오류 (잘못 기입하셨습니다): 문자가 아닌 숫자로 입력해주세요.")
        return
        
    print("\n--- 🧮 변환 결과 ---")
    
    if sub_choice == '1':
        # 1 kpsi = 6.89476 MPa / 1 MPa = 0.145038 kpsi
        print(f"▶ {val} MPa   =  {val * 0.145038:.2f} kpsi")
        print(f"▶ {val} kpsi  =  {val * 6.89476:.2f} MPa")
        
    elif sub_choice == '2':
        # 1 inch = 0.0254 m / 1 m = 39.3701 inch
        print(f"▶ {val} Meter =  {val * 39.3701:.2f} Inch")
        print(f"▶ {val} Inch  =  {val * 0.0254:.4f} Meter")
        
    elif sub_choice == '3':
        # 섭씨(C) <-> 화씨(F) 변환 공식
        c_to_f = (val * 9/5) + 32
        f_to_c = (val - 32) * 5/9
        print(f"▶ {val} °C    =  {c_to_f:.2f} °F")
        print(f"▶ {val} °F    =  {f_to_c:.2f} °C")