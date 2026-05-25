from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebTriggerOutput"]

class WebTriggerOutput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/WebTriggerOutput"
    getRequestLogRecord = JavaMethod("()Landroid/adservices/ondevicepersonalization/RequestLogRecord;")
    getEventLogRecords = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/WebTriggerOutput/Builder"
        __javaconstructor__ = [("()V", False)]
        setRequestLogRecord = JavaMethod("(Landroid/adservices/ondevicepersonalization/RequestLogRecord;)Landroid/adservices/ondevicepersonalization/WebTriggerOutput$Builder;")
        setEventLogRecords = JavaMethod("(Ljava/util/List;)Landroid/adservices/ondevicepersonalization/WebTriggerOutput$Builder;")
        addEventLogRecord = JavaMethod("(Landroid/adservices/ondevicepersonalization/EventLogRecord;)Landroid/adservices/ondevicepersonalization/WebTriggerOutput$Builder;")
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/WebTriggerOutput;")