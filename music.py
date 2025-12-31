# Импорт библиотек / Import libraries
import os
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC


def prepare_mp3(mp3_path: str, title: str, artist: str, cover_path: str = None, genre: str = None):
    # Проверка существования файла / Check if file exists
    if not os.path.isfile(mp3_path):
        raise FileNotFoundError("MP3 файл не найден / MP3 file not found")

    # Получаем директорию файла / Get file directory
    folder = os.path.dirname(mp3_path) or "."

    # Формируем новое имя файла / Create new filename
    # В Telegram используются метаданные из ID3, а не имя файла /
    # Telegram uses ID3 metadata, not filename
    safe_name = f"{title}.mp3"
    new_path = os.path.join(folder, safe_name)

    # Переименовываем файл / Rename file
    if mp3_path != new_path:
        os.rename(mp3_path, new_path)

    # Открываем файл для работы с тегами / Open file for tag editing
    audio = MP3(new_path, ID3=EasyID3)
    
    # Добавляем теги, если их нет / Add tags if missing
    try:
        audio.add_tags()
    except Exception:
        pass

    # Устанавливаем метаданные / Set metadata
    audio["title"] = title
    audio["artist"] = artist
    if genre:
        audio["genre"] = genre
    
    # Сохраняем изменения / Save changes
    audio.save()
    
    # Добавление обложки / Add cover art
    if cover_path:
        if not os.path.isfile(cover_path):
            print(f"Предупреждение: Файл обложки не найден / Warning: Cover file not found: {cover_path}")
        else:
            # Используем полный ID3 для обложки / Use full ID3 for cover art
            audio_id3 = MP3(new_path, ID3=ID3)
            
            try:
                audio_id3.add_tags()
            except Exception:
                pass
            
            # Определяем MIME-тип изображения / Determine image MIME type
            cover_ext = os.path.splitext(cover_path)[1].lower()
            mime_types = {
                '.jpg': 'image/jpeg',
                '.jpeg': 'image/jpeg',
                '.png': 'image/png',
                '.gif': 'image/gif',
                '.bmp': 'image/bmp'
            }
            mime_type = mime_types.get(cover_ext, 'image/jpeg')
            
            # Читаем изображение / Read image
            with open(cover_path, 'rb') as cover_file:
                cover_data = cover_file.read()
            
            # Добавляем обложку в теги / Add cover to tags
            audio_id3.tags.add(APIC(
                encoding=3,  # UTF-8
                mime=mime_type,
                type=3,  # Cover / Обложка
                desc='Cover',
                data=cover_data
            ))
            
            audio_id3.save()
            print(f"Обложка добавлена / Cover added: {cover_path}")

    # Результат / Result
    print("Готово / Done:")
    print(f"Файл / File: {new_path}")
    print(f"Теги / Tags: {artist} — {title}")

# Укажите путь к вашему MP3 файлу / Specify path to your MP3 file
mp3_path = r"введите путь к mp3 файлу"

# Название трека / Track title
title = "введите название"

# Имя исполнителя / Artist name
artist = "введите артиста"

# Жанр (Pop, Rock, Hip-Hop и т.д.) / Genre (Pop, Rock, Hip-Hop, etc.)
genre = "введите жанр"

# Путь к обложке (укажите None, если обложки нет) / 
# Path to cover (set None if no cover)
cover_path = r"введите путь к обложке"
# cover_path = None  # Раскомментируйте, если обложки нет / Uncomment if no cover

# Запуск обработки / Run processing
prepare_mp3(mp3_path, title, artist, cover_path, genre)
