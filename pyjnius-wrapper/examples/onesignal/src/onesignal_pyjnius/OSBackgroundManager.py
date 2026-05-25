from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSBackgroundManager"]

class OSBackgroundManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSBackgroundManager"
    __javaconstructor__ = [("()V", False)]
    runRunnableOnThread = JavaMethod("(Ljava/lang/Runnable;Ljava/lang/String;)V")