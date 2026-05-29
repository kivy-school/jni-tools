from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DrmSupportInfo"]

class DrmSupportInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmSupportInfo"
    __javaconstructor__ = [("()V", False)]
    getDescriprition = JavaMethod("()Ljava/lang/String;")
    addFileSuffix = JavaMethod("(Ljava/lang/String;)V")
    addMimeType = JavaMethod("(Ljava/lang/String;)V")
    getFileSuffixIterator = JavaMethod("()Ljava/util/Iterator;")
    getMimeTypeIterator = JavaMethod("()Ljava/util/Iterator;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    setDescription = JavaMethod("(Ljava/lang/String;)V")
    getDescription = JavaMethod("()Ljava/lang/String;")