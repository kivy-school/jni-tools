from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LSInput"]

class LSInput(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/ls/LSInput"
    getCharacterStream = JavaMethod("()Ljava/io/Reader;")
    setCharacterStream = JavaMethod("(Ljava/io/Reader;)V")
    getByteStream = JavaMethod("()Ljava/io/InputStream;")
    setByteStream = JavaMethod("(Ljava/io/InputStream;)V")
    getStringData = JavaMethod("()Ljava/lang/String;")
    setStringData = JavaMethod("(Ljava/lang/String;)V")
    getSystemId = JavaMethod("()Ljava/lang/String;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    getPublicId = JavaMethod("()Ljava/lang/String;")
    setPublicId = JavaMethod("(Ljava/lang/String;)V")
    getBaseURI = JavaMethod("()Ljava/lang/String;")
    setBaseURI = JavaMethod("(Ljava/lang/String;)V")
    getEncoding = JavaMethod("()Ljava/lang/String;")
    setEncoding = JavaMethod("(Ljava/lang/String;)V")
    getCertifiedText = JavaMethod("()Z")
    setCertifiedText = JavaMethod("(Z)V")