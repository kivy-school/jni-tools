from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CountDownLatch"]

class CountDownLatch(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/CountDownLatch"
    __javaconstructor__ = [("(I)V", False)]
    await = JavaMultipleMethod([("()V", False, False), ("(JLjava/util/concurrent/TimeUnit;)Z", False, False)])
    countDown = JavaMethod("()V")
    getCount = JavaMethod("()J")
    toString = JavaMethod("()Ljava/lang/String;")