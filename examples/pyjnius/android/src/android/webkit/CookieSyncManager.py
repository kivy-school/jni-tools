from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CookieSyncManager"]

class CookieSyncManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/CookieSyncManager"
    resetSync = JavaMethod("()V")
    stopSync = JavaMethod("()V")
    run = JavaMethod("()V")
    getInstance = JavaStaticMethod("()Landroid/webkit/CookieSyncManager;")
    startSync = JavaMethod("()V")
    createInstance = JavaStaticMethod("(Landroid/content/Context;)Landroid/webkit/CookieSyncManager;")
    sync = JavaMethod("()V")