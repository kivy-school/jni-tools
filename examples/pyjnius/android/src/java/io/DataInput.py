from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DataInput"]

class DataInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/DataInput"
    readLine = JavaMethod("()Ljava/lang/String;")
    readInt = JavaMethod("()I")
    readUTF = JavaMethod("()Ljava/lang/String;")
    readUnsignedShort = JavaMethod("()I")
    readChar = JavaMethod("()C")
    readFloat = JavaMethod("()F")
    readFully = JavaMultipleMethod([("([BII)V", False, False), ("([B)V", False, False)])
    readLong = JavaMethod("()J")
    readByte = JavaMethod("()B")
    readShort = JavaMethod("()S")
    readUnsignedByte = JavaMethod("()I")
    skipBytes = JavaMethod("(I)I")
    readBoolean = JavaMethod("()Z")
    readDouble = JavaMethod("()D")