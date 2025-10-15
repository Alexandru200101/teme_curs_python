import pandas as pd
import numpy as np

def f(df):
    dimensiune = df.shape
    tip = df.dtypes
    neexistent = df.isnull().sum()
    return f"df:\n {df}\n \ndimensiune: {dimensiune}\n\ntip:\n {tip}\n\nneexistent:\n {neexistent}"

def read_csv(file_path):
    continut = pd.read_csv(file_path)
    return continut.head(5)

def filtrare(df):
    filtrat = df[(df["Varsta"] > 22)]
    return filtrat[["Nume", "Varsta"]]

def adaugare_col(df):
    df["Note"] = np.random.randint(6, 11, size=len(df))
    return df

def sortare_col(df):
    sorted_df = df.sort_values(by="Varsta", ascending=False)
    return sorted_df

def grupare(df):
    grouped = df.groupby("Oras")["Note"].mean()
    return grouped

def salvare_csv(df, file_path):
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    data = pd.DataFrame({
        "Nume": ["Ana", "Bogdan", "Cristina", "David", "Elena"],
        "Varsta": [20, 22, 21, 23, 20],
        "Oras": ["Iasi", "Bucuresti", "Cluj", "Timisoara", "Brasov"]
    })

    df = pd.DataFrame(data)
    df = adaugare_col(df)
    #print(f(df))
    #print(read_csv("studenti.csv"))
    #print(filtrare(df))
    #print(adaugare_col(df))
    #print(sortare_col(df))
    #print(grupare(df))

    file_path = "studenti_procesati.csv"
    salvare_csv(df, file_path)