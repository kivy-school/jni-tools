from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VmSocketAddress"]

class VmSocketAddress(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/system/VmSocketAddress"
    __javaconstructor__ = [("(II)V", False)]
    getSvmCid = JavaMethod("()I")
    getSvmPort = JavaMethod("()I")