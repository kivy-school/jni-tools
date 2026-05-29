from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrintManager"]

class PrintManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/print/PrintManager"
    getPrintJobs = JavaMethod("()Ljava/util/List;")
    isPrintServiceEnabled = JavaMethod("(Landroid/content/ComponentName;)Z")
    print = JavaMethod("(Ljava/lang/String;Landroid/print/PrintDocumentAdapter;Landroid/print/PrintAttributes;)Landroid/print/PrintJob;")