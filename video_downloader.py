import streamlit as st
import yt_dlp
import os

st.title("Instagram & YouTube Video Downloader 🎥")

# Input field for video URL
url = st.text_input("Enter Instagram Reel or YouTube Video URL")

if st.button("Download"):
    if url:
        try:
            # Download folder (temporary storage)
            download_folder = "downloads"
            os.makedirs(download_folder, exist_ok=True)

            # yt-dlp options
            ydl_opts = {
                'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
                'format': 'bestvideo+bestaudio/best',
                'merge_output_format': 'mp4',
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',
                }]
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                file_name = ydl.prepare_filename(info_dict)
                final_file = file_name.replace(".webm", ".mp4").replace(".mkv", ".mp4")

            # Read the file as bytes
            with open(final_file, "rb") as file:
                video_bytes = file.read()

            # Provide a download button
            st.download_button(label="Download Video 📥",
                               data=video_bytes,
                               file_name=os.path.basename(final_file),
                               mime="video/mp4")

            st.success("Your video is ready to download!")

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a valid URL!")
