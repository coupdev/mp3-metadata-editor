<div align="center">

# 🎵 MP3 Metadata Editor

</div>

<div align="center">
<p>
<a href="https://coupdev.com/"><img src="https://img.shields.io/badge/Author-Coupdev-89b4fa?style=for-the-badge&logo=github&logoColor=white&labelColor=302D41" alt="Author"></a>&nbsp;&nbsp;
<a href="https://github.com/coupdev/mp3-metadata-editor/blob/main/LICENSE"><img src="https://img.shields.io/github/license/coupdev/mp3-metadata-editor?style=for-the-badge&logo=opensourceinitiative&color=CBA6F7&logoColor=CBA6F7&labelColor=302D41" alt="License"></a>&nbsp;&nbsp;
<a href="https://github.com/coupdev/mp3-metadata-editor/"><img src="https://img.shields.io/badge/Python-3.6+-blue?style=for-the-badge&logo=python&logoColor=yellow&labelColor=302D41" alt="Python"></a>&nbsp;&nbsp;
<a href="https://github.com/coupdev/mp3-metadata-editor/"><img src="https://img.shields.io/badge/Mutagen-Latest-4DABF7?style=for-the-badge&logo=python&logoColor=white&labelColor=302D41" alt="Mutagen"></a>&nbsp;&nbsp;
</p>
</div>

A Python script for editing MP3 file metadata: renaming, adding ID3 tags (title, artist, genre) and cover art. Perfect for preparing music files for Telegram.

---

## 🚀 Features

* ✨ Rename MP3 files automatically
* 🏷️ Add ID3 metadata tags (title, artist, genre)
* 🖼️ Embed cover art (JPG, PNG, GIF, BMP)
* 📱 Optimized for Telegram (uses ID3 metadata, not filename)
* 🔧 Simple configuration in code

---

## 📸 Preview

<div align="center">

| Before | After |
|:------:|:-----:|
| <img src="images/before.PNG" width="400" alt="Before"> | <img src="images/after.PNG" width="400" alt="After"> |

</div>

---

## 🧰 Tech Stack

* **Python 3.6+**
* **mutagen** — MP3 metadata editing library
* **os** — File system operations

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/coupdev/mp3-metadata-editor.git
cd mp3-metadata-editor
```

### 2. Install dependencies

```bash
pip install mutagen
```

### 3. Configure the script

Open `music.py` and edit the configuration section at the bottom:

```python
mp3_path = r"your_track.mp3"
title = "Track Title"
artist = "Artist Name"
genre = "Pop"
cover_path = r"cover.jpg"  # or None
```

### 4. Run the script

```bash
python music.py
```

---

## 💬 Usage

### Basic usage

1. Edit the configuration in `music.py`:
   - `mp3_path` — path to your MP3 file
   - `title` — track title
   - `artist` — artist name
   - `genre` — genre (Pop, Rock, Hip-Hop, etc.)
   - `cover_path` — path to cover image (or `None`)

2. Run the script:
   ```bash
   python music.py
   ```

### Example

```python
mp3_path = r"my_track.mp3"
title = "нету интернетов"
artist = "Леша Кореш"
genre = "Pop"
cover_path = r"cover.jpg"

prepare_mp3(mp3_path, title, artist, cover_path, genre)
```

### Notes

* File will be renamed to `title.mp3` format
* Telegram uses ID3 metadata, not filename
* Cover is optional — set `cover_path = None` if you don't have one

---

## 📄 License

MIT
