from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RunnableScheduledFuture"]

class RunnableScheduledFuture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/RunnableScheduledFuture"
    isPeriodic = JavaMethod("()Z")