from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ServiceWorkerWebSettings"]

class ServiceWorkerWebSettings(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/ServiceWorkerWebSettings"
    __javaconstructor__ = [("()V", False)]
    getAllowContentAccess = JavaMethod("()Z")
    getAllowFileAccess = JavaMethod("()Z")
    getBlockNetworkLoads = JavaMethod("()Z")
    getCacheMode = JavaMethod("()I")
    setAllowContentAccess = JavaMethod("(Z)V")
    setBlockNetworkLoads = JavaMethod("(Z)V")
    setCacheMode = JavaMethod("(I)V")
    setAllowFileAccess = JavaMethod("(Z)V")