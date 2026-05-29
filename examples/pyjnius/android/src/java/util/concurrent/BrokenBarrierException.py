from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BrokenBarrierException"]

class BrokenBarrierException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/BrokenBarrierException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]