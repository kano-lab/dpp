import pandas as pd


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


input_df = pd.read_csv("./data/student_info.csv")
columns = ["mail_address", "department"]
output_df = pd.DataFrame(columns=columns)
records = []

for row in input_df.itertuples():
    student_id = row.student_id
    last_name = row.last_name
    first_name = row.first_name
    records.append(
        {
            "mail_address": get_mail_address(student_id, last_name, first_name),
            "department": get_department(student_id),
        }
    )
output_df = pd.DataFrame(records)
output_df.to_csv("./data/student_info_output.csv", index=False)
