from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RangingConfig"]

class RangingConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/RangingConfig"
    RANGING_SESSION_OOB = JavaStaticField("I")
    RANGING_SESSION_RAW = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getRangingSessionType = JavaMethod("()I")