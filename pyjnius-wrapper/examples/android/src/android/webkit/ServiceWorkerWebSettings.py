from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ServiceWorkerWebSettings"]

class ServiceWorkerWebSettings(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/ServiceWorkerWebSettings"
    __javaconstructor__ = [("()V", False)]
    setCacheMode = JavaMethod("(I)V")
    getCacheMode = JavaMethod("()I")
    setAllowContentAccess = JavaMethod("(Z)V")
    getAllowContentAccess = JavaMethod("()Z")
    setAllowFileAccess = JavaMethod("(Z)V")
    getAllowFileAccess = JavaMethod("()Z")
    setBlockNetworkLoads = JavaMethod("(Z)V")
    getBlockNetworkLoads = JavaMethod("()Z")