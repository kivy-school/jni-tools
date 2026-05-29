from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UpdateSignalsRequest"]

class UpdateSignalsRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/signals/UpdateSignalsRequest"
    getUpdateUri = JavaMethod("()Landroid/net/Uri;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/signals/UpdateSignalsRequest$Builder"
        __javaconstructor__ = [("(Landroid/net/Uri;)V", False)]
        setUpdateUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/signals/UpdateSignalsRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/signals/UpdateSignalsRequest;")