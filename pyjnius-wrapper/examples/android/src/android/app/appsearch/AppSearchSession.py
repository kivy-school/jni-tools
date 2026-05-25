from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppSearchSession"]

class AppSearchSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/AppSearchSession"
    setSchema = JavaMethod("(Landroid/app/appsearch/SetSchemaRequest;Ljava/util/concurrent/Executor;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    getSchema = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    getNamespaces = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    put = JavaMethod("(Landroid/app/appsearch/PutDocumentsRequest;Ljava/util/concurrent/Executor;Landroid/app/appsearch/BatchResultCallback;)V")
    getByDocumentId = JavaMethod("(Landroid/app/appsearch/GetByDocumentIdRequest;Ljava/util/concurrent/Executor;Landroid/app/appsearch/BatchResultCallback;)V")
    search = JavaMethod("(Ljava/lang/String;Landroid/app/appsearch/SearchSpec;)Landroid/app/appsearch/SearchResults;")
    searchSuggestion = JavaMethod("(Ljava/lang/String;Landroid/app/appsearch/SearchSuggestionSpec;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    reportUsage = JavaMethod("(Landroid/app/appsearch/ReportUsageRequest;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    remove = JavaMultipleMethod([("(Landroid/app/appsearch/RemoveByDocumentIdRequest;Ljava/util/concurrent/Executor;Landroid/app/appsearch/BatchResultCallback;)V", False, False), ("(Ljava/lang/String;Landroid/app/appsearch/SearchSpec;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V", False, False)])
    getStorageInfo = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    close = JavaMethod("()V")