from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OvulationTestRecord"]

class OvulationTestRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/OvulationTestRecord"
    getResult = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/OvulationTestRecord/Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;I)V", False)]
        setZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/OvulationTestRecord$Builder;")
        clearZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/OvulationTestRecord$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/OvulationTestRecord;")

    class OvulationTestResult(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/OvulationTestRecord/OvulationTestResult"
        RESULT_HIGH = JavaStaticField("I")
        RESULT_INCONCLUSIVE = JavaStaticField("I")
        RESULT_NEGATIVE = JavaStaticField("I")
        RESULT_POSITIVE = JavaStaticField("I")