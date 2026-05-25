from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AssetsProvider"]

class AssetsProvider(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/res/loader/AssetsProvider"
    loadAssetFd = JavaMethod("(Ljava/lang/String;I)Landroid/content/res/AssetFileDescriptor;")