from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CervicalMucusRecord"]

class CervicalMucusRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/CervicalMucusRecord"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getSensation = JavaMethod("()I")
    getAppearance = JavaMethod("()I")

    class CervicalMucusSensation(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/CervicalMucusRecord$CervicalMucusSensation"
        SENSATION_HEAVY = JavaStaticField("I")
        SENSATION_LIGHT = JavaStaticField("I")
        SENSATION_MEDIUM = JavaStaticField("I")
        SENSATION_UNKNOWN = JavaStaticField("I")

    class CervicalMucusAppearance(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/CervicalMucusRecord$CervicalMucusAppearance"
        APPEARANCE_CREAMY = JavaStaticField("I")
        APPEARANCE_DRY = JavaStaticField("I")
        APPEARANCE_EGG_WHITE = JavaStaticField("I")
        APPEARANCE_STICKY = JavaStaticField("I")
        APPEARANCE_UNKNOWN = JavaStaticField("I")
        APPEARANCE_UNUSUAL = JavaStaticField("I")
        APPEARANCE_WATERY = JavaStaticField("I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/CervicalMucusRecord$Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;II)V", False)]
        build = JavaMethod("()Landroid/health/connect/datatypes/CervicalMucusRecord;")
        clearZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/CervicalMucusRecord$Builder;")
        setZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/CervicalMucusRecord$Builder;")