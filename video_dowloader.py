import yt_dlp

url = "https://www.youtube.com/watch?v=sHecjjm4vyQ&list=RDsHecjjm4vyQ&index=1&pp=8AUB"
output_path = r"C:\Users\Sumbul\OneDrive\Desktop\Cooding Files"

ydl_opts = {"outtmpl": f"{output_path}/%(title)s.%(ext)s"}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download complete!")



