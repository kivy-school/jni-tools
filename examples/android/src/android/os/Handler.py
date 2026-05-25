from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Handler"]

class Handler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/Handler"
    __javaconstructor__ = [("()V", False), ("(Landroid/os/Handler$Callback;)V", False), ("(Landroid/os/Looper;)V", False), ("(Landroid/os/Looper;Landroid/os/Handler$Callback;)V", False)]
    handleMessage = JavaMethod("(Landroid/os/Message;)V")
    dispatchMessage = JavaMethod("(Landroid/os/Message;)V")
    createAsync = JavaMultipleMethod([("(Landroid/os/Looper;)Landroid/os/Handler;", True, False), ("(Landroid/os/Looper;Landroid/os/Handler$Callback;)Landroid/os/Handler;", True, False)])
    getMessageName = JavaMethod("(Landroid/os/Message;)Ljava/lang/String;")
    obtainMessage = JavaMultipleMethod([("()Landroid/os/Message;", False, False), ("(I)Landroid/os/Message;", False, False), ("(ILjava/lang/Object;)Landroid/os/Message;", False, False), ("(III)Landroid/os/Message;", False, False), ("(IIILjava/lang/Object;)Landroid/os/Message;", False, False)])
    post = JavaMethod("(Ljava/lang/Runnable;)Z")
    postAtTime = JavaMultipleMethod([("(Ljava/lang/Runnable;J)Z", False, False), ("(Ljava/lang/Runnable;Ljava/lang/Object;J)Z", False, False)])
    postDelayed = JavaMultipleMethod([("(Ljava/lang/Runnable;J)Z", False, False), ("(Ljava/lang/Runnable;Ljava/lang/Object;J)Z", False, False)])
    postAtFrontOfQueue = JavaMethod("(Ljava/lang/Runnable;)Z")
    removeCallbacks = JavaMultipleMethod([("(Ljava/lang/Runnable;)V", False, False), ("(Ljava/lang/Runnable;Ljava/lang/Object;)V", False, False)])
    sendMessage = JavaMethod("(Landroid/os/Message;)Z")
    sendEmptyMessage = JavaMethod("(I)Z")
    sendEmptyMessageDelayed = JavaMethod("(IJ)Z")
    sendEmptyMessageAtTime = JavaMethod("(IJ)Z")
    sendMessageDelayed = JavaMethod("(Landroid/os/Message;J)Z")
    sendMessageAtTime = JavaMethod("(Landroid/os/Message;J)Z")
    sendMessageAtFrontOfQueue = JavaMethod("(Landroid/os/Message;)Z")
    removeMessages = JavaMultipleMethod([("(I)V", False, False), ("(ILjava/lang/Object;)V", False, False)])
    removeCallbacksAndMessages = JavaMethod("(Ljava/lang/Object;)V")
    hasMessages = JavaMultipleMethod([("(I)Z", False, False), ("(ILjava/lang/Object;)Z", False, False)])
    hasCallbacks = JavaMethod("(Ljava/lang/Runnable;)Z")
    getLooper = JavaMethod("()Landroid/os/Looper;")
    dump = JavaMethod("(Landroid/util/Printer;Ljava/lang/String;)V")
    toString = JavaMethod("()Ljava/lang/String;")

    class Callback(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/Handler/Callback"
        handleMessage = JavaMethod("(Landroid/os/Message;)Z")