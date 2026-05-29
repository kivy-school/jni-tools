from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BackupHelper"]

class BackupHelper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/backup/BackupHelper"
    performBackup = JavaMethod("(Landroid/os/ParcelFileDescriptor;Landroid/app/backup/BackupDataOutput;Landroid/os/ParcelFileDescriptor;)V")
    restoreEntity = JavaMethod("(Landroid/app/backup/BackupDataInputStream;)V")
    writeNewStateDescription = JavaMethod("(Landroid/os/ParcelFileDescriptor;)V")