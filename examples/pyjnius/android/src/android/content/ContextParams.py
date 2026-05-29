from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContextParams"]

class ContextParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ContextParams"
    getNextAttributionSource = JavaMethod("()Landroid/content/AttributionSource;")
    shouldRegisterAttributionSource = JavaMethod("()Z")
    getAttributionTag = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/ContextParams$Builder"
        __javaconstructor__ = [("()V", False), ("(Landroid/content/ContextParams;)V", False)]
        setNextAttributionSource = JavaMethod("(Landroid/content/AttributionSource;)Landroid/content/ContextParams$Builder;")
        setShouldRegisterAttributionSource = JavaMethod("(Z)Landroid/content/ContextParams$Builder;")
        build = JavaMethod("()Landroid/content/ContextParams;")
        setAttributionTag = JavaMethod("(Ljava/lang/String;)Landroid/content/ContextParams$Builder;")