from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MenstruationFlowRecord"]

class MenstruationFlowRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/MenstruationFlowRecord"
    getFlow = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/MenstruationFlowRecord/Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;I)V", False)]
        setZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/MenstruationFlowRecord$Builder;")
        clearZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/MenstruationFlowRecord$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/MenstruationFlowRecord;")

    class MenstruationFlowType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/MenstruationFlowRecord/MenstruationFlowType"
        FLOW_HEAVY = JavaStaticField("I")
        FLOW_LIGHT = JavaStaticField("I")
        FLOW_MEDIUM = JavaStaticField("I")
        FLOW_UNKNOWN = JavaStaticField("I")