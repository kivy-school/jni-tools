from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NamespaceSupport"]

class NamespaceSupport(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/helpers/NamespaceSupport"
    __javaconstructor__ = [("()V", False)]
    XMLNS = JavaStaticField("Ljava/lang/String;")
    NSDECL = JavaStaticField("Ljava/lang/String;")
    reset = JavaMethod("()V")
    processName = JavaMethod("(Ljava/lang/String;[Ljava/lang/String;Z)[Ljava/lang/String;")
    getPrefix = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getURI = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getPrefixes = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/util/Enumeration;", False, False), ("()Ljava/util/Enumeration;", False, False)])
    declarePrefix = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Z")
    getDeclaredPrefixes = JavaMethod("()Ljava/util/Enumeration;")
    pushContext = JavaMethod("()V")
    popContext = JavaMethod("()V")
    setNamespaceDeclUris = JavaMethod("(Z)V")
    isNamespaceDeclUris = JavaMethod("()Z")