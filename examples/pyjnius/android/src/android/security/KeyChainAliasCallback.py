from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyChainAliasCallback"]

class KeyChainAliasCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/KeyChainAliasCallback"
    alias = JavaMethod("(Ljava/lang/String;)V")