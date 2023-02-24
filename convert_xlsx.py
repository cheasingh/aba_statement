import typer
from core import convert_to_hbank_format
from pathlib import Path


app = typer.Typer()


@app.command()
def convertxls(filepath: str,
               app: str = typer.Option(
                   "homebank", help="specify personal finance app"),
               saveto: str = typer.Option(Path.cwd(), help="specify path that the file will save to")):
    if app == "homebank":
        convert_to_hbank_format(path_to_xlsx=filepath, save_path=saveto)

    else:
        print(f"other app is specified {app}")


if __name__ == "__main__":
    app()
