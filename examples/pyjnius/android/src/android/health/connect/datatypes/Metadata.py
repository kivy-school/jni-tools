from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Metadata"]

class Metadata(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/Metadata"
    RECORDING_METHOD_ACTIVELY_RECORDED = JavaStaticField("I")
    RECORDING_METHOD_AUTOMATICALLY_RECORDED = JavaStaticField("I")
    RECORDING_METHOD_MANUAL_ENTRY = JavaStaticField("I")
    RECORDING_METHOD_UNKNOWN = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getId = JavaMethod("()Ljava/lang/String;")
    getClientRecordId = JavaMethod("()Ljava/lang/String;")
    getClientRecordVersion = JavaMethod("()J")
    getDataOrigin = JavaMethod("()Landroid/health/connect/datatypes/DataOrigin;")
    getRecordingMethod = JavaMethod("()I")
    getLastModifiedTime = JavaMethod("()Ljava/time/Instant;")
    getDevice = JavaMethod("()Landroid/health/connect/datatypes/Device;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/Metadata$Builder"
        __javaconstructor__ = [("()V", False)]
        setId = JavaMethod("(Ljava/lang/String;)Landroid/health/connect/datatypes/Metadata$Builder;")
        setClientRecordId = JavaMethod("(Ljava/lang/String;)Landroid/health/connect/datatypes/Metadata$Builder;")
        setClientRecordVersion = JavaMethod("(J)Landroid/health/connect/datatypes/Metadata$Builder;")
        setDevice = JavaMethod("(Landroid/health/connect/datatypes/Device;)Landroid/health/connect/datatypes/Metadata$Builder;")
        setDataOrigin = JavaMethod("(Landroid/health/connect/datatypes/DataOrigin;)Landroid/health/connect/datatypes/Metadata$Builder;")
        setRecordingMethod = JavaMethod("(I)Landroid/health/connect/datatypes/Metadata$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/Metadata;")
        setLastModifiedTime = JavaMethod("(Ljava/time/Instant;)Landroid/health/connect/datatypes/Metadata$Builder;")