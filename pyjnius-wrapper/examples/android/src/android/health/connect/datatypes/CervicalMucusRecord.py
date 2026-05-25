from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CervicalMucusRecord"]

class CervicalMucusRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/CervicalMucusRecord"
    getSensation = JavaMethod("()I")
    getAppearance = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/CervicalMucusRecord/Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;II)V", False)]
        setZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/CervicalMucusRecord$Builder;")
        clearZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/CervicalMucusRecord$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/CervicalMucusRecord;")

    class CervicalMucusAppearance(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/CervicalMucusRecord/CervicalMucusAppearance"
        APPEARANCE_CREAMY = JavaStaticField("I")
        APPEARANCE_DRY = JavaStaticField("I")
        APPEARANCE_EGG_WHITE = JavaStaticField("I")
        APPEARANCE_STICKY = JavaStaticField("I")
        APPEARANCE_UNKNOWN = JavaStaticField("I")
        APPEARANCE_UNUSUAL = JavaStaticField("I")
        APPEARANCE_WATERY = JavaStaticField("I")

    class CervicalMucusSensation(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/CervicalMucusRecord/CervicalMucusSensation"
        SENSATION_HEAVY = JavaStaticField("I")
        SENSATION_LIGHT = JavaStaticField("I")
        SENSATION_MEDIUM = JavaStaticField("I")
        SENSATION_UNKNOWN = JavaStaticField("I")