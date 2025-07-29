import re

student_id = "725A2001"
first_name = "ichiro"
last_name = "ohtani"


# 入学年を取得
def get_enrollment_year(student_id):
    return f"20{student_id[1:3]}年"


# 学科名を取得
def get_department(student_id):
    match = re.match(r"^.{4}([0-2])", student_id)
    if not match:
        raise ValueError("Invalid student ID")

    department_map = {"0": "情報科学科", "1": "情報社会学科", "2": "行動情報学科"}
    return department_map[match.group(1)]


# メールアドレスを取得
def get_mail_address(student_id, last_name, first_name):
    return f"{last_name}.{first_name}.{student_id[1:3]}@shizuoka.ac.jp"


print(f"入学年: {get_enrollment_year(student_id)}")
print(f"学科名: {get_department(student_id)}")
print(f"メールアドレス: {get_mail_address(student_id, last_name, first_name)}")
