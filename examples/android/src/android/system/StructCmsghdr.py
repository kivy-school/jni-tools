from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StructCmsghdr"]

class StructCmsghdr(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/system/StructCmsghdr"
    __javaconstructor__ = [("(IIS)V", False), ("(II[B)V", False)]
    cmsg_data = JavaField("[B")
    cmsg_level = JavaField("I")
    cmsg_type = JavaField("I")