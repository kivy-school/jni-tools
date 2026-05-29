from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DataInputStream"]

class DataInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/DataInputStream"
    __javaconstructor__ = [("(Ljava/io/InputStream;)V", False)]
    readLine = JavaMethod("()Ljava/lang/String;")
    readInt = JavaMethod("()I")
    read = JavaMultipleMethod([("([B)I", False, False), ("([BII)I", False, False)])
    readUTF = JavaMultipleMethod([("()Ljava/lang/String;", False, False), ("(Ljava/io/DataInput;)Ljava/lang/String;", True, False)])
    readUnsignedShort = JavaMethod("()I")
    readChar = JavaMethod("()C")
    readFloat = JavaMethod("()F")
    readFully = JavaMultipleMethod([("([B)V", False, False), ("([BII)V", False, False)])
    readLong = JavaMethod("()J")
    readByte = JavaMethod("()B")
    readShort = JavaMethod("()S")
    readUnsignedByte = JavaMethod("()I")
    skipBytes = JavaMethod("(I)I")
    readBoolean = JavaMethod("()Z")
    readDouble = JavaMethod("()D")