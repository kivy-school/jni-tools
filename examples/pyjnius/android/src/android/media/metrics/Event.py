from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Event"]

class Event(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/metrics/Event"
    getMetricsBundle = JavaMethod("()Landroid/os/Bundle;")
    getTimeSinceCreatedMillis = JavaMethod("()J")