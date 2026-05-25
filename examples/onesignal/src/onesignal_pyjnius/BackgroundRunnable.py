from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BackgroundRunnable"]

class BackgroundRunnable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/BackgroundRunnable"
    __javaconstructor__ = [("()V", False)]
    run = JavaMethod("()V")