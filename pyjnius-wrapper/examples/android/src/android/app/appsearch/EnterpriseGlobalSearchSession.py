from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EnterpriseGlobalSearchSession"]

class EnterpriseGlobalSearchSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/EnterpriseGlobalSearchSession"
    search = JavaMethod("(Ljava/lang/String;Landroid/app/appsearch/SearchSpec;)Landroid/app/appsearch/SearchResults;")
    getByDocumentId = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Landroid/app/appsearch/GetByDocumentIdRequest;Ljava/util/concurrent/Executor;Landroid/app/appsearch/BatchResultCallback;)V")
    getSchema = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")