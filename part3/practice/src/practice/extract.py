import json

import pandas as pd


def load_data(path, categories):
    df = pd.read_csv(f"./content/csv/{path}.csv")
    df["label"] = categories["label"]
    df["category"] = categories["category"]
    return df


def load_categories():
    with open("./content/categories.json", "r") as file:
        categories = json.load(file)
    return categories


def save_data(df):
    train_ratio = 0.8
    train_size = int(len(df) * train_ratio)
    valid_size = int(len(df) * (1 - train_ratio) / 2)

    df = df.sample(frac=1, random_state=42)
    train = df[:train_size]
    valid = df[train_size : train_size + valid_size]
    test = df[train_size + valid_size :]
    with open("./content/train.csv", "w") as file:
        train.to_csv(file, index=False)
    with open("./content/valid.csv", "w") as file:
        valid.to_csv(file, index=False)
    with open("./content/test.csv", "w") as file:
        test.to_csv(file, index=False)


def main():
    categories = load_categories()
    print(categories)
    # Load the data
    df = pd.DataFrame()
    for category in categories:
        data = load_data(category["category"], category)
        df = pd.concat([df, data])
    print(df)
    # Save the data
    df = df.reindex(columns=["label", "url", "date", "category", "body"])
    save_data(df)


if __name__ == "__main__":
    main()
