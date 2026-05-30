from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class PhantomReference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ref/PhantomReference"
    __javaconstructor__ = [("(Ljava/lang/Object;Ljava/lang/ref/ReferenceQueue;)V", False)]
    get = JavaMethod("()Ljava/lang/Object;")

class Cleaner(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ref/Cleaner"
    create = JavaMultipleMethod([("(Ljava/util/concurrent/ThreadFactory;)Ljava/lang/ref/Cleaner;", True, False), ("()Ljava/lang/ref/Cleaner;", True, False)])
    register = JavaMethod("(Ljava/lang/Object;Ljava/lang/Runnable;)Ljava/lang/ref/Cleaner$Cleanable;")

    class Cleanable(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/lang/ref/Cleaner$Cleanable"
        clean = JavaMethod("()V")

class ReferenceQueue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ref/ReferenceQueue"
    __javaconstructor__ = [("()V", False)]
    poll = JavaMethod("()Ljava/lang/ref/Reference;")
    remove = JavaMultipleMethod([("()Ljava/lang/ref/Reference;", False, False), ("(J)Ljava/lang/ref/Reference;", False, False)])

class SoftReference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ref/SoftReference"
    __javaconstructor__ = [("(Ljava/lang/Object;)V", False), ("(Ljava/lang/Object;Ljava/lang/ref/ReferenceQueue;)V", False)]
    get = JavaMethod("()Ljava/lang/Object;")

class Reference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ref/Reference"
    get = JavaMethod("()Ljava/lang/Object;")
    clear = JavaMethod("()V")
    reachabilityFence = JavaStaticMethod("(Ljava/lang/Object;)V")
    enqueue = JavaMethod("()Z")
    refersTo = JavaMethod("(Ljava/lang/Object;)Z")
    isEnqueued = JavaMethod("()Z")

class WeakReference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ref/WeakReference"
    __javaconstructor__ = [("(Ljava/lang/Object;)V", False), ("(Ljava/lang/Object;Ljava/lang/ref/ReferenceQueue;)V", False)]