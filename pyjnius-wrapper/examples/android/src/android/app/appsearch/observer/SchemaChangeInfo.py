from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SchemaChangeInfo"]

class SchemaChangeInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/observer/SchemaChangeInfo"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/util/Set;)V", False)]
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getDatabaseName = JavaMethod("()Ljava/lang/String;")
    getChangedSchemaNames = JavaMethod("()Ljava/util/Set;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")