from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CookieSyncManager"]

class CookieSyncManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/CookieSyncManager"
    getInstance = JavaStaticMethod("()Landroid/webkit/CookieSyncManager;")
    createInstance = JavaStaticMethod("(Landroid/content/Context;)Landroid/webkit/CookieSyncManager;")
    sync = JavaMethod("()V")
    syncFromRamToFlash = JavaMethod("()V")
    resetSync = JavaMethod("()V")
    startSync = JavaMethod("()V")
    stopSync = JavaMethod("()V")
    run = JavaMethod("()V")