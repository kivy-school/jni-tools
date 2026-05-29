from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ServiceWorkerController"]

class ServiceWorkerController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/ServiceWorkerController"
    __javaconstructor__ = [("()V", False)]
    getServiceWorkerWebSettings = JavaMethod("()Landroid/webkit/ServiceWorkerWebSettings;")
    setServiceWorkerClient = JavaMethod("(Landroid/webkit/ServiceWorkerClient;)V")
    getInstance = JavaStaticMethod("()Landroid/webkit/ServiceWorkerController;")