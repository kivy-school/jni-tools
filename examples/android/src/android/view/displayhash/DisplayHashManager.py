from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DisplayHashManager"]

class DisplayHashManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/displayhash/DisplayHashManager"
    getSupportedHashAlgorithms = JavaMethod("()Ljava/util/Set;")
    verifyDisplayHash = JavaMethod("(Landroid/view/displayhash/DisplayHash;)Landroid/view/displayhash/VerifiedDisplayHash;")