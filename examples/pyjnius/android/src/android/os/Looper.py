from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Looper"]

class Looper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/Looper"
    getThread = JavaMethod("()Ljava/lang/Thread;")
    myLooper = JavaStaticMethod("()Landroid/os/Looper;")
    myQueue = JavaStaticMethod("()Landroid/os/MessageQueue;")
    prepareMainLooper = JavaStaticMethod("()V")
    quit = JavaMethod("()V")
    isCurrentThread = JavaMethod("()Z")
    quitSafely = JavaMethod("()V")
    setMessageLogging = JavaMethod("(Landroid/util/Printer;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    getQueue = JavaMethod("()Landroid/os/MessageQueue;")
    dump = JavaMethod("(Landroid/util/Printer;Ljava/lang/String;)V")
    prepare = JavaStaticMethod("()V")
    loop = JavaStaticMethod("()V")
    getMainLooper = JavaStaticMethod("()Landroid/os/Looper;")