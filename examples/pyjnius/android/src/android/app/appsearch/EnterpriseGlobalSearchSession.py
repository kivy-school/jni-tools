from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EnterpriseGlobalSearchSession"]

class EnterpriseGlobalSearchSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/EnterpriseGlobalSearchSession"
    openBlobForRead = JavaMethod("(Ljava/util/Set;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    getSchema = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    getByDocumentId = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Landroid/app/appsearch/GetByDocumentIdRequest;Ljava/util/concurrent/Executor;Landroid/app/appsearch/BatchResultCallback;)V")
    search = JavaMethod("(Ljava/lang/String;Landroid/app/appsearch/SearchSpec;)Landroid/app/appsearch/SearchResults;")