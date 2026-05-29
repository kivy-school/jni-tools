from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GlobalSearchSession"]

class GlobalSearchSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/GlobalSearchSession"
    openBlobForRead = JavaMethod("(Ljava/util/Set;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    getSchema = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    getByDocumentId = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Landroid/app/appsearch/GetByDocumentIdRequest;Ljava/util/concurrent/Executor;Landroid/app/appsearch/BatchResultCallback;)V")
    registerObserverCallback = JavaMethod("(Ljava/lang/String;Landroid/app/appsearch/observer/ObserverSpec;Ljava/util/concurrent/Executor;Landroid/app/appsearch/observer/ObserverCallback;)V")
    reportSystemUsage = JavaMethod("(Landroid/app/appsearch/ReportSystemUsageRequest;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    unregisterObserverCallback = JavaMethod("(Ljava/lang/String;Landroid/app/appsearch/observer/ObserverCallback;)V")
    close = JavaMethod("()V")
    search = JavaMethod("(Ljava/lang/String;Landroid/app/appsearch/SearchSpec;)Landroid/app/appsearch/SearchResults;")