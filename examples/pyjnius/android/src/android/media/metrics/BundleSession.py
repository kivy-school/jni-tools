from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BundleSession"]

class BundleSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/metrics/BundleSession"
    KEY_STATSD_ATOM = JavaStaticField("Ljava/lang/String;")
    reportBundleMetrics = JavaMethod("(Landroid/os/PersistableBundle;)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    close = JavaMethod("()V")
    getSessionId = JavaMethod("()Landroid/media/metrics/LogSessionId;")