from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConnectionlessHandwritingCallback"]

class ConnectionlessHandwritingCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/ConnectionlessHandwritingCallback"
    CONNECTIONLESS_HANDWRITING_ERROR_NO_TEXT_RECOGNIZED = JavaStaticField("I")
    CONNECTIONLESS_HANDWRITING_ERROR_OTHER = JavaStaticField("I")
    CONNECTIONLESS_HANDWRITING_ERROR_UNSUPPORTED = JavaStaticField("I")
    onResult = JavaMethod("(Ljava/lang/CharSequence;)V")
    onError = JavaMethod("(I)V")