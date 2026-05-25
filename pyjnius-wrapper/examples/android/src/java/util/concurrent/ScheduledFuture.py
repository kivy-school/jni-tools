from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScheduledFuture"]

class ScheduledFuture(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/ScheduledFuture"