from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Loader"]

class Loader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/Loader"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    abandon = JavaMethod("()V")
    reset = JavaMethod("()V")
    toString = JavaMethod("()Ljava/lang/String;")
    getId = JavaMethod("()I")
    isStarted = JavaMethod("()Z")
    dump = JavaMethod("(Ljava/lang/String;Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V")
    getContext = JavaMethod("()Landroid/content/Context;")
    cancelLoad = JavaMethod("()Z")
    commitContentChanged = JavaMethod("()V")
    dataToString = JavaMethod("(Ljava/lang/Object;)Ljava/lang/String;")
    deliverCancellation = JavaMethod("()V")
    deliverResult = JavaMethod("(Ljava/lang/Object;)V")
    forceLoad = JavaMethod("()V")
    isAbandoned = JavaMethod("()Z")
    isReset = JavaMethod("()Z")
    registerListener = JavaMethod("(ILandroid/content/Loader$OnLoadCompleteListener;)V")
    registerOnLoadCanceledListener = JavaMethod("(Landroid/content/Loader$OnLoadCanceledListener;)V")
    rollbackContentChanged = JavaMethod("()V")
    startLoading = JavaMethod("()V")
    stopLoading = JavaMethod("()V")
    takeContentChanged = JavaMethod("()Z")
    unregisterListener = JavaMethod("(Landroid/content/Loader$OnLoadCompleteListener;)V")
    unregisterOnLoadCanceledListener = JavaMethod("(Landroid/content/Loader$OnLoadCanceledListener;)V")
    onContentChanged = JavaMethod("()V")

    class OnLoadCompleteListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/Loader$OnLoadCompleteListener"
        onLoadComplete = JavaMethod("(Landroid/content/Loader;Ljava/lang/Object;)V")

    class OnLoadCanceledListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/Loader$OnLoadCanceledListener"
        onLoadCanceled = JavaMethod("(Landroid/content/Loader;)V")

    class ForceLoadContentObserver(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/Loader$ForceLoadContentObserver"
        __javaconstructor__ = [("(Landroid/content/Loader;)V", False)]
        onChange = JavaMethod("(Z)V")
        deliverSelfNotifications = JavaMethod("()Z")