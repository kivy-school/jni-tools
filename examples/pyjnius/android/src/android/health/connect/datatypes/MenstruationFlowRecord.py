from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MenstruationFlowRecord"]

class MenstruationFlowRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/MenstruationFlowRecord"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getFlow = JavaMethod("()I")

    class MenstruationFlowType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/MenstruationFlowRecord$MenstruationFlowType"
        FLOW_HEAVY = JavaStaticField("I")
        FLOW_LIGHT = JavaStaticField("I")
        FLOW_MEDIUM = JavaStaticField("I")
        FLOW_UNKNOWN = JavaStaticField("I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/MenstruationFlowRecord$Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;I)V", False)]
        build = JavaMethod("()Landroid/health/connect/datatypes/MenstruationFlowRecord;")
        clearZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/MenstruationFlowRecord$Builder;")
        setZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/MenstruationFlowRecord$Builder;")