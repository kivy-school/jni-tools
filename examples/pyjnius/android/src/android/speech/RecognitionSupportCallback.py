from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RecognitionSupportCallback"]

class RecognitionSupportCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/speech/RecognitionSupportCallback"
    onError = JavaMethod("(I)V")
    onSupportResult = JavaMethod("(Landroid/speech/RecognitionSupport;)V")