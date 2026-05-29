from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RecoverySystem"]

class RecoverySystem(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/RecoverySystem"
    rebootWipeUserData = JavaStaticMethod("(Landroid/content/Context;)V")
    verifyPackage = JavaStaticMethod("(Ljava/io/File;Landroid/os/RecoverySystem$ProgressListener;Ljava/io/File;)V")
    installPackage = JavaStaticMethod("(Landroid/content/Context;Ljava/io/File;)V")
    rebootWipeCache = JavaStaticMethod("(Landroid/content/Context;)V")

    class ProgressListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/RecoverySystem$ProgressListener"
        onProgress = JavaMethod("(I)V")