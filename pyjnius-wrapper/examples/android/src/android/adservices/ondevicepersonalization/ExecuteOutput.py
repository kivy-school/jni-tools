from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExecuteOutput"]

class ExecuteOutput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/ExecuteOutput"
    getRequestLogRecord = JavaMethod("()Landroid/adservices/ondevicepersonalization/RequestLogRecord;")
    getRenderingConfig = JavaMethod("()Landroid/adservices/ondevicepersonalization/RenderingConfig;")
    getEventLogRecords = JavaMethod("()Ljava/util/List;")
    getOutputData = JavaMethod("()[B")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/ExecuteOutput/Builder"
        __javaconstructor__ = [("()V", False)]
        setRequestLogRecord = JavaMethod("(Landroid/adservices/ondevicepersonalization/RequestLogRecord;)Landroid/adservices/ondevicepersonalization/ExecuteOutput$Builder;")
        setRenderingConfig = JavaMethod("(Landroid/adservices/ondevicepersonalization/RenderingConfig;)Landroid/adservices/ondevicepersonalization/ExecuteOutput$Builder;")
        setEventLogRecords = JavaMethod("(Ljava/util/List;)Landroid/adservices/ondevicepersonalization/ExecuteOutput$Builder;")
        addEventLogRecord = JavaMethod("(Landroid/adservices/ondevicepersonalization/EventLogRecord;)Landroid/adservices/ondevicepersonalization/ExecuteOutput$Builder;")
        setOutputData = JavaMethod("([B)Landroid/adservices/ondevicepersonalization/ExecuteOutput$Builder;", varargs=True)
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/ExecuteOutput;")