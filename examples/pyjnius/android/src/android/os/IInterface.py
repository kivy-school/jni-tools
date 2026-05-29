from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IInterface"]

class IInterface(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/IInterface"
    asBinder = JavaMethod("()Landroid/os/IBinder;")