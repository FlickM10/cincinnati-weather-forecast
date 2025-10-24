import subprocess, os, typer
app = typer.Typer()

@app.command()
def run_all(in_csv: str):
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/interim", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)
    raw_out = subprocess.check_output(["python","src/ingest.py",in_csv]).decode().strip()
    lag_out = subprocess.check_output(["python","src/features.py",raw_out]).decode().strip()
    Xy = subprocess.check_output(["python","src/preprocess.py",lag_out]).decode().split()
    subprocess.check_call(["python","src/train.py",Xy[0],Xy[1]])

if __name__ == "__main__":
    app()
