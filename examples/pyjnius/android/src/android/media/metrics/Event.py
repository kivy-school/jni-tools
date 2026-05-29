from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Event"]

class Event(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/metrics/Event"
    getTimeSinceCreatedMillis = JavaMethod("()J")
    getMetricsBundle = JavaMethod("()Landroid/os/Bundle;")