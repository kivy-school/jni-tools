from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RunnableFuture"]

class RunnableFuture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/RunnableFuture"
    run = JavaMethod("()V")