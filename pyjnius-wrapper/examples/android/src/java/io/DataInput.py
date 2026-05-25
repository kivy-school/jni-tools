from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DataInput"]

class DataInput(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/DataInput"
    readFully = JavaMultipleMethod([("([B)V", False, False), ("([BII)V", False, False)])
    skipBytes = JavaMethod("(I)I")
    readBoolean = JavaMethod("()Z")
    readByte = JavaMethod("()B")
    readUnsignedByte = JavaMethod("()I")
    readShort = JavaMethod("()S")
    readUnsignedShort = JavaMethod("()I")
    readChar = JavaMethod("()C")
    readInt = JavaMethod("()I")
    readLong = JavaMethod("()J")
    readFloat = JavaMethod("()F")
    readDouble = JavaMethod("()D")
    readLine = JavaMethod("()Ljava/lang/String;")
    readUTF = JavaMethod("()Ljava/lang/String;")