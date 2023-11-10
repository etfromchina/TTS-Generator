from flask import Blueprint, render_template, request, session, url_for, redirect
from .tts.tts_service import generate_speech
import os

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    error_message = None
    speech_file_path = None
    api_key = session.get('api_key', '')
    text = session.get('text', '')

    if request.method == 'POST':
        # ... 省略其他 POST 请求处理 ...
        # 从表单获取数据
        text = request.form.get('text')
        voice = request.form.get('voice')
        api_key = request.form.get('api_key')
        remember = request.form.get('remember_api_key')
        clear_api_key = request.form.get('clear_api_key')
        # 如果用户选择记住 API 密钥，则将其存储在 session 中
        if remember:
            session['api_key'] = api_key
        elif clear_api_key:
            session.pop('api_key', None)
            api_key = ''
            remember = ''
        # 保存音色选择
        session['voice'] = voice
        session['text'] = text

        # 检查 API 密钥是否已输入
        if not api_key:
            error_message = "请输入正确的 OpenAI API 密钥。"
        else:
            try:
                # 调用 TTS 服务生成语音
                speech_file_path = generate_speech(api_key, text, voice)
            except Exception as e:
                error_message = f"生成语音时出错: {str(e)}"

    # 获取当前或默认音色
    selected_voice = session.get('voice', 'alloy')  # 默认值为 'alloy'

    # 传递 selected_voice 到模板
    return render_template('index.html', speech_file_path=speech_file_path, api_key=api_key, error_message=error_message, text=text, selected_voice=selected_voice)
