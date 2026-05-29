from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Delayed"]

class Delayed(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/Delayed"
    getDelay = JavaMethod("(Ljava/util/concurrent/TimeUnit;)J")