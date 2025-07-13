import zipfile
from bs4 import BeautifulSoup
import re

def parse_instagram_zip(zip_path):
    result = {
        # Temel profil
        "profile": {
            "username": "dr.ayglelts",  # Varsayılan değer
            "full_name": None,
            "email": None,
            "phone_number": None
        },
        
        # Bağlantılar
        "followers": [],
        "following": [],
        "close_friends": [],
        "follow_requests_received": [],
        "synced_contacts": [],
        
        # Medya ve içerik
        "media_count": 0,
        "stories_count": 0,
        "messages_count": 0,
        "liked_posts": [],
        "liked_comments": [],
        "comments": [],
        "saved_posts": [],
        "saved_collections": [],
        
        # Aktivite ve kullanım
        "recent_searches": [],
        "link_history": [],
        "story_interactions": [],
        "subscriptions": [],
        "reports": [],
        
        # Güvenlik ve giriş
        "login_activity": [],
        "password_changes": [],
        "signup_details": None,
        "last_known_location": None,
        
        # Reklam ve ilgi alanları
        "ads_viewed": [],
        "videos_watched": [],
        "ad_preferences": [],
        "recommended_topics": [],
        
        # Cihaz ve teknik
        "devices": [],
        "camera_info": None,
        "autofill_info": None,
        
        # Profil değişiklikleri
        "profile_changes": [],
        "profile_status_changes": [],
        "privacy_changes": [],
        
        # Ayarlar ve tercihler
        "notification_preferences": None,
        "apps_websites_activity": [],
        "story_settings": []
    }
    
    with zipfile.ZipFile(zip_path, 'r') as archive:
        file_list = archive.namelist()
        base_path = "instagram-dr.ayglelts-2025-07-03-Xhx3F5GM"
        
        print(f"ZIP içinde {len(file_list)} dosya bulundu")
        print(f"Base path: {base_path}")
        
        # === MEDYA VE İÇERİK ===
        # Medya sayısı (media/other klasörü)
        try:
            media_files = [name for name in file_list if f'{base_path}/media/other/' in name]
            result["media_count"] = len(media_files)
            print(f"Medya dosyası sayısı: {result['media_count']}")
        except Exception as e:
            print(f"Medya sayma hatası: {e}")
            
        # Hikaye sayısı (media/stories klasörü)
        try:
            story_files = [name for name in file_list if f'{base_path}/media/stories/' in name]
            result["stories_count"] = len(story_files)
            print(f"Hikaye dosyası sayısı: {result['stories_count']}")
        except Exception as e:
            print(f"Hikaye sayma hatası: {e}")
            
        # Mesaj sayısı (messages/inbox klasörü)
        try:
            message_files = [name for name in file_list if f'{base_path}/your_instagram_activity/messages/inbox/' in name and name.endswith('message_1.html')]
            result["messages_count"] = len(message_files)
            print(f"Mesaj dosyası sayısı: {result['messages_count']}")
        except Exception as e:
            print(f"Mesaj sayma hatası: {e}")
            
        # === BAĞLANTILAR ===
        # Takipçiler
        try:
            followers_file = f'{base_path}/connections/followers_and_following/followers_1.html'
            if followers_file in file_list:
                with archive.open(followers_file) as f:
                    soup = BeautifulSoup(f.read(), 'html.parser')
                    result["followers"] = [a.text.strip() for a in soup.find_all('a') if a.text.strip()]
                    print(f"Takipçi sayısı: {len(result['followers'])}")
        except Exception as e:
            print(f"Takipçi okuma hatası: {e}")
            
        # Takip edilenler
        try:
            following_file = f'{base_path}/connections/followers_and_following/following.html'
            if following_file in file_list:
                with archive.open(following_file) as f:
                    soup = BeautifulSoup(f.read(), 'html.parser')
                    result["following"] = [a.text.strip() for a in soup.find_all('a') if a.text.strip()]
                    print(f"Takip edilen sayısı: {len(result['following'])}")
        except Exception as e:
            print(f"Takip edilen okuma hatası: {e}")
            
        # Yakın arkadaşlar
        try:
            close_friends_file = f'{base_path}/connections/followers_and_following/close_friends.html'
            if close_friends_file in file_list:
                with archive.open(close_friends_file) as f:
                    soup = BeautifulSoup(f.read(), 'html.parser')
                    result["close_friends"] = [a.text.strip() for a in soup.find_all('a') if a.text.strip()]
                    print(f"Yakın arkadaş sayısı: {len(result['close_friends'])}")
        except Exception as e:
            print(f"Yakın arkadaş okuma hatası: {e}")
            
        # === BEĞENİLER VE YORUMLAR ===
        # Beğenilen gönderiler
        try:
            liked_posts_file = f'{base_path}/your_instagram_activity/likes/liked_posts.html'
            if liked_posts_file in file_list:
                with archive.open(liked_posts_file) as f:
                    soup = BeautifulSoup(f.read(), 'html.parser')
                    result["liked_posts"] = [a.text.strip() for a in soup.find_all('a') if a.text.strip()]
                    print(f"Beğenilen gönderi sayısı: {len(result['liked_posts'])}")
        except Exception as e:
            print(f"Beğenilen gönderi okuma hatası: {e}")
            
        # Beğenilen yorumlar
        try:
            liked_comments_file = f'{base_path}/your_instagram_activity/likes/liked_comments.html'
            if liked_comments_file in file_list:
                with archive.open(liked_comments_file) as f:
                    soup = BeautifulSoup(f.read(), 'html.parser')
                    result["liked_comments"] = [a.text.strip() for a in soup.find_all('a') if a.text.strip()]
                    print(f"Beğenilen yorum sayısı: {len(result['liked_comments'])}")
        except Exception as e:
            print(f"Beğenilen yorum okuma hatası: {e}")
            
        # === KAYDEDİLENLER ===
        # Kaydedilen gönderiler
        try:
            saved_posts_file = f'{base_path}/your_instagram_activity/saved/saved_posts.html'
            if saved_posts_file in file_list:
                with archive.open(saved_posts_file) as f:
                    soup = BeautifulSoup(f.read(), 'html.parser')
                    result["saved_posts"] = [a.text.strip() for a in soup.find_all('a') if a.text.strip()]
                    print(f"Kaydedilen gönderi sayısı: {len(result['saved_posts'])}")
        except Exception as e:
            print(f"Kaydedilen gönderi okuma hatası: {e}")
            
        # Kaydedilen koleksiyonlar
        try:
            saved_collections_file = f'{base_path}/your_instagram_activity/saved/saved_collections.html'
            if saved_collections_file in file_list:
                with archive.open(saved_collections_file) as f:
                    soup = BeautifulSoup(f.read(), 'html.parser')
                    result["saved_collections"] = [a.text.strip() for a in soup.find_all('a') if a.text.strip()]
                    print(f"Kaydedilen koleksiyon sayısı: {len(result['saved_collections'])}")
        except Exception as e:
            print(f"Kaydedilen koleksiyon okuma hatası: {e}")
    
    return result 