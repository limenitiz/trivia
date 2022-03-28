type_work = [
    "feature",
    "refactor",
    "test",
    "docs",
    "fix",
    "cleanup"
]

print("\n\n")
print("""Type work :
    1 : feature  : добавление функционала
    2 : refactor : рефакторинг
    3 : test     : добавление / исправление тестов
    4 : docs     : добалление / исправление документации
    5 : fix      : исправление ошибок
    6 : cleanup  : чистка
""")

input_type_work = int(input("Type work (int) : ")) - 1
module_name = str(input("Module name : ")).strip()
commit_message = str(input("Commit message : ")).strip()

print("\n")
print(f'{type_work[input_type_work]} : [{module_name}] {commit_message}')
print("\n\n")
