import webview
import os

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(current_dir, 'index.html')
    
    # pywebview 조종기 창 열기
    window = webview.create_window('Autocar Dashboard', html_path, width=1024, height=768)
    webview.start(debug=True)