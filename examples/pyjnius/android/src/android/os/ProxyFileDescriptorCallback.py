from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProxyFileDescriptorCallback"]

class ProxyFileDescriptorCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/ProxyFileDescriptorCallback"
    __javaconstructor__ = [("()V", False)]
    onGetSize = JavaMethod("()J")
    onRead = JavaMethod("(JI[B)I")
    onWrite = JavaMethod("(JI[B)I")
    onFsync = JavaMethod("()V")
    onRelease = JavaMethod("()V")