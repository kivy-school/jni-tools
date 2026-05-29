from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CountDownLatch"]

class CountDownLatch(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/CountDownLatch"
    __javaconstructor__ = [("(I)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    getCount = JavaMethod("()J")
    countDown = JavaMethod("()V")
    await = JavaMultipleMethod([("()V", False, False), ("(JLjava/util/concurrent/TimeUnit;)Z", False, False)])