from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TranscodingSession"]

class TranscodingSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/metrics/TranscodingSession"
    getSessionId = JavaMethod("()Landroid/media/metrics/LogSessionId;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    close = JavaMethod("()V")