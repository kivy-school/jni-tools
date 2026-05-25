from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RunnableScheduledFuture"]

class RunnableScheduledFuture(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/RunnableScheduledFuture"
    isPeriodic = JavaMethod("()Z")