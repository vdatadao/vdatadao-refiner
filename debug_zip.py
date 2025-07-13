import zipfile

def debug_zip_structure(zip_path):
    with zipfile.ZipFile(zip_path, "r") as archive:
        print("=== ZIP İçeriği ===")
        for file_name in archive.namelist():
            print(file_name)
        
        print(f"
=== Toplam Dosya Sayısı: {len(archive.namelist())} ===")

if __name__ == "__main__":
    debug_zip_structure("instagram-dr.ayglelts-2025-07-03-Xhx3F5GM-20250705T144855Z-1-001.zip")
