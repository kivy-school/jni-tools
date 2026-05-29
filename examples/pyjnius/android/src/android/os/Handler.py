from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Handler"]

class Handler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/Handler"
    __javaconstructor__ = [("(Landroid/os/Looper;Landroid/os/Handler$Callback;)V", False), ("(Landroid/os/Looper;)V", False), ("(Landroid/os/Handler$Callback;)V", False), ("()V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    dump = JavaMethod("(Landroid/util/Printer;Ljava/lang/String;)V")
    post = JavaMethod("(Ljava/lang/Runnable;)Z")
    postDelayed = JavaMultipleMethod([("(Ljava/lang/Runnable;Ljava/lang/Object;J)Z", False, False), ("(Ljava/lang/Runnable;J)Z", False, False)])
    removeCallbacks = JavaMultipleMethod([("(Ljava/lang/Runnable;)V", False, False), ("(Ljava/lang/Runnable;Ljava/lang/Object;)V", False, False)])
    createAsync = JavaMultipleMethod([("(Landroid/os/Looper;)Landroid/os/Handler;", True, False), ("(Landroid/os/Looper;Landroid/os/Handler$Callback;)Landroid/os/Handler;", True, False)])
    dispatchMessage = JavaMethod("(Landroid/os/Message;)V")
    getLooper = JavaMethod("()Landroid/os/Looper;")
    getMessageName = JavaMethod("(Landroid/os/Message;)Ljava/lang/String;")
    handleMessage = JavaMethod("(Landroid/os/Message;)V")
    hasCallbacks = JavaMethod("(Ljava/lang/Runnable;)Z")
    hasMessages = JavaMultipleMethod([("(I)Z", False, False), ("(ILjava/lang/Object;)Z", False, False)])
    obtainMessage = JavaMultipleMethod([("(I)Landroid/os/Message;", False, False), ("(III)Landroid/os/Message;", False, False), ("()Landroid/os/Message;", False, False), ("(IIILjava/lang/Object;)Landroid/os/Message;", False, False), ("(ILjava/lang/Object;)Landroid/os/Message;", False, False)])
    postAtFrontOfQueue = JavaMethod("(Ljava/lang/Runnable;)Z")
    postAtTime = JavaMultipleMethod([("(Ljava/lang/Runnable;Ljava/lang/Object;J)Z", False, False), ("(Ljava/lang/Runnable;J)Z", False, False)])
    removeCallbacksAndMessages = JavaMethod("(Ljava/lang/Object;)V")
    removeMessages = JavaMultipleMethod([("(ILjava/lang/Object;)V", False, False), ("(I)V", False, False)])
    sendEmptyMessage = JavaMethod("(I)Z")
    sendEmptyMessageAtTime = JavaMethod("(IJ)Z")
    sendEmptyMessageDelayed = JavaMethod("(IJ)Z")
    sendMessage = JavaMethod("(Landroid/os/Message;)Z")
    sendMessageAtFrontOfQueue = JavaMethod("(Landroid/os/Message;)Z")
    sendMessageAtTime = JavaMethod("(Landroid/os/Message;J)Z")
    sendMessageDelayed = JavaMethod("(Landroid/os/Message;J)Z")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/Handler$Callback"
        handleMessage = JavaMethod("(Landroid/os/Message;)Z")