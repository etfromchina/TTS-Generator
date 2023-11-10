import openai
from pathlib import Path
import os
import time

def generate_speech(api_key, text, voice):
    try:
        # 设置 OpenAI API 密钥
        openai.api_key = api_key

        # 创建语音文件路径
        speech_dir = Path(__file__).parent.parent / "static" / "voices"
        os.makedirs(speech_dir, exist_ok=True)
        speech_file_path = speech_dir / f"speech_{int(time.time())}.mp3"

        # 使用 OpenAI 的 TTS 模型将文本转换为语音
        response = openai.audio.speech.create(
            model="tts-1",
            voice=voice,
            input=text
        )

        # 将语音流保存到文件
        response.stream_to_file(speech_file_path)

        return str(speech_file_path.name)
    except Exception as e:
        raise e
