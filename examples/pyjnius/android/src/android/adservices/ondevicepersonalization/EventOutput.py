from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EventOutput"]

class EventOutput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/EventOutput"
    getEventLogRecord = JavaMethod("()Landroid/adservices/ondevicepersonalization/EventLogRecord;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/EventOutput$Builder"
        __javaconstructor__ = [("()V", False)]
        setEventLogRecord = JavaMethod("(Landroid/adservices/ondevicepersonalization/EventLogRecord;)Landroid/adservices/ondevicepersonalization/EventOutput$Builder;")
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/EventOutput;")