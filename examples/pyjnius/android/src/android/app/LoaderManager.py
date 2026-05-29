from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LoaderManager"]

class LoaderManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/LoaderManager"
    __javaconstructor__ = [("()V", False)]
    enableDebugLogging = JavaStaticMethod("(Z)V")
    destroyLoader = JavaMethod("(I)V")
    initLoader = JavaMethod("(ILandroid/os/Bundle;Landroid/app/LoaderManager$LoaderCallbacks;)Landroid/content/Loader;")
    restartLoader = JavaMethod("(ILandroid/os/Bundle;Landroid/app/LoaderManager$LoaderCallbacks;)Landroid/content/Loader;")
    dump = JavaMethod("(Ljava/lang/String;Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V")
    getLoader = JavaMethod("(I)Landroid/content/Loader;")

    class LoaderCallbacks(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/LoaderManager$LoaderCallbacks"
        onCreateLoader = JavaMethod("(ILandroid/os/Bundle;)Landroid/content/Loader;")
        onLoadFinished = JavaMethod("(Landroid/content/Loader;Ljava/lang/Object;)V")
        onLoaderReset = JavaMethod("(Landroid/content/Loader;)V")