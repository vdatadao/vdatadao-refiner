import os
import sys
sys.path.append('refiner')

from refiner.utils.instagram_parser import parse_instagram_zip
from refiner.transformer.instagram_transformer import InstagramTransformer
from refiner.models.unrefined import InstagramData

def test_instagram_parser():
    print("=== Instagram Parser Test ===")
    
    # ZIP dosyası yolu
    zip_path = "instagram-dr.ayglelts-2025-07-03-Xhx3F5GM-20250705T144855Z-1-001.zip"
    
    if not os.path.exists(zip_path):
        print(f"HATA: {zip_path} dosyası bulunamadı!")
        print("ZIP dosyasını bu klasöre koyun.")
        return
    
    try:
        # Parse Instagram ZIP
        print(f"ZIP dosyası parse ediliyor: {zip_path}")
        data = parse_instagram_zip(zip_path)
        
        print("\n=== Parse Sonuçları ===")
        print(f"Profil: {data['profile']}")
        print(f"Takipçi sayısı: {len(data['followers'])}")
        print(f"Takip edilen sayısı: {len(data['following'])}")
        print(f"Medya sayısı: {data['media_count']}")
        print(f"Hikaye sayısı: {data['stories_count']}")
        print(f"Mesaj sayısı: {data['messages_count']}")
        
        # Model doğrulaması
        print("\n=== Model Doğrulaması ===")
        instagram_data = InstagramData.model_validate(data)
        print("✅ Instagram verisi başarıyla doğrulandı!")
        
        # Transformer test
        print("\n=== Transformer Test ===")
        transformer = InstagramTransformer("test_output.db")
        transformer.process(data)
        print("✅ Transformer başarıyla çalıştı!")
        
        print("\n=== Test Tamamlandı ===")
        print("Instagram parser sistemi başarıyla çalışıyor!")
        
    except Exception as e:
        print(f"HATA: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_instagram_parser() 