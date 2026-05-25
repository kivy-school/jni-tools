from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GenericDocument"]

class GenericDocument(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/GenericDocument"
    __javaconstructor__ = [("(Landroid/app/appsearch/GenericDocument;)V", False)]
    getMaxIndexedProperties = JavaStaticMethod("()I")
    getId = JavaMethod("()Ljava/lang/String;")
    getNamespace = JavaMethod("()Ljava/lang/String;")
    getSchemaType = JavaMethod("()Ljava/lang/String;")
    getCreationTimestampMillis = JavaMethod("()J")
    getTtlMillis = JavaMethod("()J")
    getScore = JavaMethod("()I")
    getPropertyNames = JavaMethod("()Ljava/util/Set;")
    getProperty = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    getPropertyString = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getPropertyLong = JavaMethod("(Ljava/lang/String;)J")
    getPropertyDouble = JavaMethod("(Ljava/lang/String;)D")
    getPropertyBoolean = JavaMethod("(Ljava/lang/String;)Z")
    getPropertyBytes = JavaMethod("(Ljava/lang/String;)[B")
    getPropertyDocument = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/GenericDocument;")
    getPropertyStringArray = JavaMethod("(Ljava/lang/String;)[Ljava/lang/String;")
    getPropertyLongArray = JavaMethod("(Ljava/lang/String;)[J")
    getPropertyDoubleArray = JavaMethod("(Ljava/lang/String;)[D")
    getPropertyBooleanArray = JavaMethod("(Ljava/lang/String;)[Z")
    getPropertyBytesArray = JavaMethod("(Ljava/lang/String;)[[B")
    getPropertyDocumentArray = JavaMethod("(Ljava/lang/String;)[Landroid/app/appsearch/GenericDocument;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/GenericDocument/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False), ("(Landroid/app/appsearch/GenericDocument;)V", False)]
        setNamespace = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/GenericDocument$Builder;")
        setId = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/GenericDocument$Builder;")
        setSchemaType = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/GenericDocument$Builder;")
        setScore = JavaMethod("(I)Landroid/app/appsearch/GenericDocument$Builder;")
        setCreationTimestampMillis = JavaMethod("(J)Landroid/app/appsearch/GenericDocument$Builder;")
        setTtlMillis = JavaMethod("(J)Landroid/app/appsearch/GenericDocument$Builder;")
        setPropertyString = JavaMethod("(Ljava/lang/String;[Ljava/lang/String;)Landroid/app/appsearch/GenericDocument$Builder;", varargs=True)
        setPropertyBoolean = JavaMethod("(Ljava/lang/String;[Z)Landroid/app/appsearch/GenericDocument$Builder;", varargs=True)
        setPropertyLong = JavaMethod("(Ljava/lang/String;[J)Landroid/app/appsearch/GenericDocument$Builder;", varargs=True)
        setPropertyDouble = JavaMethod("(Ljava/lang/String;[D)Landroid/app/appsearch/GenericDocument$Builder;", varargs=True)
        setPropertyBytes = JavaMethod("(Ljava/lang/String;[[B)Landroid/app/appsearch/GenericDocument$Builder;", varargs=True)
        setPropertyDocument = JavaMethod("(Ljava/lang/String;[Landroid/app/appsearch/GenericDocument;)Landroid/app/appsearch/GenericDocument$Builder;", varargs=True)
        clearProperty = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/GenericDocument$Builder;")
        build = JavaMethod("()Landroid/app/appsearch/GenericDocument;")