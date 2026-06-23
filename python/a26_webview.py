from pathlib import Path


import webview

def main():
    webview.create_window(
        "simple text",
        url=
        (Path(__file__).resolve().parent /
         "text_html").as_uri(),
        height=520,
        resizable=True
        )
    webview.start()

if __name__ == "__main__":
    main()
