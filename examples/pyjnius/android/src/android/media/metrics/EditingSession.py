from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EditingSession"]

class EditingSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/metrics/EditingSession"
    reportEditingEndedEvent = JavaMethod("(Landroid/media/metrics/EditingEndedEvent;)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    close = JavaMethod("()V")
    getSessionId = JavaMethod("()Landroid/media/metrics/LogSessionId;")