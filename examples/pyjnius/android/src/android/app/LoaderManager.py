from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LoaderManager"]

class LoaderManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/LoaderManager"
    __javaconstructor__ = [("()V", False)]
    initLoader = JavaMethod("(ILandroid/os/Bundle;Landroid/app/LoaderManager$LoaderCallbacks;)Landroid/content/Loader;")
    restartLoader = JavaMethod("(ILandroid/os/Bundle;Landroid/app/LoaderManager$LoaderCallbacks;)Landroid/content/Loader;")
    destroyLoader = JavaMethod("(I)V")
    getLoader = JavaMethod("(I)Landroid/content/Loader;")
    dump = JavaMethod("(Ljava/lang/String;Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V")
    enableDebugLogging = JavaStaticMethod("(Z)V")

    class LoaderCallbacks(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/LoaderManager/LoaderCallbacks"
        onCreateLoader = JavaMethod("(ILandroid/os/Bundle;)Landroid/content/Loader;")
        onLoadFinished = JavaMethod("(Landroid/content/Loader;Ljava/lang/Object;)V")
        onLoaderReset = JavaMethod("(Landroid/content/Loader;)V")