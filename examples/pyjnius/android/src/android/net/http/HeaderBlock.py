from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HeaderBlock"]

class HeaderBlock(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/HeaderBlock"
    __javaconstructor__ = [("()V", False)]
    getAsMap = JavaMethod("()Ljava/util/Map;")
    getAsList = JavaMethod("()Ljava/util/List;")