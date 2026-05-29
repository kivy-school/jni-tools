from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BundleSession"]

class BundleSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/metrics/BundleSession"
    KEY_STATSD_ATOM = JavaStaticField("Ljava/lang/String;")
    reportBundleMetrics = JavaMethod("(Landroid/os/PersistableBundle;)V")
    getSessionId = JavaMethod("()Landroid/media/metrics/LogSessionId;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    close = JavaMethod("()V")