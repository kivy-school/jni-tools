from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LSInput"]

class LSInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/ls/LSInput"
    getSystemId = JavaMethod("()Ljava/lang/String;")
    setCharacterStream = JavaMethod("(Ljava/io/Reader;)V")
    getCharacterStream = JavaMethod("()Ljava/io/Reader;")
    setEncoding = JavaMethod("(Ljava/lang/String;)V")
    getEncoding = JavaMethod("()Ljava/lang/String;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    getPublicId = JavaMethod("()Ljava/lang/String;")
    setPublicId = JavaMethod("(Ljava/lang/String;)V")
    getBaseURI = JavaMethod("()Ljava/lang/String;")
    setByteStream = JavaMethod("(Ljava/io/InputStream;)V")
    getByteStream = JavaMethod("()Ljava/io/InputStream;")
    getStringData = JavaMethod("()Ljava/lang/String;")
    setStringData = JavaMethod("(Ljava/lang/String;)V")
    setBaseURI = JavaMethod("(Ljava/lang/String;)V")
    getCertifiedText = JavaMethod("()Z")
    setCertifiedText = JavaMethod("(Z)V")