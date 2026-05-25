from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChildSaProposal"]

class ChildSaProposal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/ChildSaProposal"
    getSupportedEncryptionAlgorithms = JavaStaticMethod("()Ljava/util/Set;")
    getSupportedIntegrityAlgorithms = JavaStaticMethod("()Ljava/util/Set;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/ChildSaProposal/Builder"
        __javaconstructor__ = [("()V", False)]
        addEncryptionAlgorithm = JavaMethod("(II)Landroid/net/ipsec/ike/ChildSaProposal$Builder;")
        addIntegrityAlgorithm = JavaMethod("(I)Landroid/net/ipsec/ike/ChildSaProposal$Builder;")
        addDhGroup = JavaMethod("(I)Landroid/net/ipsec/ike/ChildSaProposal$Builder;")
        build = JavaMethod("()Landroid/net/ipsec/ike/ChildSaProposal;")