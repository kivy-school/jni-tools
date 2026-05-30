from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class AssetsProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/res/loader/AssetsProvider"
    loadAssetFd = JavaMethod("(Ljava/lang/String;I)Landroid/content/res/AssetFileDescriptor;")

class ResourcesLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/res/loader/ResourcesLoader"
    __javaconstructor__ = [("()V", False)]
    clearProviders = JavaMethod("()V")
    getProviders = JavaMethod("()Ljava/util/List;")
    removeProvider = JavaMethod("(Landroid/content/res/loader/ResourcesProvider;)V")
    setProviders = JavaMethod("(Ljava/util/List;)V")
    addProvider = JavaMethod("(Landroid/content/res/loader/ResourcesProvider;)V")

class ResourcesProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/res/loader/ResourcesProvider"
    loadFromApk = JavaMultipleMethod([("(Landroid/os/ParcelFileDescriptor;Landroid/content/res/loader/AssetsProvider;)Landroid/content/res/loader/ResourcesProvider;", True, False), ("(Landroid/os/ParcelFileDescriptor;)Landroid/content/res/loader/ResourcesProvider;", True, False)])
    loadFromDirectory = JavaStaticMethod("(Ljava/lang/String;Landroid/content/res/loader/AssetsProvider;)Landroid/content/res/loader/ResourcesProvider;")
    loadFromSplit = JavaStaticMethod("(Landroid/content/Context;Ljava/lang/String;)Landroid/content/res/loader/ResourcesProvider;")
    loadFromTable = JavaStaticMethod("(Landroid/os/ParcelFileDescriptor;Landroid/content/res/loader/AssetsProvider;)Landroid/content/res/loader/ResourcesProvider;")
    loadOverlay = JavaStaticMethod("(Landroid/content/om/OverlayInfo;)Landroid/content/res/loader/ResourcesProvider;")
    empty = JavaStaticMethod("(Landroid/content/res/loader/AssetsProvider;)Landroid/content/res/loader/ResourcesProvider;")
    close = JavaMethod("()V")