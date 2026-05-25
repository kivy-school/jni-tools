from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SexualActivityRecord"]

class SexualActivityRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/SexualActivityRecord"
    getProtectionUsed = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/SexualActivityRecord/Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;I)V", False)]
        setZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/SexualActivityRecord$Builder;")
        clearZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/SexualActivityRecord$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/SexualActivityRecord;")

    class SexualActivityProtectionUsed(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/SexualActivityRecord/SexualActivityProtectionUsed"
        PROTECTION_USED_PROTECTED = JavaStaticField("I")
        PROTECTION_USED_UNKNOWN = JavaStaticField("I")
        PROTECTION_USED_UNPROTECTED = JavaStaticField("I")