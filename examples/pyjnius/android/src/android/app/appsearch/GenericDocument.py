from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GenericDocument"]

class GenericDocument(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/GenericDocument"
    getProperty = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getId = JavaMethod("()Ljava/lang/String;")
    getPropertyLong = JavaMethod("(Ljava/lang/String;)J")
    getPropertyString = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getTtlMillis = JavaMethod("()J")
    getSchemaType = JavaMethod("()Ljava/lang/String;")
    getPropertyNames = JavaMethod("()Ljava/util/Set;")
    getPropertyBoolean = JavaMethod("(Ljava/lang/String;)Z")
    getPropertyBytes = JavaMethod("(Ljava/lang/String;)[B")
    getScore = JavaMethod("()I")
    getPropertyBlobHandle = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/AppSearchBlobHandle;")
    getPropertyBlobHandleArray = JavaMethod("(Ljava/lang/String;)[Landroid/app/appsearch/AppSearchBlobHandle;")
    getPropertyBooleanArray = JavaMethod("(Ljava/lang/String;)[Z")
    getPropertyBytesArray = JavaMethod("(Ljava/lang/String;)[[B")
    getPropertyDocument = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/GenericDocument;")
    getPropertyDocumentArray = JavaMethod("(Ljava/lang/String;)[Landroid/app/appsearch/GenericDocument;")
    getPropertyDouble = JavaMethod("(Ljava/lang/String;)D")
    getMaxIndexedProperties = JavaStaticMethod("()I")
    getCreationTimestampMillis = JavaMethod("()J")
    getPropertyDoubleArray = JavaMethod("(Ljava/lang/String;)[D")
    getPropertyEmbedding = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/EmbeddingVector;")
    getPropertyEmbeddingArray = JavaMethod("(Ljava/lang/String;)[Landroid/app/appsearch/EmbeddingVector;")
    getPropertyLongArray = JavaMethod("(Ljava/lang/String;)[J")
    getPropertyStringArray = JavaMethod("(Ljava/lang/String;)[Ljava/lang/String;")
    getNamespace = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/GenericDocument$Builder"
        __javaconstructor__ = [("(Landroid/app/appsearch/GenericDocument;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]
        setCreationTimestampMillis = JavaMethod("(J)Landroid/app/appsearch/GenericDocument$Builder;")
        setPropertyDouble = JavaMethod("(Ljava/lang/String;[D)Landroid/app/appsearch/GenericDocument$Builder;", varargs=True)
        setPropertyEmbedding = JavaMethod("(Ljava/lang/String;[Landroid/app/appsearch/EmbeddingVector;)Landroid/app/appsearch/GenericDocument$Builder;", varargs=True)
        setPropertyLong = JavaMethod("(Ljava/lang/String;[J)Landroid/app/appsearch/GenericDocument$Builder;", varargs=True)
        setPropertyString = JavaMethod("(Ljava/lang/String;[Ljava/lang/String;)Landroid/app/appsearch/GenericDocument$Builder;", varargs=True)
        setSchemaType = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/GenericDocument$Builder;")
        setTtlMillis = JavaMethod("(J)Landroid/app/appsearch/GenericDocument$Builder;")
        setNamespace = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/GenericDocument$Builder;")
        setPropertyBlobHandle = JavaMethod("(Ljava/lang/String;[Landroid/app/appsearch/AppSearchBlobHandle;)Landroid/app/appsearch/GenericDocument$Builder;", varargs=True)
        setPropertyBoolean = JavaMethod("(Ljava/lang/String;[Z)Landroid/app/appsearch/GenericDocument$Builder;", varargs=True)
        setPropertyBytes = JavaMethod("(Ljava/lang/String;[[B)Landroid/app/appsearch/GenericDocument$Builder;", varargs=True)
        setPropertyDocument = JavaMethod("(Ljava/lang/String;[Landroid/app/appsearch/GenericDocument;)Landroid/app/appsearch/GenericDocument$Builder;", varargs=True)
        clearProperty = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/GenericDocument$Builder;")
        setScore = JavaMethod("(I)Landroid/app/appsearch/GenericDocument$Builder;")
        setId = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/GenericDocument$Builder;")
        build = JavaMethod("()Landroid/app/appsearch/GenericDocument;")