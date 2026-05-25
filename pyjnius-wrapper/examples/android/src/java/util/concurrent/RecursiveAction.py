from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RecursiveAction"]

class RecursiveAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/RecursiveAction"
    __javaconstructor__ = [("()V", False)]
    compute = JavaMethod("()V")
    getRawResult = JavaMethod("()Ljava/lang/Void;")
    setRawResult = JavaMethod("(Ljava/lang/Void;)V")
    exec = JavaMethod("()Z")