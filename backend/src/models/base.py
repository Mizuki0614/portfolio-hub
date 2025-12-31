"""ベースモデルクラス"""

from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field


class BaseEntity(BaseModel):
    """ベースエンティティクラス"""
    
    id: UUID = Field(default_factory=uuid4, description="一意識別子")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="作成日時")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="更新日時")
    
    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat(),
            UUID: lambda v: str(v)
        }


class BaseRequest(BaseModel):
    """ベースリクエストクラス"""
    
    class Config:
        from_attributes = True


class BaseResponse(BaseModel):
    """ベースレスポンスクラス"""
    
    success: bool = True
    message: Optional[str] = None
    
    class Config:
        from_attributes = True