import pandas as pd, os, time, joblib
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

def preprocess(in_csv: str, out_dir="data/processed"):
    os.makedirs(out_dir, exist_ok=True)
    df = pd.read_csv(in_csv).sort_values("date")
    features = [c for c in df.columns if c not in ["date","target"]]
    y = df["target"].values
    pipe = Pipeline([("imp", SimpleImputer(strategy="median")),
                     ("sc", StandardScaler())])
    ct = ColumnTransformer([("num", pipe, features)], remainder="drop")
    X_t = ct.fit_transform(df[features])
    os.makedirs("models", exist_ok=True)
    joblib.dump(ct, "models/preprocess_ct.joblib")
    X_path = os.path.join(out_dir, f"X_{int(time.time())}.pkl")
    y_path = os.path.join(out_dir, f"y_{int(time.time())}.pkl")
    joblib.dump(X_t, X_path)
    joblib.dump(y, y_path)
    print(X_path, y_path)

if __name__ == "__main__":
    import sys; preprocess(sys.argv[1])
