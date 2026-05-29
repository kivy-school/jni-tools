from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ServiceWorkerClient"]

class ServiceWorkerClient(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/ServiceWorkerClient"
    __javaconstructor__ = [("()V", False)]
    shouldInterceptRequest = JavaMethod("(Landroid/webkit/WebResourceRequest;)Landroid/webkit/WebResourceResponse;")