from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BackingStoreException"]

class BackingStoreException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/prefs/BackingStoreException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/Throwable;)V", False)]