from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GetTopicsResponse"]

class GetTopicsResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/topics/GetTopicsResponse"
    getTopics = JavaMethod("()Ljava/util/List;")
    getEncryptedTopics = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/topics/GetTopicsResponse$Builder"
        __javaconstructor__ = [("(Ljava/util/List;)V", False), ("(Ljava/util/List;Ljava/util/List;)V", False)]
        build = JavaMethod("()Landroid/adservices/topics/GetTopicsResponse;")