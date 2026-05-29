from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Security"]

class Security(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Security"
    insertProviderAt = JavaStaticMethod("(Ljava/security/Provider;I)I")
    getAlgorithmProperty = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")
    getAlgorithms = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/Set;")
    getProvider = JavaStaticMethod("(Ljava/lang/String;)Ljava/security/Provider;")
    getProperty = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    setProperty = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    addProvider = JavaStaticMethod("(Ljava/security/Provider;)I")
    removeProvider = JavaStaticMethod("(Ljava/lang/String;)V")
    getProviders = JavaMultipleMethod([("()[Ljava/security/Provider;", True, False), ("(Ljava/util/Map;)[Ljava/security/Provider;", True, False), ("(Ljava/lang/String;)[Ljava/security/Provider;", True, False)])