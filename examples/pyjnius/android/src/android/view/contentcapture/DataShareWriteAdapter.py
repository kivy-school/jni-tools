from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DataShareWriteAdapter"]

class DataShareWriteAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/contentcapture/DataShareWriteAdapter"
    onRejected = JavaMethod("()V")
    onError = JavaMethod("(I)V")
    onWrite = JavaMethod("(Landroid/os/ParcelFileDescriptor;)V")