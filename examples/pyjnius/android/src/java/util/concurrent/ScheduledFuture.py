from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScheduledFuture"]

class ScheduledFuture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/ScheduledFuture"