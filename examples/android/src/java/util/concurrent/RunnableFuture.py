from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RunnableFuture"]

class RunnableFuture(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/RunnableFuture"
    run = JavaMethod("()V")