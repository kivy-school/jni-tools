from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BackupAgent"]

class BackupAgent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/backup/BackupAgent"
    __javaconstructor__ = [("()V", False)]
    FLAG_CLIENT_SIDE_ENCRYPTION_ENABLED = JavaStaticField("I")
    FLAG_DEVICE_TO_DEVICE_TRANSFER = JavaStaticField("I")
    TYPE_DIRECTORY = JavaStaticField("I")
    TYPE_FILE = JavaStaticField("I")
    onCreate = JavaMethod("()V")
    onDestroy = JavaMethod("()V")
    onBackup = JavaMethod("(Landroid/os/ParcelFileDescriptor;Landroid/app/backup/BackupDataOutput;Landroid/os/ParcelFileDescriptor;)V")
    onRestore = JavaMultipleMethod([("(Landroid/app/backup/BackupDataInput;ILandroid/os/ParcelFileDescriptor;)V", False, False), ("(Landroid/app/backup/BackupDataInput;JLandroid/os/ParcelFileDescriptor;)V", False, False)])
    onFullBackup = JavaMethod("(Landroid/app/backup/FullBackupDataOutput;)V")
    onQuotaExceeded = JavaMethod("(JJ)V")
    fullBackupFile = JavaMethod("(Ljava/io/File;Landroid/app/backup/FullBackupDataOutput;)V")
    onRestoreFile = JavaMethod("(Landroid/os/ParcelFileDescriptor;JLjava/io/File;IJJ)V")
    onRestoreFinished = JavaMethod("()V")