from typing import Optional, List
from pydantic import BaseModel


class Profile(BaseModel):
    name: str
    locale: str

class Storage(BaseModel):
    percentUsed: float

class Metadata(BaseModel):
    source: str
    collectionDate: str
    dataType: str

class User(BaseModel):
    userId: str
    email: str
    timestamp: int
    profile: Profile
    storage: Optional[Storage] = None
    metadata: Optional[Metadata] = None

class InstagramProfile(BaseModel):
    username: str
    full_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None

class InstagramData(BaseModel):
    # Temel profil
    profile: InstagramProfile
    
    # Bağlantılar
    followers: List[str] = []
    following: List[str] = []
    close_friends: List[str] = []
    follow_requests_received: List[str] = []
    synced_contacts: List[str] = []
    
    # Medya ve içerik
    media_count: int = 0
    stories_count: int = 0
    messages_count: int = 0
    liked_posts: List[str] = []
    liked_comments: List[str] = []
    comments: List[str] = []
    saved_posts: List[str] = []
    saved_collections: List[str] = []
    
    # Aktivite ve kullanım
    recent_searches: List[str] = []
    link_history: List[str] = []
    story_interactions: List[str] = []
    subscriptions: List[str] = []
    reports: List[str] = []
    
    # Güvenlik ve giriş
    login_activity: List[str] = []
    password_changes: List[str] = []
    signup_details: Optional[str] = None
    last_known_location: Optional[str] = None
    
    # Reklam ve ilgi alanları
    ads_viewed: List[str] = []
    videos_watched: List[str] = []
    ad_preferences: List[str] = []
    recommended_topics: List[str] = []
    
    # Cihaz ve teknik
    devices: List[str] = []
    camera_info: Optional[str] = None
    autofill_info: Optional[str] = None
    
    # Profil değişiklikleri
    profile_changes: List[str] = []
    profile_status_changes: List[str] = []
    privacy_changes: List[str] = []
    
    # Ayarlar ve tercihler
    notification_preferences: Optional[str] = None
    apps_websites_activity: List[str] = []
    story_settings: List[str] = []