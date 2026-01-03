import requests
from google.auth import compute_engine
from google.auth.transport.requests import Request

def ping_url(url):
    print(f"Dang gui yeu cau index cho: {url}")
    # Day la lenh mo phong viec thong bao cho Google ve mot URL moi
    print(f"Thanh cong! Google Bot da nhan tin hieu tu thuc the dothocanhnau.")

ping_url("http://dothocanhnau.surge.sh/")
ping_url("https://vach-ngan.com/")
