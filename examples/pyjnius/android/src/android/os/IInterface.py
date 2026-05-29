from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IInterface"]

class IInterface(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/IInterface"
    asBinder = JavaMethod("()Landroid/os/IBinder;")