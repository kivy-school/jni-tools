from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrintManager"]

class PrintManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/print/PrintManager"
    getPrintJobs = JavaMethod("()Ljava/util/List;")
    print = JavaMethod("(Ljava/lang/String;Landroid/print/PrintDocumentAdapter;Landroid/print/PrintAttributes;)Landroid/print/PrintJob;")
    isPrintServiceEnabled = JavaMethod("(Landroid/content/ComponentName;)Z")