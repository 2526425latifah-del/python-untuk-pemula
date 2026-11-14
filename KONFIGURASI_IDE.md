# Konfigurasi Environment dan IDE

Modul membahas PyCharm. Pengerjaan proyek ini dilakukan di WSL2 Arch Linux, jadi environment memakai venv dan editor yang terpasang di Arch (VS Code dan Neovim).

## Langkah

1. Buat virtual environment: python -m venv venv
2. Aktifkan: source venv/bin/activate
3. Pasang paket: pip install camelcase
4. Pilih interpreter venv/bin/python di editor (lihat .vscode/settings.json)

## Catatan

PyCharm tidak dipasang di lingkungan ini. Folder venv tidak ikut Git karena ada di .gitignore.
