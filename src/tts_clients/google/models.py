from pydantic import BaseModel


class TextToAudioRequest(BaseModel):
    text: str
    instructions: str
    voice_name: str = "Kore"


class TextToAudioResponse(BaseModel):
    audio: bytes

