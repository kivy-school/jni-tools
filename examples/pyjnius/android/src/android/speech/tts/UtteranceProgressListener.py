from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UtteranceProgressListener"]

class UtteranceProgressListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/speech/tts/UtteranceProgressListener"
    __javaconstructor__ = [("()V", False)]
    onAudioAvailable = JavaMethod("(Ljava/lang/String;[B)V")
    onBeginSynthesis = JavaMethod("(Ljava/lang/String;III)V")
    onDone = JavaMethod("(Ljava/lang/String;)V")
    onError = JavaMultipleMethod([("(Ljava/lang/String;I)V", False, False), ("(Ljava/lang/String;)V", False, False)])
    onRangeStart = JavaMethod("(Ljava/lang/String;III)V")
    onStop = JavaMethod("(Ljava/lang/String;Z)V")
    onStart = JavaMethod("(Ljava/lang/String;)V")