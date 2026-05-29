from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObserverCallback"]

class ObserverCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/observer/ObserverCallback"
    onDocumentChanged = JavaMethod("(Landroid/app/appsearch/observer/DocumentChangeInfo;)V")
    onSchemaChanged = JavaMethod("(Landroid/app/appsearch/observer/SchemaChangeInfo;)V")