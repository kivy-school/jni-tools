from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RestoreObserver"]

class RestoreObserver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/backup/RestoreObserver"
    __javaconstructor__ = [("()V", False)]
    restoreStarting = JavaMethod("(I)V")
    onUpdate = JavaMethod("(ILjava/lang/String;)V")
    restoreFinished = JavaMethod("(I)V")