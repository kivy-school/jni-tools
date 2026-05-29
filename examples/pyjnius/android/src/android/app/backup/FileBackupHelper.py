from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileBackupHelper"]

class FileBackupHelper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/backup/FileBackupHelper"
    __javaconstructor__ = [("(Landroid/content/Context;[Ljava/lang/String;)V", True)]
    performBackup = JavaMethod("(Landroid/os/ParcelFileDescriptor;Landroid/app/backup/BackupDataOutput;Landroid/os/ParcelFileDescriptor;)V")
    restoreEntity = JavaMethod("(Landroid/app/backup/BackupDataInputStream;)V")
    writeNewStateDescription = JavaMethod("(Landroid/os/ParcelFileDescriptor;)V")