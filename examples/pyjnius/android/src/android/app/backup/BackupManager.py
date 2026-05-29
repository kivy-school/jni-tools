from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BackupManager"]

class BackupManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/backup/BackupManager"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    dataChanged = JavaMultipleMethod([("(Ljava/lang/String;)V", True, False), ("()V", False, False)])
    getUserForAncestralSerialNumber = JavaMethod("(J)Landroid/os/UserHandle;")
    requestRestore = JavaMethod("(Landroid/app/backup/RestoreObserver;)I")