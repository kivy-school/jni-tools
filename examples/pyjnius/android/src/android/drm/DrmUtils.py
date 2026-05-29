from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DrmUtils"]

class DrmUtils(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmUtils"
    __javaconstructor__ = [("()V", False)]
    getExtendedMetadataParser = JavaStaticMethod("([B)Landroid/drm/DrmUtils$ExtendedMetadataParser;")

    class ExtendedMetadataParser(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/drm/DrmUtils$ExtendedMetadataParser"
        keyIterator = JavaMethod("()Ljava/util/Iterator;")
        get = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
        iterator = JavaMethod("()Ljava/util/Iterator;")