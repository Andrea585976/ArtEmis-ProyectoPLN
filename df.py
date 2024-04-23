import os
import pandas as pd

def create_df(image_dir, csv_path):
    df = pd.read_csv(csv_path)
    #Columna con ruta de img
    df['image_path'] = df['painting'].apply(lambda _: os.path.join(image_dir, _))
    return df

def format_df(df):
    return df

def split_data(df, train_ratio=0.8, val_ratio=0.2):
    df = df.sample(frac=1).reset_index(drop=True)

    #idx de cada df
    num_samples = len(df)
    num_train = int(train_ratio * num_samples)

    #Split
    train_df = df.iloc[:num_train]
    val_df = df.iloc[num_train:]
    return train_df, val_df

if __name__ == "__main__":
    image_dir = "/home/axel/Desktop/NLP/artemis/img"
    csv_path = "/home/axel/Desktop/NLP/artemis/romanticism_dataset.csv"

    # Create df
    df = create_df(image_dir, csv_path)

    # Format df
    df = format_df(df)

    # Split df
    train_df, val_df = split_data(df)

    print(train_df.head())
