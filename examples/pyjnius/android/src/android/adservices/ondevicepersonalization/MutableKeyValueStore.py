from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MutableKeyValueStore"]

class MutableKeyValueStore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/MutableKeyValueStore"
    remove = JavaMethod("(Ljava/lang/String;)[B")
    put = JavaMethod("(Ljava/lang/String;[B)[B")