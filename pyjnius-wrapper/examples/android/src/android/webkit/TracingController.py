from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TracingController"]

class TracingController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/TracingController"
    __javaconstructor__ = [("()V", False)]
    getInstance = JavaStaticMethod("()Landroid/webkit/TracingController;")
    start = JavaMethod("(Landroid/webkit/TracingConfig;)V")
    stop = JavaMethod("(Ljava/io/OutputStream;Ljava/util/concurrent/Executor;)Z")
    isTracing = JavaMethod("()Z")