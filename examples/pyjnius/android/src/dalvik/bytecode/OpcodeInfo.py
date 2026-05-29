from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OpcodeInfo"]

class OpcodeInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/bytecode/OpcodeInfo"
    MAXIMUM_PACKED_VALUE = JavaStaticField("I")
    MAXIMUM_VALUE = JavaStaticField("I")