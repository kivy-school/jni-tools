from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Runnable"]

class Runnable(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Runnable"
    run = JavaMethod("()V")