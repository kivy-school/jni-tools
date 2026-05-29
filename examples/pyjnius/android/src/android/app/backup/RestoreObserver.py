from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RestoreObserver"]

class RestoreObserver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/backup/RestoreObserver"
    __javaconstructor__ = [("()V", False)]
    onUpdate = JavaMethod("(ILjava/lang/String;)V")
    restoreFinished = JavaMethod("(I)V")
    restoreStarting = JavaMethod("(I)V")