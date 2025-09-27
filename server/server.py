from flask import Flask, request, jsonify
import time
import os
import threading
import socket

app = Flask(__name__)

# 配置
HOST = '0.0.0.0'  # 監聽所有可用的網路介面
PORT = 8888       # Flask 應用程式監聽的埠號

# 這個 Flask 應用程式的 PID
FLASK_PID = os.getpid()

# 簡單的首頁，用於測試正常連接
@app.route('/')
def home():
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] received from {request.remote_addr} '/' request")
    return "Hello from Flask SYN Flood Test Server!"

# 模擬一個耗時的操作，可以觀察其在攻擊下的響應時間變化
@app.route('/slow')
def slow_operation():
    start_time = time.time()
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] received from {request.remote_addr} '/slow' request, starting slow operation...")
    time.sleep(1)  
    end_time = time.time()
    duration = end_time - start_time
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] completed from {request.remote_addr} '/slow' request, took {duration:.2f} seconds")
    return f"Slow operation completed in {duration:.2f} seconds."

# 運行 Flask 應用程式的主函數
def run_flask_app():
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Flask server PID: {FLASK_PID}")
    app.run(host=HOST, port=PORT, debug=False)

if __name__ == '__main__':
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Starting Flask server at {HOST}:{PORT}")
    run_flask_app()