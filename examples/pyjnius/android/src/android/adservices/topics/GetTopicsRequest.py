from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GetTopicsRequest"]

class GetTopicsRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/topics/GetTopicsRequest"
    getAdsSdkName = JavaMethod("()Ljava/lang/String;")
    shouldRecordObservation = JavaMethod("()Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/topics/GetTopicsRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        setShouldRecordObservation = JavaMethod("(Z)Landroid/adservices/topics/GetTopicsRequest$Builder;")
        setAdsSdkName = JavaMethod("(Ljava/lang/String;)Landroid/adservices/topics/GetTopicsRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/topics/GetTopicsRequest;")