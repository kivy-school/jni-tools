from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class DocumentChangeInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/observer/DocumentChangeInfo"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/util/Set;)V", False)]
    getDatabaseName = JavaMethod("()Ljava/lang/String;")
    getChangedDocumentIds = JavaMethod("()Ljava/util/Set;")
    getSchemaName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getNamespace = JavaMethod("()Ljava/lang/String;")

class ObserverSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/observer/ObserverSpec"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getFilterSchemas = JavaMethod("()Ljava/util/Set;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/observer/ObserverSpec$Builder"
        __javaconstructor__ = [("()V", False)]
        addFilterSchemas = JavaMultipleMethod([("(Ljava/util/Collection;)Landroid/app/appsearch/observer/ObserverSpec$Builder;", False, False), ("([Ljava/lang/String;)Landroid/app/appsearch/observer/ObserverSpec$Builder;", False, True)])
        build = JavaMethod("()Landroid/app/appsearch/observer/ObserverSpec;")

class ObserverCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/observer/ObserverCallback"
    onDocumentChanged = JavaMethod("(Landroid/app/appsearch/observer/DocumentChangeInfo;)V")
    onSchemaChanged = JavaMethod("(Landroid/app/appsearch/observer/SchemaChangeInfo;)V")

class SchemaChangeInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/observer/SchemaChangeInfo"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/util/Set;)V", False)]
    getDatabaseName = JavaMethod("()Ljava/lang/String;")
    getChangedSchemaNames = JavaMethod("()Ljava/util/Set;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getPackageName = JavaMethod("()Ljava/lang/String;")