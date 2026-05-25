from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Loader"]

class Loader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/Loader"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    deliverResult = JavaMethod("(Ljava/lang/Object;)V")
    deliverCancellation = JavaMethod("()V")
    getContext = JavaMethod("()Landroid/content/Context;")
    getId = JavaMethod("()I")
    registerListener = JavaMethod("(ILandroid/content/Loader$OnLoadCompleteListener;)V")
    unregisterListener = JavaMethod("(Landroid/content/Loader$OnLoadCompleteListener;)V")
    registerOnLoadCanceledListener = JavaMethod("(Landroid/content/Loader$OnLoadCanceledListener;)V")
    unregisterOnLoadCanceledListener = JavaMethod("(Landroid/content/Loader$OnLoadCanceledListener;)V")
    isStarted = JavaMethod("()Z")
    isAbandoned = JavaMethod("()Z")
    isReset = JavaMethod("()Z")
    startLoading = JavaMethod("()V")
    onStartLoading = JavaMethod("()V")
    cancelLoad = JavaMethod("()Z")
    onCancelLoad = JavaMethod("()Z")
    forceLoad = JavaMethod("()V")
    onForceLoad = JavaMethod("()V")
    stopLoading = JavaMethod("()V")
    onStopLoading = JavaMethod("()V")
    abandon = JavaMethod("()V")
    onAbandon = JavaMethod("()V")
    reset = JavaMethod("()V")
    onReset = JavaMethod("()V")
    takeContentChanged = JavaMethod("()Z")
    commitContentChanged = JavaMethod("()V")
    rollbackContentChanged = JavaMethod("()V")
    onContentChanged = JavaMethod("()V")
    dataToString = JavaMethod("(Ljava/lang/Object;)Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    dump = JavaMethod("(Ljava/lang/String;Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V")

    class ForceLoadContentObserver(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/Loader/ForceLoadContentObserver"
        __javaconstructor__ = [("(Landroid/content/Loader;)V", False)]
        deliverSelfNotifications = JavaMethod("()Z")
        onChange = JavaMethod("(Z)V")

    class OnLoadCanceledListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/Loader/OnLoadCanceledListener"
        onLoadCanceled = JavaMethod("(Landroid/content/Loader;)V")

    class OnLoadCompleteListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/Loader/OnLoadCompleteListener"
        onLoadComplete = JavaMethod("(Landroid/content/Loader;Ljava/lang/Object;)V")