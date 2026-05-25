from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyStoreBuilderParameters"]

class KeyStoreBuilderParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/KeyStoreBuilderParameters"
    __javaconstructor__ = [("(Ljava/security/KeyStore$Builder;)V", False), ("(Ljava/util/List;)V", False)]
    getParameters = JavaMethod("()Ljava/util/List;")