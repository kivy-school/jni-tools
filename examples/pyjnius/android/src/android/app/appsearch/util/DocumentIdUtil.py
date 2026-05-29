from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DocumentIdUtil"]

class DocumentIdUtil(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/util/DocumentIdUtil"
    createQualifiedId = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;Landroid/app/appsearch/GenericDocument;)Ljava/lang/String;", True, False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", True, False)])