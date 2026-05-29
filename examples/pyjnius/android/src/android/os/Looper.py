from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Looper"]

class Looper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/Looper"
    prepare = JavaStaticMethod("()V")
    prepareMainLooper = JavaStaticMethod("()V")
    getMainLooper = JavaStaticMethod("()Landroid/os/Looper;")
    loop = JavaStaticMethod("()V")
    myLooper = JavaStaticMethod("()Landroid/os/Looper;")
    myQueue = JavaStaticMethod("()Landroid/os/MessageQueue;")
    isCurrentThread = JavaMethod("()Z")
    setMessageLogging = JavaMethod("(Landroid/util/Printer;)V")
    quit = JavaMethod("()V")
    quitSafely = JavaMethod("()V")
    getThread = JavaMethod("()Ljava/lang/Thread;")
    getQueue = JavaMethod("()Landroid/os/MessageQueue;")
    dump = JavaMethod("(Landroid/util/Printer;Ljava/lang/String;)V")
    toString = JavaMethod("()Ljava/lang/String;")