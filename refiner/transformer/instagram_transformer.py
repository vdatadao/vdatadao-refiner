from typing import Dict, Any, List
from refiner.models.refined import Base
from refiner.transformer.base_transformer import DataTransformer
from refiner.models.unrefined import InstagramData

class InstagramTransformer(DataTransformer):
    """
    Transformer for Instagram data extracted from ZIP archives.
    """
    
    def transform(self, data: Dict[str, Any]) -> List[Base]:
        """
        Transform Instagram data into SQLAlchemy model instances.
        
        Args:
            data: Dictionary containing Instagram data from parser
            
        Returns:
            List of SQLAlchemy model instances
        """
        # Validate data with Pydantic
        unrefined_instagram = InstagramData.model_validate(data)
        
        print(f"Instagram verisi doğrulandı:")
        print(f"- Kullanıcı: {unrefined_instagram.profile.username}")
        print(f"- Takipçi: {len(unrefined_instagram.followers)}")
        print(f"- Takip edilen: {len(unrefined_instagram.following)}")
        print(f"- Medya: {unrefined_instagram.media_count}")
        print(f"- Hikaye: {unrefined_instagram.stories_count}")
        print(f"- Mesaj: {unrefined_instagram.messages_count}")
        
        # For now, return empty list since we haven't created refined models yet
        # In the future, you can create InstagramRefined models here
        models = []
        
        return models 