from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ResourcesLoader"]

class ResourcesLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/res/loader/ResourcesLoader"
    __javaconstructor__ = [("()V", False)]
    addProvider = JavaMethod("(Landroid/content/res/loader/ResourcesProvider;)V")
    removeProvider = JavaMethod("(Landroid/content/res/loader/ResourcesProvider;)V")
    getProviders = JavaMethod("()Ljava/util/List;")
    setProviders = JavaMethod("(Ljava/util/List;)V")
    clearProviders = JavaMethod("()V")