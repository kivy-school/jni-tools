from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObserverCallback"]

class ObserverCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/observer/ObserverCallback"
    onSchemaChanged = JavaMethod("(Landroid/app/appsearch/observer/SchemaChangeInfo;)V")
    onDocumentChanged = JavaMethod("(Landroid/app/appsearch/observer/DocumentChangeInfo;)V")