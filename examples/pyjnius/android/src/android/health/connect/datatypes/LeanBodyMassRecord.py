from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LeanBodyMassRecord"]

class LeanBodyMassRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/LeanBodyMassRecord"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getMass = JavaMethod("()Landroid/health/connect/datatypes/units/Mass;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/LeanBodyMassRecord$Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;Landroid/health/connect/datatypes/units/Mass;)V", False)]
        build = JavaMethod("()Landroid/health/connect/datatypes/LeanBodyMassRecord;")
        clearZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/LeanBodyMassRecord$Builder;")
        setZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/LeanBodyMassRecord$Builder;")