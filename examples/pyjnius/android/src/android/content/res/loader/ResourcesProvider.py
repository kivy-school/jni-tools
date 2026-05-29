from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ResourcesProvider"]

class ResourcesProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/res/loader/ResourcesProvider"
    loadFromDirectory = JavaStaticMethod("(Ljava/lang/String;Landroid/content/res/loader/AssetsProvider;)Landroid/content/res/loader/ResourcesProvider;")
    loadFromApk = JavaMultipleMethod([("(Landroid/os/ParcelFileDescriptor;)Landroid/content/res/loader/ResourcesProvider;", True, False), ("(Landroid/os/ParcelFileDescriptor;Landroid/content/res/loader/AssetsProvider;)Landroid/content/res/loader/ResourcesProvider;", True, False)])
    loadFromTable = JavaStaticMethod("(Landroid/os/ParcelFileDescriptor;Landroid/content/res/loader/AssetsProvider;)Landroid/content/res/loader/ResourcesProvider;")
    loadOverlay = JavaStaticMethod("(Landroid/content/om/OverlayInfo;)Landroid/content/res/loader/ResourcesProvider;")
    loadFromSplit = JavaStaticMethod("(Landroid/content/Context;Ljava/lang/String;)Landroid/content/res/loader/ResourcesProvider;")
    empty = JavaStaticMethod("(Landroid/content/res/loader/AssetsProvider;)Landroid/content/res/loader/ResourcesProvider;")
    close = JavaMethod("()V")