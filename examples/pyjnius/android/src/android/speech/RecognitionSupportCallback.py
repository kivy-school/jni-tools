from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RecognitionSupportCallback"]

class RecognitionSupportCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/speech/RecognitionSupportCallback"
    onSupportResult = JavaMethod("(Landroid/speech/RecognitionSupport;)V")
    onError = JavaMethod("(I)V")