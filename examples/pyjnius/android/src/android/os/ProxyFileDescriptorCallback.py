from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProxyFileDescriptorCallback"]

class ProxyFileDescriptorCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/ProxyFileDescriptorCallback"
    __javaconstructor__ = [("()V", False)]
    onGetSize = JavaMethod("()J")
    onFsync = JavaMethod("()V")
    onRead = JavaMethod("(JI[B)I")
    onRelease = JavaMethod("()V")
    onWrite = JavaMethod("(JI[B)I")