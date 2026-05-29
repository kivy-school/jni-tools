from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextToSpeechService"]

class TextToSpeechService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/speech/tts/TextToSpeechService"
    __javaconstructor__ = [("()V", False)]
    onCreate = JavaMethod("()V")
    onDestroy = JavaMethod("()V")
    onIsLanguageAvailable = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I")
    onGetLanguage = JavaMethod("()[Ljava/lang/String;")
    onLoadLanguage = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I")
    onStop = JavaMethod("()V")
    onSynthesizeText = JavaMethod("(Landroid/speech/tts/SynthesisRequest;Landroid/speech/tts/SynthesisCallback;)V")
    onGetFeaturesForLanguage = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/util/Set;")
    onGetVoices = JavaMethod("()Ljava/util/List;")
    onGetDefaultVoiceNameFor = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")
    onLoadVoice = JavaMethod("(Ljava/lang/String;)I")
    onIsValidVoiceName = JavaMethod("(Ljava/lang/String;)I")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")