from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NamespaceSupport"]

class NamespaceSupport(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/helpers/NamespaceSupport"
    __javaconstructor__ = [("()V", False)]
    NSDECL = JavaStaticField("Ljava/lang/String;")
    XMLNS = JavaStaticField("Ljava/lang/String;")
    reset = JavaMethod("()V")
    pushContext = JavaMethod("()V")
    popContext = JavaMethod("()V")
    declarePrefix = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Z")
    processName = JavaMethod("(Ljava/lang/String;[Ljava/lang/String;Z)[Ljava/lang/String;")
    getURI = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getPrefixes = JavaMultipleMethod([("()Ljava/util/Enumeration;", False, False), ("(Ljava/lang/String;)Ljava/util/Enumeration;", False, False)])
    getPrefix = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getDeclaredPrefixes = JavaMethod("()Ljava/util/Enumeration;")
    setNamespaceDeclUris = JavaMethod("(Z)V")
    isNamespaceDeclUris = JavaMethod("()Z")