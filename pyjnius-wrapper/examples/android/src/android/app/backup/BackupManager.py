from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BackupManager"]

class BackupManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/backup/BackupManager"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    dataChanged = JavaMultipleMethod([("()V", False, False), ("(Ljava/lang/String;)V", True, False)])
    requestRestore = JavaMethod("(Landroid/app/backup/RestoreObserver;)I")
    getUserForAncestralSerialNumber = JavaMethod("(J)Landroid/os/UserHandle;")