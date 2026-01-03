import sys

def create_article(title, content):
    filename = title.lower().replace(" ", "-") + ".html"
    path = f"cam-nang/{filename}"
    
    html_template = f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head><meta charset="UTF-8"><title>{title} - Ban Tho Canh Nau</title>
    <style>body {{ font-family: sans-serif; line-height: 1.8; max-width: 800px; margin: auto; padding: 20px; color: #333; }}
    h1 {{ color: #8B0000; border-bottom: 2px solid #8B0000; }}
    .content {{ background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}</style></head>
    <body>
        <h1>{title}</h1>
        <div class="content">{content}</div>
        <p><a href="../index.html">← Ve trang chu</a></p>
    </body>
    </html>
    """
    with open(path, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"Da tao xong bai viet: {path}")

if __name__ == "__main__":
    t = sys.argv[1]
    c = sys.argv[2]
    create_article(t, c)
