import uuid
from collections.abc import Generator
from typing import Any

import azure.cognitiveservices.speech as speechsdk
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class EdgeTtsTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        # 1. 从运行时获取凭证
        try:
            speech_key = self.runtime.credentials["speech_key"]
        except KeyError:
            raise Exception("Telegraph Access Token 未配置或无效。请在插件设置中提供。")

        try:
            service_region = self.runtime.credentials["service_region"]
        except KeyError:
            raise Exception("service_region 未配置或无效。请在插件设置中提供。")

        # 2. 获取工具输入参数
        voice_name = tool_parameters.get("voice_name")
        text = tool_parameters.get("text")

        if not voice_name:
            raise Exception("语音名称不能为空。")

        if not text:
            raise Exception("文字内容不能为空。")

        # 3. 调用库执行操作
        try:
            voice_path = tts(speech_key, service_region, text, voice_name)
            with open(voice_path, "rb") as f:
                audio_bytes = f.read()
            yield self.create_blob_message(audio_bytes, meta = {"mime_type": "audio/wav", "filename": voice_path})
        except Exception as e:
            # 如果库调用失败，抛出异常
            raise Exception(f"调用 Edge TTS 失败: {e}")


def tts(speech_key: str, service_region: str, text: str, voice_name: str = 'zh-CN-XiaohanNeural') -> str | None:
    speech_config = speechsdk.SpeechConfig(subscription = speech_key, region = service_region)
    # Note: the voice setting will not overwrite the voice element in input SSML.
    speech_config.speech_synthesis_voice_name = voice_name

    # 指定输出音频文件的路径
    audio_filename = uuid.uuid4().__str__() + ".wav"
    audio_config = speechsdk.audio.AudioOutputConfig(filename = audio_filename)

    # use the default speaker as audio output.
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config = speech_config, audio_config = audio_config)

    result = speech_synthesizer.speak_text_async(text).get()

    # 检查结果
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print(f"语音合成成功，音频已保存至：{audio_filename}")
        return audio_filename
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print(f"语音合成被取消：{cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print(f"错误详情：{cancellation_details.error_details}")
    return None
