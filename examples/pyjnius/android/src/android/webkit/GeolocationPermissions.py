from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GeolocationPermissions"]

class GeolocationPermissions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/GeolocationPermissions"
    getOrigins = JavaMethod("(Landroid/webkit/ValueCallback;)V")
    getAllowed = JavaMethod("(Ljava/lang/String;Landroid/webkit/ValueCallback;)V")
    clearAll = JavaMethod("()V")
    clear = JavaMethod("(Ljava/lang/String;)V")
    getInstance = JavaStaticMethod("()Landroid/webkit/GeolocationPermissions;")
    allow = JavaMethod("(Ljava/lang/String;)V")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/webkit/GeolocationPermissions$Callback"
        invoke = JavaMethod("(Ljava/lang/String;ZZ)V")