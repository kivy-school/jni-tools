from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RecursiveTask"]

class RecursiveTask(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/RecursiveTask"
    __javaconstructor__ = [("()V", False)]
    compute = JavaMethod("()Ljava/lang/Object;")
    getRawResult = JavaMethod("()Ljava/lang/Object;")
    setRawResult = JavaMethod("(Ljava/lang/Object;)V")
    exec = JavaMethod("()Z")