import whisper
import torch

def transcribe(file_path: str, model_name="base") -> str:
    """
    Transcribe input audio file using Whisper.
    """
    try:
        # Определение устройства: использовать GPU если доступно, иначе CPU
        device = "cuda" if torch.cuda.is_available() else "cpu"

        # Загрузка модели Whisper на соответствующее устройство
        model = whisper.load_model(model_name, device=device)

        # Распознавание аудио
        result = model.transcribe(file_path)
        return result["text"]
    except Exception as e:
        print(f"Error during transcription: {e}")
        return ""