from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DisplayHashManager"]

class DisplayHashManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/displayhash/DisplayHashManager"
    verifyDisplayHash = JavaMethod("(Landroid/view/displayhash/DisplayHash;)Landroid/view/displayhash/VerifiedDisplayHash;")
    getSupportedHashAlgorithms = JavaMethod("()Ljava/util/Set;")