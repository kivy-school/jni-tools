from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RecognitionListener"]

class RecognitionListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/speech/RecognitionListener"
    onReadyForSpeech = JavaMethod("(Landroid/os/Bundle;)V")
    onBeginningOfSpeech = JavaMethod("()V")
    onRmsChanged = JavaMethod("(F)V")
    onBufferReceived = JavaMethod("([B)V")
    onEndOfSpeech = JavaMethod("()V")
    onError = JavaMethod("(I)V")
    onResults = JavaMethod("(Landroid/os/Bundle;)V")
    onPartialResults = JavaMethod("(Landroid/os/Bundle;)V")
    onSegmentResults = JavaMethod("(Landroid/os/Bundle;)V")
    onEndOfSegmentedSession = JavaMethod("()V")
    onLanguageDetection = JavaMethod("(Landroid/os/Bundle;)V")
    onEvent = JavaMethod("(ILandroid/os/Bundle;)V")