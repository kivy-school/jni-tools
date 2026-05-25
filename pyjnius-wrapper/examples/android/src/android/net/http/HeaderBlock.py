from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HeaderBlock"]

class HeaderBlock(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/HeaderBlock"
    __javaconstructor__ = [("()V", False)]
    getAsList = JavaMethod("()Ljava/util/List;")
    getAsMap = JavaMethod("()Ljava/util/Map;")