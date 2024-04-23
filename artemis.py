import os
import pandas as pd
import torch
import torchvision
from torchtext.data.utils import get_tokenizer
from torchtext.vocab import vocab as Vocab
from collections import Counter
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import DataLoader
from torchvision import transforms
from torch.nn.utils.rnn import pad_sequence
from PIL import Image


def create_df(image_dir, csv_path):
    df = pd.read_csv(csv_path)
    #Columna con ruta de img
    df['image_path'] = df['painting'].apply(lambda _: os.path.join(image_dir, _) + '.jpg')
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

def create_vocab(df):
    tokenizer = get_tokenizer('basic_english')
    counter = Counter()
    for desc in df['utterance']:
        counter.update(tokenizer(desc))
    return Vocab(counter, specials=['<unk>', '<pad>', '<bos>', '<eos>']), tokenizer

def data_process(df, vocab, tokenizer):
    data = []
    for x, y in zip(df['image_path'], df['utterance']):
        tensor_ = torch.tensor(
            [vocab[token] for token in tokenizer(y)],
            dtype=torch.long
        )
        data.append((x, tensor_))
    return data

def generate_batch(data_batch):
    transform = transforms.Compose([
            transforms.Resize((128, 128)),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor()
    ])

    x, y = [], []
    for (x_item, y_item) in data_batch:
        image = Image.open(x_item).convert('RGB')
        image = transform(image)
        x.append(image)
        y.append(
            torch.cat([
                torch.tensor([BOS_IDX]),
                y_item,
                torch.tensor([EOS_IDX])
            ], dim=0)
        )

    x = torch.stack(x)
    y = pad_sequence(y, batch_first=True, padding_value=PAD_IDX)
    return x, y[:, :-1], y[:, 1:]

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
    print(train_df['image_path'].iloc[0])

    # Create vocab
    vocab, tokenizer = create_vocab(pd.concat([train_df, val_df]))
    vocab.set_default_index(0) # fix <ukn>
    vocab_size = len(vocab)
    print(vocab_size)

    PAD_IDX = vocab['<pad>']
    BOS_IDX = vocab['<bos>']
    EOS_IDX = vocab['<eos>']

    # Create tensor
    train_data = data_process(train_df, vocab, tokenizer)
    val_data = data_process(val_df, vocab, tokenizer)
    print(len(train_data))
    print(len(val_data))

    # Create batches and append imgs
    train_loader = DataLoader(train_data, batch_size=64,
                    shuffle=True, collate_fn=generate_batch,
                    num_workers=4, pin_memory=True)
    val_loader = DataLoader(val_data, batch_size=64,
                    shuffle=False, collate_fn=generate_batch,
                    num_workers=4, pin_memory=True)


    enc_batch, dec_batch, target_batch = next(iter(val_loader))
    print(f'{enc_batch.shape}, {dec_batch.shape}, {target_batch.shape}')
