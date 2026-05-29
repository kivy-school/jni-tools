from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DrmRights"]

class DrmRights(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmRights"
    __javaconstructor__ = [("(Landroid/drm/ProcessedData;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/io/File;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]
    getAccountId = JavaMethod("()Ljava/lang/String;")
    getSubscriptionId = JavaMethod("()Ljava/lang/String;")
    getData = JavaMethod("()[B")
    getMimeType = JavaMethod("()Ljava/lang/String;")