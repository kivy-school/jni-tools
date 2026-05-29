from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChildSessionConfiguration"]

class ChildSessionConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/ChildSessionConfiguration"
    getInboundTrafficSelectors = JavaMethod("()Ljava/util/List;")
    getOutboundTrafficSelectors = JavaMethod("()Ljava/util/List;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/ChildSessionConfiguration$Builder"
        __javaconstructor__ = [("(Ljava/util/List;Ljava/util/List;)V", False)]
        build = JavaMethod("()Landroid/net/ipsec/ike/ChildSessionConfiguration;")