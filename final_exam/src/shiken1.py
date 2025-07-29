student_id = "725A2001"
first_name = "ichiro"
last_name = "ohtani"


# 入学年を取得
def get_enrollment_year(student_id):
    return f"20{student_id[1:3]}年"


# 学科名を取得
def get_department(student_id):
    y = student_id[4]
    if y == "0":
        department = "情報科学科"
    elif y == "1":
        department = "情報社会学科"
    elif y == "2":
        department = "行動情報学科"
    else:
        raise ValueError("Invalid student ID")
    return department


# メールアドレスを取得
def get_mail_address(student_id, last_name, first_name):
    return f"{last_name}.{first_name}.{student_id[1:3]}@shizuoka.ac.jp"


print(f"入学年: {get_enrollment_year(student_id)}")
print(f"学科名: {get_department(student_id)}")
print(f"メールアドレス: {get_mail_address(student_id, last_name, first_name)}")
