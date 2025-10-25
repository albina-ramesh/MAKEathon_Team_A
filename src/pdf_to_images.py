# src/pdf_to_images.py
from pathlib import Path
from pdf2image import convert_from_path

# Windows: Poppler installieren und diesen Pfad anpassen (z.B. r"C:\poppler\Library\bin")
POPPLER_PATH = None  # setze auf Pfad-String, falls nötig

def pdf_to_images(pdf_path: str, out_dir: str, dpi: int = 300, poppler_path: str | None = POPPLER_PATH):
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    pages = convert_from_path(pdf_path, dpi=dpi, poppler_path=poppler_path)
    saved = []
    for i, p in enumerate(pages):
        out_path = out / f"{Path(pdf_path).stem}_p{i:03d}.png"
        p.save(out_path)
        saved.append(str(out_path))
    return saved

if __name__ == "__main__":
    # Beispiel: eine PDF aus deinem Dataset konvertieren
    pdf = r"Dataset Ic-Ss Platform\MAKEathon Ic-Ss Platform.pdf"  # Pfad anpassen, wenn andere Datei
    imgs = pdf_to_images(pdf, r"data\pages", dpi=300)
    print(f"Gespeichert: {len(imgs)} Seiten in data\\pages")