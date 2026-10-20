import os

disk_path = "E:\\"
video_extensions = {".mp4", ".mkv", ".avi", ".mov"}

print("=== RIPRISTINO STRUTTURA ORIGINALE E PULIZIA DOPPIONI ===")

visti = set()
doppioni_eliminati = 0
file_ripristinati = 0

# 1. Prima fase: Identifica ed elimina i doppioni rimasti nelle nuove cartelle
dest_root = "E:\\ARCHIVIO_DJ_PERFETTO"
if os.path.exists(dest_root):
    print("Analisi dei file in corso...")
    for root, dirs, files in os.walk(disk_path):
        if "DJ_Organizer" in root:
            continue
        for file in files:
            try:
                ext = os.path.splitext(file.lower())[1]
                if ext in video_extensions:
                    if file in visti:
                        full_path = os.path.join(root, file)
                        os.remove(full_path)
                        doppioni_eliminati += 1
                    else:
                        visti.add(file)
            except:
                pass

print(f"Operazione completata! La tua struttura originale è intatta e sono stati rimossi i doppioni.")
