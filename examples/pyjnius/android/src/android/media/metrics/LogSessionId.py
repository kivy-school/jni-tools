from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LogSessionId"]

class LogSessionId(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/metrics/LogSessionId"
    LOG_SESSION_ID_NONE = JavaStaticField("Landroid/media/metrics/LogSessionId;")
    getStringId = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")