from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractOwnableSynchronizer"]

class AbstractOwnableSynchronizer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/locks/AbstractOwnableSynchronizer"