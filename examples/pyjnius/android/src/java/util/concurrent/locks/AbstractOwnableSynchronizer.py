from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractOwnableSynchronizer"]

class AbstractOwnableSynchronizer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/locks/AbstractOwnableSynchronizer"
    __javaconstructor__ = [("()V", False)]
    setExclusiveOwnerThread = JavaMethod("(Ljava/lang/Thread;)V")
    getExclusiveOwnerThread = JavaMethod("()Ljava/lang/Thread;")