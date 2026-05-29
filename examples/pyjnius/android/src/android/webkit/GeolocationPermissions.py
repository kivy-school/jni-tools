from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GeolocationPermissions"]

class GeolocationPermissions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/GeolocationPermissions"
    getInstance = JavaStaticMethod("()Landroid/webkit/GeolocationPermissions;")
    getOrigins = JavaMethod("(Landroid/webkit/ValueCallback;)V")
    getAllowed = JavaMethod("(Ljava/lang/String;Landroid/webkit/ValueCallback;)V")
    clear = JavaMethod("(Ljava/lang/String;)V")
    allow = JavaMethod("(Ljava/lang/String;)V")
    clearAll = JavaMethod("()V")

    class Callback(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/webkit/GeolocationPermissions/Callback"
        invoke = JavaMethod("(Ljava/lang/String;ZZ)V")