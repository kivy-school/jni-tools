from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DocumentChangeInfo"]

class DocumentChangeInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/observer/DocumentChangeInfo"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/util/Set;)V", False)]
    getDatabaseName = JavaMethod("()Ljava/lang/String;")
    getSchemaName = JavaMethod("()Ljava/lang/String;")
    getChangedDocumentIds = JavaMethod("()Ljava/util/Set;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getNamespace = JavaMethod("()Ljava/lang/String;")