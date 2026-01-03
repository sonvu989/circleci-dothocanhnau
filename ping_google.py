import requests

def ping():
    sitemap_url = "https://sonvu989.github.io/circleci-dothocanhnau/sitemap.xml"
    google_ping = f"https://www.google.com/ping?sitemap={sitemap_url}"
    try:
        r = requests.get(google_ping)
        if r.status_code == 200:
            print("Chuc mung nghe nhan! Google da nhan tin hieu 'Tầm nhiệt'.")
    except:
        print("Loi ket noi, nghe nhan hay kiem tra lai mang.")

if __name__ == "__main__":
    ping()
