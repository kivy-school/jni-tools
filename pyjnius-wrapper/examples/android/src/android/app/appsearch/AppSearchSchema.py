from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppSearchSchema"]

class AppSearchSchema(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/AppSearchSchema"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    toString = JavaMethod("()Ljava/lang/String;")
    getSchemaType = JavaMethod("()Ljava/lang/String;")
    getProperties = JavaMethod("()Ljava/util/List;")
    getParentTypes = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class BooleanPropertyConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/AppSearchSchema/BooleanPropertyConfig"

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/app/appsearch/AppSearchSchema/BooleanPropertyConfig/Builder"
            __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
            setCardinality = JavaMethod("(I)Landroid/app/appsearch/AppSearchSchema$BooleanPropertyConfig$Builder;")
            build = JavaMethod("()Landroid/app/appsearch/AppSearchSchema$BooleanPropertyConfig;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/AppSearchSchema/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        addProperty = JavaMethod("(Landroid/app/appsearch/AppSearchSchema$PropertyConfig;)Landroid/app/appsearch/AppSearchSchema$Builder;")
        addParentType = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/AppSearchSchema$Builder;")
        build = JavaMethod("()Landroid/app/appsearch/AppSearchSchema;")

    class BytesPropertyConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/AppSearchSchema/BytesPropertyConfig"

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/app/appsearch/AppSearchSchema/BytesPropertyConfig/Builder"
            __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
            setCardinality = JavaMethod("(I)Landroid/app/appsearch/AppSearchSchema$BytesPropertyConfig$Builder;")
            build = JavaMethod("()Landroid/app/appsearch/AppSearchSchema$BytesPropertyConfig;")

    class DocumentPropertyConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/AppSearchSchema/DocumentPropertyConfig"
        getSchemaType = JavaMethod("()Ljava/lang/String;")
        shouldIndexNestedProperties = JavaMethod("()Z")
        getIndexableNestedProperties = JavaMethod("()Ljava/util/List;")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/app/appsearch/AppSearchSchema/DocumentPropertyConfig/Builder"
            __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
            setCardinality = JavaMethod("(I)Landroid/app/appsearch/AppSearchSchema$DocumentPropertyConfig$Builder;")
            setShouldIndexNestedProperties = JavaMethod("(Z)Landroid/app/appsearch/AppSearchSchema$DocumentPropertyConfig$Builder;")
            addIndexableNestedProperties = JavaMultipleMethod([("([Ljava/lang/String;)Landroid/app/appsearch/AppSearchSchema$DocumentPropertyConfig$Builder;", False, True), ("(Ljava/util/Collection;)Landroid/app/appsearch/AppSearchSchema$DocumentPropertyConfig$Builder;", False, False)])
            addIndexableNestedPropertyPaths = JavaMultipleMethod([("([Landroid/app/appsearch/PropertyPath;)Landroid/app/appsearch/AppSearchSchema$DocumentPropertyConfig$Builder;", False, True), ("(Ljava/util/Collection;)Landroid/app/appsearch/AppSearchSchema$DocumentPropertyConfig$Builder;", False, False)])
            build = JavaMethod("()Landroid/app/appsearch/AppSearchSchema$DocumentPropertyConfig;")

    class DoublePropertyConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/AppSearchSchema/DoublePropertyConfig"

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/app/appsearch/AppSearchSchema/DoublePropertyConfig/Builder"
            __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
            setCardinality = JavaMethod("(I)Landroid/app/appsearch/AppSearchSchema$DoublePropertyConfig$Builder;")
            build = JavaMethod("()Landroid/app/appsearch/AppSearchSchema$DoublePropertyConfig;")

    class LongPropertyConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/AppSearchSchema/LongPropertyConfig"
        INDEXING_TYPE_NONE = JavaStaticField("I")
        INDEXING_TYPE_RANGE = JavaStaticField("I")
        getIndexingType = JavaMethod("()I")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/app/appsearch/AppSearchSchema/LongPropertyConfig/Builder"
            __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
            setCardinality = JavaMethod("(I)Landroid/app/appsearch/AppSearchSchema$LongPropertyConfig$Builder;")
            setIndexingType = JavaMethod("(I)Landroid/app/appsearch/AppSearchSchema$LongPropertyConfig$Builder;")
            build = JavaMethod("()Landroid/app/appsearch/AppSearchSchema$LongPropertyConfig;")

    class PropertyConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/AppSearchSchema/PropertyConfig"
        CARDINALITY_OPTIONAL = JavaStaticField("I")
        CARDINALITY_REPEATED = JavaStaticField("I")
        CARDINALITY_REQUIRED = JavaStaticField("I")
        toString = JavaMethod("()Ljava/lang/String;")
        getName = JavaMethod("()Ljava/lang/String;")
        getCardinality = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class StringPropertyConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/AppSearchSchema/StringPropertyConfig"
        INDEXING_TYPE_EXACT_TERMS = JavaStaticField("I")
        INDEXING_TYPE_NONE = JavaStaticField("I")
        INDEXING_TYPE_PREFIXES = JavaStaticField("I")
        JOINABLE_VALUE_TYPE_NONE = JavaStaticField("I")
        JOINABLE_VALUE_TYPE_QUALIFIED_ID = JavaStaticField("I")
        TOKENIZER_TYPE_NONE = JavaStaticField("I")
        TOKENIZER_TYPE_PLAIN = JavaStaticField("I")
        TOKENIZER_TYPE_RFC822 = JavaStaticField("I")
        TOKENIZER_TYPE_VERBATIM = JavaStaticField("I")
        getIndexingType = JavaMethod("()I")
        getTokenizerType = JavaMethod("()I")
        getJoinableValueType = JavaMethod("()I")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/app/appsearch/AppSearchSchema/StringPropertyConfig/Builder"
            __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
            setCardinality = JavaMethod("(I)Landroid/app/appsearch/AppSearchSchema$StringPropertyConfig$Builder;")
            setIndexingType = JavaMethod("(I)Landroid/app/appsearch/AppSearchSchema$StringPropertyConfig$Builder;")
            setTokenizerType = JavaMethod("(I)Landroid/app/appsearch/AppSearchSchema$StringPropertyConfig$Builder;")
            setJoinableValueType = JavaMethod("(I)Landroid/app/appsearch/AppSearchSchema$StringPropertyConfig$Builder;")
            build = JavaMethod("()Landroid/app/appsearch/AppSearchSchema$StringPropertyConfig;")