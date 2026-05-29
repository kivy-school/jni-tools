from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RecognitionListener"]

class RecognitionListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/speech/RecognitionListener"
    onError = JavaMethod("(I)V")
    onReadyForSpeech = JavaMethod("(Landroid/os/Bundle;)V")
    onPartialResults = JavaMethod("(Landroid/os/Bundle;)V")
    onRmsChanged = JavaMethod("(F)V")
    onResults = JavaMethod("(Landroid/os/Bundle;)V")
    onSegmentResults = JavaMethod("(Landroid/os/Bundle;)V")
    onBufferReceived = JavaMethod("([B)V")
    onEvent = JavaMethod("(ILandroid/os/Bundle;)V")
    onEndOfSpeech = JavaMethod("()V")
    onEndOfSegmentedSession = JavaMethod("()V")
    onLanguageDetection = JavaMethod("(Landroid/os/Bundle;)V")
    onBeginningOfSpeech = JavaMethod("()V")