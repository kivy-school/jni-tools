from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppSearchSession"]

class AppSearchSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/AppSearchSession"
    getNamespaces = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    commitBlob = JavaMethod("(Ljava/util/Set;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    removeBlob = JavaMethod("(Ljava/util/Set;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    getStorageInfo = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    reportUsage = JavaMethod("(Landroid/app/appsearch/ReportUsageRequest;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    openBlobForWrite = JavaMethod("(Ljava/util/Set;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    searchSuggestion = JavaMethod("(Ljava/lang/String;Landroid/app/appsearch/SearchSuggestionSpec;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    setBlobVisibility = JavaMethod("(Landroid/app/appsearch/SetBlobVisibilityRequest;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    setSchema = JavaMethod("(Landroid/app/appsearch/SetSchemaRequest;Ljava/util/concurrent/Executor;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    openBlobForRead = JavaMethod("(Ljava/util/Set;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    getSchema = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    getByDocumentId = JavaMethod("(Landroid/app/appsearch/GetByDocumentIdRequest;Ljava/util/concurrent/Executor;Landroid/app/appsearch/BatchResultCallback;)V")
    remove = JavaMultipleMethod([("(Ljava/lang/String;Landroid/app/appsearch/SearchSpec;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V", False, False), ("(Landroid/app/appsearch/RemoveByDocumentIdRequest;Ljava/util/concurrent/Executor;Landroid/app/appsearch/BatchResultCallback;)V", False, False)])
    put = JavaMethod("(Landroid/app/appsearch/PutDocumentsRequest;Ljava/util/concurrent/Executor;Landroid/app/appsearch/BatchResultCallback;)V")
    close = JavaMethod("()V")
    search = JavaMethod("(Ljava/lang/String;Landroid/app/appsearch/SearchSpec;)Landroid/app/appsearch/SearchResults;")