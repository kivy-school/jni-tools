from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LeanBodyMassRecord"]

class LeanBodyMassRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/LeanBodyMassRecord"
    getMass = JavaMethod("()Landroid/health/connect/datatypes/units/Mass;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/LeanBodyMassRecord/Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;Landroid/health/connect/datatypes/units/Mass;)V", False)]
        setZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/LeanBodyMassRecord$Builder;")
        clearZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/LeanBodyMassRecord$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/LeanBodyMassRecord;")