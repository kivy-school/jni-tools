from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UtteranceProgressListener"]

class UtteranceProgressListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/speech/tts/UtteranceProgressListener"
    __javaconstructor__ = [("()V", False)]
    onStart = JavaMethod("(Ljava/lang/String;)V")
    onDone = JavaMethod("(Ljava/lang/String;)V")
    onError = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Ljava/lang/String;I)V", False, False)])
    onStop = JavaMethod("(Ljava/lang/String;Z)V")
    onBeginSynthesis = JavaMethod("(Ljava/lang/String;III)V")
    onAudioAvailable = JavaMethod("(Ljava/lang/String;[B)V")
    onRangeStart = JavaMethod("(Ljava/lang/String;III)V")