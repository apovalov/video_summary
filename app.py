import os
import re
import streamlit as st
from uuid import uuid4
from src.download import convert_mp4_to_mp3, download_audio, video_title
from src.transcribe import transcribe
from src.summarize import summarize_text


def main():
    st.title("Видео Суммаризатор")

    # Вставьте ссылку на видеоролик в YouTube
    youtube_url = st.text_input("Вставьте ссылку на видеоролик в youtube:")

    # Проверка URL YouTube
    if re.match(r"^https://www.youtube.com/watch\?v=[a-zA-Z0-9_-]*$", youtube_url):
        # Отображение видео
        st.video(youtube_url)

        transcribe_button = st.empty()
        title_placeholder = st.empty()
        progress_placeholder = st.empty()

        if transcribe_button.button("Суммаризировать видео"):
            try:
                transcribe_button.empty()
                title = video_title(youtube_url)
                title_placeholder.title(title)
                progress_placeholder.text("Скачиваю видео...")

                # Создание папки runtimes, если не существует
                if not os.path.exists('runtimes/'):
                    os.makedirs('runtimes/')

                runtime_id = str(uuid4())
                download_path = f"runtimes/{runtime_id}.mp4"

                # Скачивание аудио
                input_file = download_audio(youtube_url, download_path)
                output_file = f"runtimes/{runtime_id}.mp3"

                # Конвертация MP4 в MP3
                convert_mp4_to_mp3(input_file, output_file)

                # Расшифровка
                progress_placeholder.text("Распознавание аудио...")
                transcribed_text = transcribe(output_file)

                # Суммаризация
                progress_placeholder.text("Суммаризация...")
                summary = summarize_text(transcribed_text)
                # print('summary: ', summary)
                st.text_area("Результат", summary, height=300)
            except Exception as e:
                print(e)
                st.error("Ошибка при обработке видео. Пожалуйста, попробуйте еще раз!")
                transcribe_button.empty()
                title_placeholder.empty()
                progress_placeholder.empty()
                st.stop()


            progress_placeholder.empty()


if __name__ == "__main__":
    main()
