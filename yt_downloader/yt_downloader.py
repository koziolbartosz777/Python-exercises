from pytubefix import YouTube 

url = input("Enter video URL you want to be downloaded: ")

yt = YouTube(url)

print("Title: ", yt.title)
print("Length: ", yt.length, "seconds")

video_download = yt.streams.get_highest_resolution()

print("Downloading...")

video_download.download(output_path="C:\\Users\\bkozi\\Desktop\\Nauka\\PYTHON BARTEK\\yt_downloader\\Pobrane filmy")

print("Download completed")