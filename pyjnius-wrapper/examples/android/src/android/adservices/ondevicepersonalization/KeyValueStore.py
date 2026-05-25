from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyValueStore"]

class KeyValueStore(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/KeyValueStore"
    get = JavaMethod("(Ljava/lang/String;)[B")
    keySet = JavaMethod("()Ljava/util/Set;")