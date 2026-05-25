from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FontRequest"]

class FontRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/provider/FontRequest"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/util/List;)V", False)]
    getProviderAuthority = JavaMethod("()Ljava/lang/String;")
    getProviderPackage = JavaMethod("()Ljava/lang/String;")
    getQuery = JavaMethod("()Ljava/lang/String;")
    getCertificates = JavaMethod("()Ljava/util/List;")
    toString = JavaMethod("()Ljava/lang/String;")