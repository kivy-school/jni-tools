from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RecordingSession"]

class RecordingSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/metrics/RecordingSession"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    close = JavaMethod("()V")
    getSessionId = JavaMethod("()Landroid/media/metrics/LogSessionId;")