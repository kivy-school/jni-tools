from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrintDocument"]

class PrintDocument(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/printservice/PrintDocument"
    getInfo = JavaMethod("()Landroid/print/PrintDocumentInfo;")
    getData = JavaMethod("()Landroid/os/ParcelFileDescriptor;")