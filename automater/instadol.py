import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube, Playlist
import instaloader
import os

# --- Download Functions ---

def download_youtube(url, output_path):
    try:
        if 'playlist' in url:
            pl = Playlist(url)
            for video_url in pl.video_urls:
                yt = YouTube(video_url)
                yt.streams.get_highest_resolution().download(output_path)
                log(f"✅ Downloaded: {yt.title}")
        else:
            yt = YouTube(url)
            yt.streams.get_highest_resolution().download(output_path)
            log(f"✅ Downloaded: {yt.title}")
    except Exception as e:
        log(f"❌ YouTube Error: {e}")

def download_instagram(url, output_path):
    try:
        loader = instaloader.Instaloader(dirname_pattern=output_path, save_metadata=False)
        shortcode = url.strip('/').split("/")[-1]
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        loader.download_post(post, target="insta_content")
        log(f"✅ Downloaded Instagram post: {shortcode}")
    except Exception as e:
        log(f"❌ Instagram Error: {e}")

def detect_platform(url):
    if "youtube.com" in url or "youtu.be" in url:
        return "youtube"
    elif "instagram.com" in url:
        return "instagram"
    else:
        return "unknown"

# --- GUI Functions ---

def log(message):
    output_box.insert(tk.END, message + "\n")
    output_box.see(tk.END)

def process_url(url, output_dir):
    platform = detect_platform(url)
    if platform == "youtube":
        download_youtube(url, output_dir)
    elif platform == "instagram":
        download_instagram(url, output_dir)
    else:
        log(f"❓ Unknown platform: {url}")

def handle_links(urls):
    output_dir = filedialog.askdirectory(title="Select Output Folder")
    if not output_dir:
        return
    for url in urls:
        if url.strip():
            process_url(url.strip(), output_dir)

def paste_link():
    url = url_entry.get().strip()
    if url:
        handle_links([url])
    else:
        messagebox.showinfo("Info", "Please paste a link first.")

def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as f:
            links = [line.strip() for line in f if line.strip()]
        handle_links(links)

# --- Build GUI ---

root = tk.Tk()
root.title("Instagram & YouTube Video Downloader")
root.geometry("600x400")
root.resizable(False, False)

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

tk.Label(frame, text="Paste a YouTube or Instagram link:").pack()
url_entry = tk.Entry(frame, width=80)
url_entry.pack(pady=5)

btn_frame = tk.Frame(frame)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="📥 Download Link", command=paste_link).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="📄 Load URLs from File", command=upload_file).pack(side=tk.LEFT, padx=5)

output_box = tk.Text(frame, height=15, wrap=tk.WORD)
output_box.pack(pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
