from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DataShareWriteAdapter"]

class DataShareWriteAdapter(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/contentcapture/DataShareWriteAdapter"
    onWrite = JavaMethod("(Landroid/os/ParcelFileDescriptor;)V")
    onRejected = JavaMethod("()V")
    onError = JavaMethod("(I)V")