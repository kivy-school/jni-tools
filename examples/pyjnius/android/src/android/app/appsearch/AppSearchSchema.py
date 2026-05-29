from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppSearchSchema"]

class AppSearchSchema(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/AppSearchSchema"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getProperties = JavaMethod("()Ljava/util/List;")
    getSchemaType = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getParentTypes = JavaMethod("()Ljava/util/List;")

    class StringPropertyConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/AppSearchSchema$StringPropertyConfig"
        INDEXING_TYPE_EXACT_TERMS = JavaStaticField("I")
        INDEXING_TYPE_NONE = JavaStaticField("I")
        INDEXING_TYPE_PREFIXES = JavaStaticField("I")
        JOINABLE_VALUE_TYPE_NONE = JavaStaticField("I")
        JOINABLE_VALUE_TYPE_QUALIFIED_ID = JavaStaticField("I")
        TOKENIZER_TYPE_NONE = JavaStaticField("I")
        TOKENIZER_TYPE_PLAIN = JavaStaticField("I")
        TOKENIZER_TYPE_RFC822 = JavaStaticField("I")
        TOKENIZER_TYPE_VERBATIM = JavaStaticField("I")
        CARDINALITY_OPTIONAL = JavaStaticField("I")
        CARDINALITY_REPEATED = JavaStaticField("I")
        CARDINALITY_REQUIRED = JavaStaticField("I")
        getIndexingType = JavaMethod("()I")
        getJoinableValueType = JavaMethod("()I")
        getTokenizerType = JavaMethod("()I")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/app/appsearch/AppSearchSchema$StringPropertyConfig$Builder"
            __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
            setIndexingType = JavaMethod("(I)Landroid/app/appsearch/AppSearchSchema$StringPropertyConfig$Builder;")
            setCardinality = JavaMethod("(I)Landroid/app/appsearch/AppSearchSchema$StringPropertyConfig$Builder;")
            setJoinableValueType = JavaMethod("(I)Landroid/app/appsearch/AppSearchSchema$StringPropertyConfig$Builder;")
            setTokenizerType = JavaMethod("(I)Landroid/app/appsearch/AppSearchSchema$StringPropertyConfig$Builder;")
            build = JavaMethod("()Landroid/app/appsearch/AppSearchSchema$StringPropertyConfig;")

    class PropertyConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/AppSearchSchema$PropertyConfig"
        CARDINALITY_OPTIONAL = JavaStaticField("I")
        CARDINALITY_REPEATED = JavaStaticField("I")
        CARDINALITY_REQUIRED = JavaStaticField("I")
        getCardinality = JavaMethod("()I")
        getName = JavaMethod("()Ljava/lang/String;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")
        hashCode = JavaMethod("()I")

    class LongPropertyConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/AppSearchSchema$LongPropertyConfig"
        INDEXING_TYPE_NONE = JavaStaticField("I")
        INDEXING_TYPE_RANGE = JavaStaticField("I")
        CARDINALITY_OPTIONAL = JavaStaticField("I")
        CARDINALITY_REPEATED = JavaStaticField("I")
        CARDINALITY_REQUIRED = JavaStaticField("I")
        getIndexingType = JavaMethod("()I")
        isScoringEnabled = JavaMethod("()Z")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/app/appsearch/AppSearchSchema$LongPropertyConfig$Builder"
            __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
            setScoringEnabled = JavaMethod("(Z)Landroid/app/appsearch/AppSearchSchema$LongPropertyConfig$Builder;")
            setIndexingType = JavaMethod("(I)Landroid/app/appsearch/AppSearchSchema$LongPropertyConfig$Builder;")
            setCardinality = JavaMethod("(I)Landroid/app/appsearch/AppSearchSchema$LongPropertyConfig$Builder;")
            build = JavaMethod("()Landroid/app/appsearch/AppSearchSchema$LongPropertyConfig;")

    class EmbeddingPropertyConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/AppSearchSchema$EmbeddingPropertyConfig"
        INDEXING_TYPE_NONE = JavaStaticField("I")
        INDEXING_TYPE_SIMILARITY = JavaStaticField("I")
        QUANTIZATION_TYPE_8_BIT = JavaStaticField("I")
        QUANTIZATION_TYPE_NONE = JavaStaticField("I")
        CARDINALITY_OPTIONAL = JavaStaticField("I")
        CARDINALITY_REPEATED = JavaStaticField("I")
        CARDINALITY_REQUIRED = JavaStaticField("I")
        getIndexingType = JavaMethod("()I")
        getQuantizationType = JavaMethod("()I")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/app/appsearch/AppSearchSchema$EmbeddingPropertyConfig$Builder"
            __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
            setQuantizationType = JavaMethod("(I)Landroid/app/appsearch/AppSearchSchema$EmbeddingPropertyConfig$Builder;")
            setIndexingType = JavaMethod("(I)Landroid/app/appsearch/AppSearchSchema$EmbeddingPropertyConfig$Builder;")
            setCardinality = JavaMethod("(I)Landroid/app/appsearch/AppSearchSchema$EmbeddingPropertyConfig$Builder;")
            build = JavaMethod("()Landroid/app/appsearch/AppSearchSchema$EmbeddingPropertyConfig;")

    class DoublePropertyConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/AppSearchSchema$DoublePropertyConfig"
        CARDINALITY_OPTIONAL = JavaStaticField("I")
        CARDINALITY_REPEATED = JavaStaticField("I")
        CARDINALITY_REQUIRED = JavaStaticField("I")
        isScoringEnabled = JavaMethod("()Z")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/app/appsearch/AppSearchSchema$DoublePropertyConfig$Builder"
            __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
            setScoringEnabled = JavaMethod("(Z)Landroid/app/appsearch/AppSearchSchema$DoublePropertyConfig$Builder;")
            setCardinality = JavaMethod("(I)Landroid/app/appsearch/AppSearchSchema$DoublePropertyConfig$Builder;")
            build = JavaMethod("()Landroid/app/appsearch/AppSearchSchema$DoublePropertyConfig;")

    class DocumentPropertyConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/AppSearchSchema$DocumentPropertyConfig"
        CARDINALITY_OPTIONAL = JavaStaticField("I")
        CARDINALITY_REPEATED = JavaStaticField("I")
        CARDINALITY_REQUIRED = JavaStaticField("I")
        getSchemaType = JavaMethod("()Ljava/lang/String;")
        getIndexableNestedProperties = JavaMethod("()Ljava/util/List;")
        shouldIndexNestedProperties = JavaMethod("()Z")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/app/appsearch/AppSearchSchema$DocumentPropertyConfig$Builder"
            __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
            addIndexableNestedProperties = JavaMultipleMethod([("(Ljava/util/Collection;)Landroid/app/appsearch/AppSearchSchema$DocumentPropertyConfig$Builder;", False, False), ("([Ljava/lang/String;)Landroid/app/appsearch/AppSearchSchema$DocumentPropertyConfig$Builder;", False, True)])
            addIndexableNestedPropertyPaths = JavaMultipleMethod([("([Landroid/app/appsearch/PropertyPath;)Landroid/app/appsearch/AppSearchSchema$DocumentPropertyConfig$Builder;", False, True), ("(Ljava/util/Collection;)Landroid/app/appsearch/AppSearchSchema$DocumentPropertyConfig$Builder;", False, False)])
            setShouldIndexNestedProperties = JavaMethod("(Z)Landroid/app/appsearch/AppSearchSchema$DocumentPropertyConfig$Builder;")
            setCardinality = JavaMethod("(I)Landroid/app/appsearch/AppSearchSchema$DocumentPropertyConfig$Builder;")
            build = JavaMethod("()Landroid/app/appsearch/AppSearchSchema$DocumentPropertyConfig;")

    class BytesPropertyConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/AppSearchSchema$BytesPropertyConfig"
        CARDINALITY_OPTIONAL = JavaStaticField("I")
        CARDINALITY_REPEATED = JavaStaticField("I")
        CARDINALITY_REQUIRED = JavaStaticField("I")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/app/appsearch/AppSearchSchema$BytesPropertyConfig$Builder"
            __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
            setCardinality = JavaMethod("(I)Landroid/app/appsearch/AppSearchSchema$BytesPropertyConfig$Builder;")
            build = JavaMethod("()Landroid/app/appsearch/AppSearchSchema$BytesPropertyConfig;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/AppSearchSchema$Builder"
        __javaconstructor__ = [("(Landroid/app/appsearch/AppSearchSchema;)V", False), ("(Ljava/lang/String;)V", False)]
        setSchemaType = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/AppSearchSchema$Builder;")
        build = JavaMethod("()Landroid/app/appsearch/AppSearchSchema;")
        addParentType = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/AppSearchSchema$Builder;")
        clearProperties = JavaMethod("()Landroid/app/appsearch/AppSearchSchema$Builder;")
        clearParentTypes = JavaMethod("()Landroid/app/appsearch/AppSearchSchema$Builder;")
        addProperty = JavaMethod("(Landroid/app/appsearch/AppSearchSchema$PropertyConfig;)Landroid/app/appsearch/AppSearchSchema$Builder;")

    class BooleanPropertyConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/AppSearchSchema$BooleanPropertyConfig"
        CARDINALITY_OPTIONAL = JavaStaticField("I")
        CARDINALITY_REPEATED = JavaStaticField("I")
        CARDINALITY_REQUIRED = JavaStaticField("I")
        isScoringEnabled = JavaMethod("()Z")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/app/appsearch/AppSearchSchema$BooleanPropertyConfig$Builder"
            __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
            setScoringEnabled = JavaMethod("(Z)Landroid/app/appsearch/AppSearchSchema$BooleanPropertyConfig$Builder;")
            setCardinality = JavaMethod("(I)Landroid/app/appsearch/AppSearchSchema$BooleanPropertyConfig$Builder;")
            build = JavaMethod("()Landroid/app/appsearch/AppSearchSchema$BooleanPropertyConfig;")

    class BlobHandlePropertyConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/AppSearchSchema$BlobHandlePropertyConfig"
        CARDINALITY_OPTIONAL = JavaStaticField("I")
        CARDINALITY_REPEATED = JavaStaticField("I")
        CARDINALITY_REQUIRED = JavaStaticField("I")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/app/appsearch/AppSearchSchema$BlobHandlePropertyConfig$Builder"
            __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
            setCardinality = JavaMethod("(I)Landroid/app/appsearch/AppSearchSchema$BlobHandlePropertyConfig$Builder;")
            build = JavaMethod("()Landroid/app/appsearch/AppSearchSchema$BlobHandlePropertyConfig;")