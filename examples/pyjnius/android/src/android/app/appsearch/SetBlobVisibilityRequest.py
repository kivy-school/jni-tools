from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SetBlobVisibilityRequest"]

class SetBlobVisibilityRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/SetBlobVisibilityRequest"
    getNamespacesNotDisplayedBySystem = JavaMethod("()Ljava/util/Set;")
    getNamespacesVisibleToConfigs = JavaMethod("()Ljava/util/Map;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/SetBlobVisibilityRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        addNamespaceVisibleToConfig = JavaMethod("(Ljava/lang/String;Landroid/app/appsearch/SchemaVisibilityConfig;)Landroid/app/appsearch/SetBlobVisibilityRequest$Builder;")
        clearNamespaceVisibleToConfigs = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/SetBlobVisibilityRequest$Builder;")
        setNamespaceDisplayedBySystem = JavaMethod("(Ljava/lang/String;Z)Landroid/app/appsearch/SetBlobVisibilityRequest$Builder;")
        build = JavaMethod("()Landroid/app/appsearch/SetBlobVisibilityRequest;")