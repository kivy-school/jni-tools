from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExecuteOutput"]

class ExecuteOutput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/ExecuteOutput"
    getOutputData = JavaMethod("()[B")
    getBestValue = JavaMethod("()I")
    getEventLogRecords = JavaMethod("()Ljava/util/List;")
    getRequestLogRecord = JavaMethod("()Landroid/adservices/ondevicepersonalization/RequestLogRecord;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getRenderingConfig = JavaMethod("()Landroid/adservices/ondevicepersonalization/RenderingConfig;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/ExecuteOutput$Builder"
        __javaconstructor__ = [("()V", False)]
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/ExecuteOutput;")
        setOutputData = JavaMethod("([B)Landroid/adservices/ondevicepersonalization/ExecuteOutput$Builder;", varargs=True)
        setRenderingConfig = JavaMethod("(Landroid/adservices/ondevicepersonalization/RenderingConfig;)Landroid/adservices/ondevicepersonalization/ExecuteOutput$Builder;")
        setBestValue = JavaMethod("(I)Landroid/adservices/ondevicepersonalization/ExecuteOutput$Builder;")
        setEventLogRecords = JavaMethod("(Ljava/util/List;)Landroid/adservices/ondevicepersonalization/ExecuteOutput$Builder;")
        addEventLogRecord = JavaMethod("(Landroid/adservices/ondevicepersonalization/EventLogRecord;)Landroid/adservices/ondevicepersonalization/ExecuteOutput$Builder;")
        setRequestLogRecord = JavaMethod("(Landroid/adservices/ondevicepersonalization/RequestLogRecord;)Landroid/adservices/ondevicepersonalization/ExecuteOutput$Builder;")