from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyChainAliasCallback"]

class KeyChainAliasCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/KeyChainAliasCallback"
    alias = JavaMethod("(Ljava/lang/String;)V")