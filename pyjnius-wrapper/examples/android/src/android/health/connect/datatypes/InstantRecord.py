from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InstantRecord"]

class InstantRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/InstantRecord"
    getTime = JavaMethod("()Ljava/time/Instant;")
    getZoneOffset = JavaMethod("()Ljava/time/ZoneOffset;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")