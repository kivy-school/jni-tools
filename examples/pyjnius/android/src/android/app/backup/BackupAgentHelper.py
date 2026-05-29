from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BackupAgentHelper"]

class BackupAgentHelper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/backup/BackupAgentHelper"
    __javaconstructor__ = [("()V", False)]
    onBackup = JavaMethod("(Landroid/os/ParcelFileDescriptor;Landroid/app/backup/BackupDataOutput;Landroid/os/ParcelFileDescriptor;)V")
    onRestore = JavaMethod("(Landroid/app/backup/BackupDataInput;ILandroid/os/ParcelFileDescriptor;)V")
    addHelper = JavaMethod("(Ljava/lang/String;Landroid/app/backup/BackupHelper;)V")