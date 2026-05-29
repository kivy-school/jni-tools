from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TracingConfig"]

class TracingConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/TracingConfig"
    CATEGORIES_ALL = JavaStaticField("I")
    CATEGORIES_ANDROID_WEBVIEW = JavaStaticField("I")
    CATEGORIES_FRAME_VIEWER = JavaStaticField("I")
    CATEGORIES_INPUT_LATENCY = JavaStaticField("I")
    CATEGORIES_JAVASCRIPT_AND_RENDERING = JavaStaticField("I")
    CATEGORIES_NONE = JavaStaticField("I")
    CATEGORIES_RENDERING = JavaStaticField("I")
    CATEGORIES_WEB_DEVELOPER = JavaStaticField("I")
    RECORD_CONTINUOUSLY = JavaStaticField("I")
    RECORD_UNTIL_FULL = JavaStaticField("I")
    getPredefinedCategories = JavaMethod("()I")
    getTracingMode = JavaMethod("()I")
    getCustomIncludedCategories = JavaMethod("()Ljava/util/List;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/webkit/TracingConfig$Builder"
        __javaconstructor__ = [("()V", False)]
        addCategories = JavaMultipleMethod([("([Ljava/lang/String;)Landroid/webkit/TracingConfig$Builder;", False, True), ("([I)Landroid/webkit/TracingConfig$Builder;", False, True), ("(Ljava/util/Collection;)Landroid/webkit/TracingConfig$Builder;", False, False)])
        setTracingMode = JavaMethod("(I)Landroid/webkit/TracingConfig$Builder;")
        build = JavaMethod("()Landroid/webkit/TracingConfig;")