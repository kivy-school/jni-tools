from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IkeSaProposal"]

class IkeSaProposal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeSaProposal"
    getSupportedEncryptionAlgorithms = JavaStaticMethod("()Ljava/util/Set;")
    getSupportedIntegrityAlgorithms = JavaStaticMethod("()Ljava/util/Set;")
    getSupportedPseudorandomFunctions = JavaStaticMethod("()Ljava/util/Set;")
    getPseudorandomFunctions = JavaMethod("()Ljava/util/List;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/IkeSaProposal/Builder"
        __javaconstructor__ = [("()V", False)]
        addEncryptionAlgorithm = JavaMethod("(II)Landroid/net/ipsec/ike/IkeSaProposal$Builder;")
        addIntegrityAlgorithm = JavaMethod("(I)Landroid/net/ipsec/ike/IkeSaProposal$Builder;")
        addDhGroup = JavaMethod("(I)Landroid/net/ipsec/ike/IkeSaProposal$Builder;")
        addPseudorandomFunction = JavaMethod("(I)Landroid/net/ipsec/ike/IkeSaProposal$Builder;")
        build = JavaMethod("()Landroid/net/ipsec/ike/IkeSaProposal;")