from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MutableKeyValueStore"]

class MutableKeyValueStore(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/MutableKeyValueStore"
    put = JavaMethod("(Ljava/lang/String;[B)[B")
    remove = JavaMethod("(Ljava/lang/String;)[B")