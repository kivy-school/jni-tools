from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class LSParser(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/ls/LSParser"
    ACTION_APPEND_AS_CHILDREN = JavaStaticField("S")
    ACTION_REPLACE_CHILDREN = JavaStaticField("S")
    ACTION_INSERT_BEFORE = JavaStaticField("S")
    ACTION_INSERT_AFTER = JavaStaticField("S")
    ACTION_REPLACE = JavaStaticField("S")
    getDomConfig = JavaMethod("()Lorg/w3c/dom/DOMConfiguration;")
    setFilter = JavaMethod("(Lorg/w3c/dom/ls/LSParserFilter;)V")
    abort = JavaMethod("()V")
    getAsync = JavaMethod("()Z")
    getBusy = JavaMethod("()Z")
    parseURI = JavaMethod("(Ljava/lang/String;)Lorg/w3c/dom/Document;")
    parseWithContext = JavaMethod("(Lorg/w3c/dom/ls/LSInput;Lorg/w3c/dom/Node;S)Lorg/w3c/dom/Node;")
    parse = JavaMethod("(Lorg/w3c/dom/ls/LSInput;)Lorg/w3c/dom/Document;")
    getFilter = JavaMethod("()Lorg/w3c/dom/ls/LSParserFilter;")

class LSInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/ls/LSInput"
    getSystemId = JavaMethod("()Ljava/lang/String;")
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
    getEncoding = JavaMethod("()Ljava/lang/String;")
    setEncoding = JavaMethod("(Ljava/lang/String;)V")
    setCharacterStream = JavaMethod("(Ljava/io/Reader;)V")
    getCharacterStream = JavaMethod("()Ljava/io/Reader;")

class LSResourceResolver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/ls/LSResourceResolver"
    resolveResource = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Lorg/w3c/dom/ls/LSInput;")

class DOMImplementationLS(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/ls/DOMImplementationLS"
    MODE_SYNCHRONOUS = JavaStaticField("S")
    MODE_ASYNCHRONOUS = JavaStaticField("S")
    createLSParser = JavaMethod("(SLjava/lang/String;)Lorg/w3c/dom/ls/LSParser;")
    createLSSerializer = JavaMethod("()Lorg/w3c/dom/ls/LSSerializer;")
    createLSInput = JavaMethod("()Lorg/w3c/dom/ls/LSInput;")
    createLSOutput = JavaMethod("()Lorg/w3c/dom/ls/LSOutput;")

class LSParserFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/ls/LSParserFilter"
    FILTER_ACCEPT = JavaStaticField("S")
    FILTER_REJECT = JavaStaticField("S")
    FILTER_SKIP = JavaStaticField("S")
    FILTER_INTERRUPT = JavaStaticField("S")
    acceptNode = JavaMethod("(Lorg/w3c/dom/Node;)S")
    getWhatToShow = JavaMethod("()I")
    startElement = JavaMethod("(Lorg/w3c/dom/Element;)S")

class LSSerializer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/ls/LSSerializer"
    getDomConfig = JavaMethod("()Lorg/w3c/dom/DOMConfiguration;")
    setFilter = JavaMethod("(Lorg/w3c/dom/ls/LSSerializerFilter;)V")
    getNewLine = JavaMethod("()Ljava/lang/String;")
    setNewLine = JavaMethod("(Ljava/lang/String;)V")
    writeToURI = JavaMethod("(Lorg/w3c/dom/Node;Ljava/lang/String;)Z")
    writeToString = JavaMethod("(Lorg/w3c/dom/Node;)Ljava/lang/String;")
    write = JavaMethod("(Lorg/w3c/dom/Node;Lorg/w3c/dom/ls/LSOutput;)Z")
    getFilter = JavaMethod("()Lorg/w3c/dom/ls/LSSerializerFilter;")

class LSOutput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/ls/LSOutput"
    getSystemId = JavaMethod("()Ljava/lang/String;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    setByteStream = JavaMethod("(Ljava/io/OutputStream;)V")
    getByteStream = JavaMethod("()Ljava/io/OutputStream;")
    getEncoding = JavaMethod("()Ljava/lang/String;")
    setEncoding = JavaMethod("(Ljava/lang/String;)V")
    setCharacterStream = JavaMethod("(Ljava/io/Writer;)V")
    getCharacterStream = JavaMethod("()Ljava/io/Writer;")

class LSException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/ls/LSException"
    __javaconstructor__ = [("(SLjava/lang/String;)V", False)]
    code = JavaField("S")
    PARSE_ERR = JavaStaticField("S")
    SERIALIZE_ERR = JavaStaticField("S")