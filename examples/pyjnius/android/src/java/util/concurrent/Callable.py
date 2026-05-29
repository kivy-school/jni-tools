from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Callable"]

class Callable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/Callable"
    call = JavaMethod("()Ljava/lang/Object;")