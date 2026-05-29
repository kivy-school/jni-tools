from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RecursiveTask"]

class RecursiveTask(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/RecursiveTask"
    __javaconstructor__ = [("()V", False)]
    getRawResult = JavaMethod("()Ljava/lang/Object;")