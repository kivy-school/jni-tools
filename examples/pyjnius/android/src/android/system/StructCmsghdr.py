from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StructCmsghdr"]

class StructCmsghdr(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/system/StructCmsghdr"
    __javaconstructor__ = [("(II[B)V", False), ("(IIS)V", False)]
    cmsg_data = JavaField("[B")
    cmsg_level = JavaField("I")
    cmsg_type = JavaField("I")